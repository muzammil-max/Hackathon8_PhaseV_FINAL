# Data Model: Advanced CLI Todo Features

**Feature**: `002-cli-todo-advanced`

## Entities

### Task (Updated)

Extends the MVP Task entity.

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| `id` | Integer | Yes | Unique identifier | > 0, Auto-incrementing |
| `description` | String | Yes | Content of the task | Non-empty |
| `status` | String | Yes | Current state | `pending`, `completed` |
| `priority` | String | No | Urgency level | `high`, `medium`, `low` (Default: `medium`) |
| `tags` | List[String] | No | Categories | Alphanumeric, lowercase |
| `due_date` | String | No | Deadline (ISO 8601) | Valid timestamp |
| `recurrence` | String | No | Repeat pattern | `daily`, `weekly`, `monthly` |
| `created_at` | String | Yes | Creation timestamp | ISO 8601 |
| `updated_at` | String | Yes | Last modification | ISO 8601 |

## Storage Schema (JSON)

Backward compatible update to `tasks.json`. New fields are optional.

```json
{
  "version": "1.1",
  "last_id": 10,
  "tasks": [
    {
      "id": 1,
      "description": "Buy milk",
      "status": "pending",
      "priority": "medium",
      "tags": ["personal", "shopping"],
      "due_date": "2026-01-02T10:00:00",
      "recurrence": null,
      "created_at": "...",
      "updated_at": "..."
    }
  ]
}
```

## State Transitions

- **Mark Done (Recurring)**:
  - If `recurrence` is set:
    - Mark current task `completed`.
    - Create NEW task with:
      - `description` = same
      - `priority`, `tags`, `recurrence` = same
      - `due_date` = `due_date` + interval
      - `status` = `pending`
