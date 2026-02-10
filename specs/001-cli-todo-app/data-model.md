# Data Model: CLI Todo App

**Feature**: `001-cli-todo-app`

## Entities

### Task

Represents a single unit of work.

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| `id` | Integer | Yes | Unique identifier | > 0, Auto-incrementing |
| `description` | String | Yes | Content of the task | Non-empty, max 1000 chars |
| `status` | String | Yes | Current state | Enum: `pending`, `completed` |
| `created_at` | ISO 8601 String | Yes | Creation timestamp | UTC |
| `updated_at` | ISO 8601 String | Yes | Last modification | UTC |

## Storage Schema (JSON)

The application will persist data in a JSON file containing a list of task objects and metadata.

```json
{
  "version": "1.0",
  "last_id": 5,
  "tasks": [
    {
      "id": 1,
      "description": "Buy milk",
      "status": "pending",
      "created_at": "2026-01-01T10:00:00Z",
      "updated_at": "2026-01-01T10:00:00Z"
    }
  ]
}
```

## State Transitions

- **Create**: Status `pending`, `created_at` = now, `updated_at` = now.
- **Update**: `description` changes, `updated_at` = now.
- **Complete**: Status `pending` -> `completed`, `updated_at` = now.
- **Uncomplete** (optional): Status `completed` -> `pending`.
