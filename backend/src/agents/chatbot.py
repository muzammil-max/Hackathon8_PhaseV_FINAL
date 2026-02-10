import os
import asyncio
from typing import List, Optional, Dict, Any
from openai import AsyncOpenAI
from agents import Agent, Runner, set_default_openai_client, function_tool, ModelSettings, set_tracing_disabled, OpenAIChatCompletionsModel
from src.config import settings
from src.agents.tools import (
    create_task_tool, 
    list_tasks_tool, 
    update_task_tool, 
    delete_task_tool
)

# Configure Gemini via OpenAI SDK (OpenRouter)
GEMINI_API_KEY = settings.GEMINI_API_KEY
client = None
if GEMINI_API_KEY:
    # Disable tracing to avoid 401 errors from OpenAI-specific telemetry
    set_tracing_disabled(True)
    
    # Set default client for the entire process (using OpenRouter)
    client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        default_headers={
            "HTTP-Referer": "http://localhost:3000",
            "X-Title": "MyTodoApp",
        }
    )
    set_default_openai_client(client)
    # Set OPENAI_API_KEY to satisfy internal SDK requirements
    os.environ["OPENAI_API_KEY"] = GEMINI_API_KEY

class TodoChatbot:
    def __init__(self, db, user_id: str):
        self.db = db
        self.user_id = user_id
        # Lock to ensure sequential database access per chatbot instance
        self.lock = asyncio.Lock()
        
        # Define local functions that wrap the tools with session, user context, and Lock
        async def create_task(title: str, description: Optional[str] = None, status: str = "TODO", priority: str = "MEDIUM") -> str:
            """
            Create a new task for the user.
            Args:
                title: The title of the task.
                description: A detailed description of the task.
                status: The status of the task (TODO, IN_PROGRESS, DONE).
                priority: The priority of the task (LOW, MEDIUM, HIGH).
            """
            async with self.lock:
                return await create_task_tool(self.db, self.user_id, title, description, status, priority)

        async def list_tasks(status: Optional[str] = None) -> str:
            """
            List tasks for the user.
            Args:
                status: Optional filter by status (TODO, IN_PROGRESS, DONE).
            """
            async with self.lock:
                return await list_tasks_tool(self.db, self.user_id, status)

        async def update_task(task_id: str, title: Optional[str] = None, description: Optional[str] = None, status: Optional[str] = None, priority: Optional[str] = None) -> str:
            """
            Update an existing task.
            Args:
                task_id: The UUID of the task to update.
                title: New title for the task.
                description: New description for the task.
                status: New status for the task.
                priority: New priority for the task.
            """
            async with self.lock:
                return await update_task_tool(self.db, self.user_id, task_id, title, description, status, priority)

        async def delete_task(task_id: str) -> str:
            """
            Delete a task.
            Args:
                task_id: The UUID of the task to delete.
            """
            async with self.lock:
                return await delete_task_tool(self.db, self.user_id, task_id)

        # Wrap OpenRouter model to bypass SDK prefix validation
        gemini_model = OpenAIChatCompletionsModel(
            model="google/gemini-2.0-flash-001",
            openai_client=client
        ) if client else "gpt-4o"

        self.agent = Agent(
            name="TodoBot",
            model=gemini_model,
            instructions=(
                "You are an extremely concise Todo List assistant. "
                "Actions: Create, List, Update (Mark Done), Delete. "
                "Instructions: "
                "1. BE BRIEF. No conversational filler like 'Sure, I can help'. "
                "2. When asked to update/complete/delete a task, ALWAYS call 'list_tasks' first to find the ID. "
                "3. To mark a task as DONE, use 'update_task' with status='DONE'. "
                "4. Confirm actions with a single short sentence: 'Done: Task marked complete.' or 'Task created.' "
                "5. Never ask follow-up questions unless the request is truly ambiguous."
            ),
            tools=[
                function_tool(create_task), 
                function_tool(list_tasks), 
                function_tool(update_task), 
                function_tool(delete_task)
            ],
            model_settings=ModelSettings(temperature=0.1, max_tokens=1024, parallel_tool_calls=False)
        )

    async def get_response(self, messages: List[Dict[str, Any]]) -> Any:
        """
        Process a list of messages and return the agent's response.
        """
        runner = Runner()
        result = await runner.run(self.agent, messages)
        return result