from fastapi import FastAPI, HTTPException, Body
from dapr.clients import DaprClient
from shared.models import Task, TaskStatus, TaskEvent
import os
import json
from datetime import datetime

app = FastAPI(title="Task Service")
DAPR_STORE_NAME = "statestore"
PUB_SUB_NAME = "pubsub"
TOPIC_NAME = "todo.tasks.lifecycle"

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    with DaprClient() as d:
        # Save state
        d.save_state(DAPR_STORE_NAME, f"task::{task.id}", task.json())
        
        # Update task_ids index
        ids_state = d.get_state(DAPR_STORE_NAME, "task_ids")
        ids = json.loads(ids_state.data) if ids_state.data else []
        if task.id not in ids:
            ids.append(task.id)
            d.save_state(DAPR_STORE_NAME, "task_ids", json.dumps(ids))

        # Emit event
        event = TaskEvent(
            event_type="TaskCreated",
            source="task-service",
            payload={"task": task.dict()}
        )
        d.publish_event(PUB_SUB_NAME, TOPIC_NAME, event.json())
        
    return task

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: str):
    with DaprClient() as d:
        state = d.get_state(DAPR_STORE_NAME, f"task::{task_id}")
        if not state.data:
            raise HTTPException(status_code=404, detail="Task not found")
        return Task.parse_raw(state.data)

@app.get("/tasks", response_model=List[Task])
async def list_tasks(status: Optional[str] = None, priority: Optional[str] = None, tag: Optional[str] = None):
    tasks = []
    with DaprClient() as d:
        # For Phase 5, we simulate a scan/filter. 
        # In production Dapr, we'd use d.query_state() with a JSON query.
        # Since we don't have the Query API metadata configured here, we'll use a prefix scan if supported or 
        # a mock that assumes we have a list of all IDs.
        
        # Mock: In a real demo, we might maintain a 'task_ids' list in state
        all_ids_state = d.get_state(DAPR_STORE_NAME, "task_ids")
        if all_ids_state.data:
            ids = json.loads(all_ids_state.data)
            for tid in ids:
                t_state = d.get_state(DAPR_STORE_NAME, f"task::{tid}")
                if t_state.data:
                    task = Task.parse_raw(t_state.data)
                    # Filter logic
                    if status and task.status != status: continue
                    if priority and task.priority != priority: continue
                    if tag and tag not in task.tags: continue
                    tasks.append(task)
    return tasks

@app.get("/tasks/search")
async def search_tasks(query: str):
    results = []
    with DaprClient() as d:
        # Simple keyword search in title/description
        all_ids_state = d.get_state(DAPR_STORE_NAME, "task_ids")
        if all_ids_state.data:
            ids = json.loads(all_ids_state.data)
            for tid in ids:
                t_state = d.get_state(DAPR_STORE_NAME, f"task::{tid}")
                if t_state.data:
                    task = Task.parse_raw(t_state.data)
                    if query.lower() in task.title.lower() or (task.description and query.lower() in task.description.lower()):
                        results.append(task)
    return results

@app.patch("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, updates: dict):
    with DaprClient() as d:
        state = d.get_state(DAPR_STORE_NAME, f"task::{task_id}")
        if not state.data:
            raise HTTPException(status_code=404, detail="Task not found")
        
        task = Task.parse_raw(state.data)
        updated_data = task.dict()
        updated_data.update(updates)
        updated_data['updated_at'] = datetime.utcnow()
        updated_task = Task(**updated_data)
        
        d.save_state(DAPR_STORE_NAME, f"task::{task_id}", updated_task.json())
        
        # Emit event
        event = TaskEvent(
            event_type="TaskUpdated",
            source="task-service",
            payload={"task_id": task_id, "changes": updates}
        )
        d.publish_event(PUB_SUB_NAME, TOPIC_NAME, event.json())
        
        return updated_task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    with DaprClient() as d:
        d.delete_state(DAPR_STORE_NAME, f"task::{task_id}")
        
        # Emit event
        event = TaskEvent(
            event_type="TaskDeleted",
            source="task-service",
            payload={"task_id": task_id}
        )
        d.publish_event(PUB_SUB_NAME, TOPIC_NAME, event.json())
        
    return {"status": "deleted"}
