# API & Event Contracts: Advanced Cloud-Native Deployment

**Feature**: `006-advanced-cloud-deployment`

## 1. Chat Interface Service (Public API)
*Gateway for the AI Chatbot interaction.*

### `POST /api/chat`
Process a natural language user command.
- **Request**:
  ```json
  { "message": "Remind me to buy milk tomorrow", "context": {} }
  ```
- **Response**:
  ```json
  { "response": "I've added 'Buy milk' to your task list for tomorrow.", "actions_taken": [...] }
  ```

---

## 2. Task Service (Dapr Internal API)
*Invoked via Dapr Service Invocation: `http://localhost:3500/v1.0/invoke/task-service/method/{method}`*

### `POST /tasks`
Create a new task.
- **Payload**: `Task` object (minus ID/timestamps).
- **Response**: Full `Task` object.

### `GET /tasks`
Search/Filter tasks.
- **Query Params**: `?status=pending&priority=high&tag=urgent`
- **Response**: `[ Task, ... ]`

### `PATCH /tasks/{id}`
Update a task.
- **Payload**: Partial `Task` object.
- **Response**: Updated `Task` object.

---

## 3. Event Schemas (Pub/Sub)
*Topic: `todo.tasks.lifecycle`*

### `TaskCreated`
```json
{
  "event_type": "TaskCreated",
  "payload": { "task": { ...full task object... } }
}
```

### `TaskCompleted`
```json
{
  "event_type": "TaskCompleted",
  "payload": { "task_id": "uuid", "completed_at": "ISO-timestamp" }
}
```

---

## 4. Scheduler Service (Internal)
*Invoked via Dapr Bindings or Pub/Sub*

### Topic: `todo.jobs.recurrence`
Trigger creation of the next task instance.
- **Payload**: `{ "original_task_id": "uuid", "recurrence_rule": {...} }`
