from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database import get_session
from src.auth import get_current_user
from src.models import User, Conversation, Message, MessageRole
from src.agents.chatbot import TodoChatbot
from agents import ToolCallItem
from pydantic import BaseModel
import uuid
from typing import Optional
from datetime import datetime

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None

@router.post("/")
async def chat(
    request: ChatRequest,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    # 1. Resolve Conversation
    if request.conversation_id:
        try:
            convo_uuid = uuid.UUID(request.conversation_id)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid conversation_id format")
        
        statement = select(Conversation).where(Conversation.id == convo_uuid, Conversation.user_id == current_user.id)
        result = await db.execute(statement)
        conversation = result.scalars().first()
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found or access denied")
    else:
        # Create new conversation
        conversation = Conversation(user_id=current_user.id)
        db.add(conversation)
        await db.commit()
        await db.refresh(conversation)

    # 2. Store User Message
    user_msg = Message(
        conversation_id=conversation.id, 
        role=MessageRole.USER, 
        content=request.message
    )
    db.add(user_msg)
    await db.commit()

    # 3. Load History (Last 15 messages for more context)
    history_statement = select(Message).where(Message.conversation_id == conversation.id).order_by(Message.created_at.desc()).limit(16)
    result = await db.execute(history_statement)
    messages_objs = result.scalars().all()
    messages_objs = list(messages_objs)
    messages_objs.reverse()
    
    agent_messages = []
    for msg in messages_objs:
        role_val = msg.role.value
        m = {
            "role": role_val,
            "content": msg.content or ""
        }
        
        # SDK Requirement: 'name' is only for 'tool' (and sometimes 'system')
        # 'assistant' messages with a 'name' field cause Unhandled item errors.
        if role_val == "tool":
            m["tool_call_id"] = msg.tool_call_id
            m["name"] = msg.name
        elif role_val == "assistant":
            if msg.tool_calls:
                import json
                m["tool_calls"] = json.loads(msg.tool_calls)
            # DO NOT add 'name' to assistant role
        elif role_val == "system":
            if msg.name:
                m["name"] = msg.name
                
        agent_messages.append(m)

    # 4. Run Agent
    bot = TodoChatbot(db, current_user.id)
    try:
        # Result is a RunResult object
        result = await bot.get_response(agent_messages)
        
        # 5. Identify and Store NEW messages
        full_history = result.to_input_list()
        new_messages = full_history[len(agent_messages):]
        
        import json
        for msg in new_messages:
            try:
                role_str = msg.get("role", "assistant").lower()
                # Validate role
                if role_str not in [r.value for r in MessageRole]:
                    role_str = "assistant"
                
                content = msg.get("content")
                if isinstance(content, list):
                    # Flatten text content
                    text_parts = [item.get("text", "") for item in content if isinstance(item, dict) and item.get("type") == "output_text"]
                    content = "".join(text_parts).strip()
                elif content is None:
                    content = ""

                new_msg = Message(
                    conversation_id=conversation.id,
                    role=MessageRole(role_str),
                    content=content,
                    tool_calls=json.dumps(msg.get("tool_calls")) if msg.get("tool_calls") else None,
                    tool_call_id=msg.get("tool_call_id"),
                    name=msg.get("name")
                )
                db.add(new_msg)
            except Exception as msg_err:
                print(f"Error processing message for DB: {msg_err}")
                print(f"Message dict: {msg}")
        
        await db.commit()

        # Update conversation timestamp
        conversation.updated_at = datetime.utcnow()
        db.add(conversation)
        await db.commit()

        # Extract the final response text
        response_text = result.final_output
        if not response_text and len(new_messages) > 0:
            last_msg = new_messages[-1]
            response_text = last_msg.get("content")
            if isinstance(response_text, list):
                text_parts = [item.get("text", "") for item in response_text if isinstance(item, dict) and item.get("type") == "output_text"]
                response_text = "".join(text_parts).strip()

        # Extract tool calls for frontend indicator
        frontend_tool_calls = []
        if hasattr(result, "new_items"):
            for item in result.new_items:
                if isinstance(item, ToolCallItem):
                    tool_name = "unknown"
                    if hasattr(item.raw_item, "name"):
                        tool_name = item.raw_item.name
                    elif hasattr(item.raw_item, "function") and hasattr(item.raw_item.function, "name"):
                        tool_name = item.raw_item.function.name
                    
                    frontend_tool_calls.append({"function": {"name": tool_name}})

        return {
            "conversation_id": str(conversation.id),
            "response": response_text or "I processed your request.",
            "tool_calls": frontend_tool_calls
        }
        
    except Exception as e:
        await db.rollback() # Crucial: Reset session state on error
        import traceback
        print(f"Chat Route Error: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"AI Agent failed: {str(e)}")
