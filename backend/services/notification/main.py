from fastapi import FastAPI, Body
from dapr.ext.fastapi import DaprApp
from shared.models import TaskEvent
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("notification-service")

app = FastAPI(title="Notification Service")
dapr_app = DaprApp(app)

PUB_SUB_NAME = "pubsub"
TOPIC_NAME = "todo.tasks.lifecycle"

@dapr_app.subscribe(pubsub=PUB_SUB_NAME, topic=TOPIC_NAME)
async def task_event_handler(event_data: dict = Body(...)):
    # Dapr sends the event wrapped in a CloudEvent envelope
    # event_data['data'] will contain our TaskEvent
    data = event_data.get('data')
    if isinstance(data, str):
        data = json.loads(data)
    
    event = TaskEvent(**data)
    logger.info(f"NOTIFICATION RECEIVED: [{event.event_type}] from {event.source}")
    logger.info(f"Payload: {event.payload}")
    
    return {"status": "SUCCESS"}

@app.get("/health")
async def health():
    return {"status": "ok"}
