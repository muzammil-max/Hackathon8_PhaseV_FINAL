# API Contract: /api/chat

## Endpoint: `POST /api/chat`

Handles natural language messages, processes them via an AI agent, and returns the response.

### Headers
- `Authorization: Bearer <JWT_TOKEN>`
- `Content-Type: application/json`

### Request Body
```json
{
  "conversation_id": "uuid-string (optional)",
  "message": "string (required)"
}
```

### Success Response (200 OK)
```json
{
  "conversation_id": "uuid-string",
  "response": "string (assistant message)",
  "tool_calls": [
    {
      "name": "create_task",
      "arguments": { "title": "Buy milk" },
      "output": { "id": 123, "status": "success" }
    }
  ]
}
```

### Error Responses
- **401 Unauthorized**: Missing or invalid JWT.
- **403 Forbidden**: User does not own the requested `conversation_id`.
- **400 Bad Request**: Missing message or malformed JSON.
- **500 Internal Server Error**: Agent failure or database error.

### Constraints
- `conversation_id` must be a valid UUID if provided.
- `message` cannot be empty.
- JWT must contain `sub` (user_id).
