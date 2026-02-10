import json
import uuid
from typing import List, Optional, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import Task, TaskStatus, TaskPriority

class ToolResult:
    def __init__(self, success: bool, data: Any = None, error: str = None):
        self.success = success
        self.data = data
        self.error = error

    def to_json(self) -> str:
        return json.dumps({
            "success": self.success,
            "data": self.data,
            "error": self.error
        })

# Base MCP Tool Wrapper
# In a real MCP setup, these would be registered with an MCP server.
# For this implementation, they will be used by the OpenAI Agents SDK.

def format_task(task: Task) -> dict:
    return {
        "id": str(task.id),
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority": task.priority,
        "created_at": task.created_at.isoformat()
    }

async def create_task_tool(db: AsyncSession, user_id: str, title: str, description: Optional[str] = None, status: str = "TODO", priority: str = "MEDIUM") -> str:

    """Create a new task for the authenticated user."""

    print(f"Tool [create_task]: user={user_id} title='{title}' status={status}")

    # Explicitly convert strings to Enums

    task_status = TaskStatus(status.upper()) if isinstance(status, str) else status

    task_priority = TaskPriority(priority.upper()) if isinstance(priority, str) else priority

    

    task = Task(title=title, description=description, status=task_status, priority=task_priority, owner_id=user_id)

    db.add(task)

    await db.commit()

    await db.refresh(task)

    return json.dumps(format_task(task))



async def list_tasks_tool(db: AsyncSession, user_id: str, status: Optional[str] = None) -> str:

    """List all tasks for the authenticated user, optionally filtered by status."""

    print(f"Tool [list_tasks]: user={user_id} status_filter={status}")

    statement = select(Task).where(Task.owner_id == user_id)

    if status:

        task_status = TaskStatus(status.upper()) if isinstance(status, str) else status

        statement = statement.where(Task.status == task_status)

    result = await db.execute(statement)

    tasks = result.scalars().all()

    return json.dumps([format_task(t) for t in tasks])



async def update_task_tool(db: AsyncSession, user_id: str, task_id: str, title: Optional[str] = None, description: Optional[str] = None, status: Optional[str] = None, priority: Optional[str] = None) -> str:

    """Update an existing task for the authenticated user."""

    print(f"Tool [update_task]: id={task_id} status_update={status}")

    try:

        task_uuid = uuid.UUID(task_id)

    except ValueError:

        return json.dumps({"error": "Invalid task ID format"})

        

    statement = select(Task).where(Task.id == task_uuid, Task.owner_id == user_id)

    result = await db.execute(statement)

    task = result.scalars().first()

    if not task:

        print(f"Tool [update_task]: Task {task_id} NOT FOUND for user {user_id}")

        return json.dumps({"error": "Task not found or access denied"})

    

    if title is not None:

        task.title = title

    if description is not None:

        task.description = description

    if status is not None:

        task.status = TaskStatus(status.upper()) if isinstance(status, str) else status

    if priority is not None:

        task.priority = TaskPriority(priority.upper()) if isinstance(priority, str) else priority

        

    db.add(task)

    await db.commit()

    await db.refresh(task)

    print(f"Tool [update_task]: Task {task_id} UPDATED successfully. New status: {task.status}")

    return json.dumps(format_task(task))



async def delete_task_tool(db: AsyncSession, user_id: str, task_id: str) -> str:

    """Delete a task for the authenticated user."""

    print(f"Tool [delete_task]: id={task_id}")
