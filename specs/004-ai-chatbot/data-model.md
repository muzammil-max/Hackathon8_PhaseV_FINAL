# Data Model: AI Chatbot System

## Entities

### Conversation
Represents a unique chat session between a user and the AI.
- `id`: UUID (Primary Key)
- `user_id`: UUID (Foreign Key to User)
- `title`: String (Optional, e.g., first few words of first message)
- `created_at`: DateTime
- `updated_at`: DateTime

### Message
An individual message within a conversation.
- `id`: UUID (Primary Key)
- `conversation_id`: UUID (Foreign Key to Conversation)
- `role`: Enum (user, assistant, system, tool)
- `content`: Text (The message body or tool output)
- `tool_calls`: JSON (Optional, if the message contains tool calls)
- `created_at`: DateTime

### Task (Updated/Existing)
- `id`: Integer (Primary Key)
- `user_id`: UUID (Foreign Key to User)
- `title`: String
- `description`: String (Optional)
- `is_completed`: Boolean
- `created_at`: DateTime

## Relationships
- A **User** has many **Conversations**.
- A **Conversation** has many **Messages**.
- A **Message** belongs to one **Conversation**.
- A **User** has many **Tasks**.

## State Transitions
1. **Chat Request**: `POST /api/chat`
2. **Conversation Lookup**: If `conversation_id` exists, verify ownership. If not, create new.
3. **History Load**: Load recent `Messages` for the `conversation_id`.
4. **Agent Execution**: Agent processes history + new message.
5. **Tool Calls**: Agent triggers MCP tools (stateless).
6. **Persist**: Store User message and Assistant response (and tool outputs) in the `Message` table.
7. **Response**: Return result to user.
