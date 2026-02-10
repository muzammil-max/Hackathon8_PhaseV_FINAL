# Data Model: Advanced Cloud-Native Deployment

**Feature**: `006-advanced-cloud-deployment`
**Date**: 2026-02-09

## Entities

### 1. Task
The core unit of work, stored in Dapr State.

```json
{
  "id": "uuid-string",
  "title": "string",
  "description": "string",
  "status": "pending | completed | deleted",
  "priority": "low | medium | high",
  "tags": ["string"],
  "due_date": "ISO8601-timestamp (optional)",
  "recurrence": {
    "type": "daily | weekly | custom",
    "interval": "integer",
    "end_date": "ISO8601-timestamp (optional)"
  },
  "created_at": "ISO8601-timestamp",
  "updated_at": "ISO8601-timestamp"
}
```

### 2. TaskEvent
The standard payload for all Kafka events.

```json
{
  "event_id": "uuid-string",
  "event_type": "TaskCreated | TaskUpdated | TaskCompleted | TaskDeleted | ReminderDue",
  "timestamp": "ISO8601-timestamp",
  "source": "service-name",
  "payload": {
    // Partial or full Task object, or specific action details
    "task_id": "uuid-string",
    "changes": { ... }
  }
}
```

## Dapr State Key Design

- **Tasks**: `task::{task_id}`
- **Indexes** (if manual indexing needed): `index::tag::{tag_name} -> [task_id_list]`

## Event Topics

| Topic Name | Publisher | Consumers | Description |
|------------|-----------|-----------|-------------|
| `todo.tasks.lifecycle` | Task Service | Scheduler, Notification | All CRUD lifecycle events |
| `todo.reminders` | Scheduler Service | Notification | When a reminder or due date is triggered |
| `todo.jobs` | Scheduler Service | Task Service | Triggers for creating next recurring instance |

## Validation Rules
- `title`: Not empty, max 200 chars.
- `priority`: Default "medium".
- `recurrence`: If present, must have valid type.
