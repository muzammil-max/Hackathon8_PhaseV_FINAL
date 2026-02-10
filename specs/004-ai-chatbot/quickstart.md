# Quickstart: AI Chatbot System

## Interaction via API

1. **Obtain JWT**: Login via `/api/auth/login` to get your access token.
2. **Start a Conversation**:
   ```bash
   curl -X POST http://localhost:8000/api/chat 
     -H "Authorization: Bearer <YOUR_TOKEN>" 
     -H "Content-Type: application/json" 
     -d '{"message": "Add a task to buy groceries"}'
   ```
3. **Continue the Conversation**: Use the `conversation_id` returned from the first response.
   ```bash
   curl -X POST http://localhost:8000/api/chat 
     -H "Authorization: Bearer <YOUR_TOKEN>" 
     -H "Content-Type: application/json" 
     -d '{"conversation_id": "YOUR_CONVO_ID", "message": "List my tasks"}'
   ```

## Key Chat Commands
- "Add [task title]"
- "What's on my list?"
- "Mark [task title] as done"
- "Delete [task title]"
- "Change task [title] to [new title]"
