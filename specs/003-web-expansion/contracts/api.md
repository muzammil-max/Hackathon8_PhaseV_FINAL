# API Contract: Phase 2 Web Expansion

**Protocol**: REST over HTTP
**Format**: JSON
**Auth**: Bearer JWT in `Authorization` header required for all endpoints.

## Endpoints

### 1. List Tasks
**GET** `/api/tasks`

- **Auth**: Required
- **Response**: `200 OK`
  ```json
  [
    {
      "id": "uuid",
      "title": "Buy milk",
      "status": "TODO",
      "created_at": "iso-date"
    }
  ]
  ```

### 2. Create Task
**POST** `/api/tasks`

- **Auth**: Required
- **Body**:
  ```json
  {
    "title": "New Task",
    "priority": "MEDIUM"  // optional
  }
  ```
- **Response**: `201 Created`
  ```json
  {
    "id": "new-uuid",
    "title": "New Task",
    "status": "TODO",
    "owner_id": "current-user-id",
    ...
  }
  ```

### 3. Get Task
**GET** `/api/tasks/{id}`

- **Auth**: Required
- **Response**: `200 OK` (Task object)
- **Error**: `404 Not Found` (if not found or belongs to another user)

### 4. Update Task
**PUT** `/api/tasks/{id}`

- **Auth**: Required
- **Body**: (Partial or full update fields)
  ```json
  {
    "title": "Updated Title",
    "status": "IN_PROGRESS"
  }
  ```
- **Response**: `200 OK` (Updated task)

### 5. Delete Task
**DELETE** `/api/tasks/{id}`

- **Auth**: Required
- **Response**: `204 No Content`

### 6. Toggle Completion
**PATCH** `/api/tasks/{id}/complete`

- **Auth**: Required
- **Response**: `200 OK`
  ```json
  {
    "id": "...",
    "status": "DONE" // or "TODO" if toggled back
  }
  ```

## Error Codes

- `400 Bad Request`: Validation failure.
- `401 Unauthorized`: Missing or invalid JWT.
- `403 Forbidden`: Valid JWT but insufficient permissions (e.g., trying to access another user's resource, though 404 is preferred for privacy).
- `404 Not Found`: Resource does not exist or user does not own it.
- `500 Internal Server Error`: Unexpected server error.
