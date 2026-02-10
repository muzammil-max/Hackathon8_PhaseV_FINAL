from fastapi import FastAPI, Body
from dapr.ext.fastapi import DaprApp
from dapr.clients import DaprClient
from shared.models import TaskEvent, Task, RecurrenceType
import logging
import json
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("scheduler-service")

app = FastAPI(title="Scheduler Service")
dapr_app = DaprApp(app)

PUB_SUB_NAME = "pubsub"
TOPIC_NAME = "todo.tasks.lifecycle"
TASK_SERVICE_APP_ID = "task-service"

@dapr_app.subscribe(pubsub=PUB_SUB_NAME, topic=TOPIC_NAME)
async def handle_task_events(event_data: dict = Body(...)):
    data = event_data.get('data')
    if isinstance(data, str):
        data = json.loads(data)
    
    event = TaskEvent(**data)
    
    if event.event_type == "TaskCreated":
        task_dict = event.payload.get("task")
        if task_dict:
            task = Task(**task_dict)
            if task.recurrence:
                logger.info(f"Scheduling recurrence for task: {task.id}")
                # In a real system, we'd use Dapr Cron binding or a persistent job queue
                # For Phase 5 demonstration, we log the intent
    
    return {"status": "SUCCESS"}

@app.post("/trigger-recurrence")
async def trigger_recurrence(payload: dict = Body(...)):
    """
    This endpoint would be called by a Dapr Cron binding to check for recurring tasks.
    """
    task_id = payload.get("task_id")
    logger.info(f"Triggering next instance for task: {task_id}")
    
    with DaprClient() as d:
        # 1. Get original task
        resp = d.invoke_method(TASK_SERVICE_APP_ID, f"tasks/{task_id}", http_verb="GET")
        original_task = Task.parse_raw(resp.data)
        
        if original_task.recurrence:
            # 2. Create new task based on recurrence rule
            new_task_data = original_task.dict(exclude={'id', 'created_at', 'updated_at'})
            # Simple logic: add 1 interval to due_date
            if original_task.due_date:
                if original_task.recurrence.type == RecurrenceType.DAILY:
                    new_task_data['due_date'] = original_task.due_date + timedelta(days=original_task.recurrence.interval)
                elif original_task.recurrence.type == RecurrenceType.WEEKLY:
                    new_task_data['due_date'] = original_task.due_date + timedelta(weeks=original_task.recurrence.interval)
            
            # 3. Invoke Task Service to create new instance
            d.invoke_method(
                TASK_SERVICE_APP_ID, 
                "tasks", 
                data=json.dumps(new_task_data), 
                http_verb="POST"
            )
            
    return {"status": "triggered"}
