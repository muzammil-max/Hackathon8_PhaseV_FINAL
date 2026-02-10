from fastapi import FastAPI, Body
from dapr.clients import DaprClient
import os
import json

app = FastAPI(title="Chat Service")
TASK_SERVICE_APP_ID = "task-service"

@app.post("/api/chat")
async def chat(payload: dict = Body(...)):
    message = payload.get("message", "")
    
    # Placeholder for AI logic (Gemini/NLP)
    # For now, simple keyword matching to demonstrate Dapr invocation
    
    if "add" in message.lower() or "create" in message.lower():
        # Mock parsing logic
        clean_msg = message.lower().replace("add", "").replace("create", "").strip()
        
        priority = "medium"
        if "urgent" in clean_msg or "high" in clean_msg: priority = "high"
        if "low" in clean_msg: priority = "low"
        
        tags = []
        if "#" in clean_msg:
            tags = [word.replace("#", "") for word in clean_msg.split() if word.startswith("#")]
        
        recurrence = None
        if "every" in clean_msg:
            if "day" in clean_msg: recurrence = {"type": "daily"}
            elif "week" in clean_msg: recurrence = {"type": "weekly"}

        task_data = {
            "title": clean_msg.split("#")[0].replace("urgent", "").replace("high", "").replace("low", "").replace("every day", "").replace("every week", "").strip() or "New Task",
            "priority": priority,
            "tags": tags,
            "recurrence": recurrence
        }
        
        with DaprClient() as d:
            resp = d.invoke_method(
                TASK_SERVICE_APP_ID,
                "tasks",
                data=json.dumps(task_data),
                http_verb="POST"
            )
            created_task = json.loads(resp.data)
            
        return {
            "response": f"I've added the task: '{created_task['title']}'",
            "task": created_task
        }

    if "search" in message.lower() or "find" in message.lower() or "list" in message.lower():
        query = message.replace("search", "").replace("find", "").replace("list", "").strip()
        
        with DaprClient() as d:
            method = "tasks/search" if query else "tasks"
            query_param = f"?query={query}" if query else ""
            
            resp = d.invoke_method(
                TASK_SERVICE_APP_ID,
                method + query_param,
                http_verb="GET"
            )
            tasks = json.loads(resp.data)
            
        if not tasks:
            return {"response": f"I couldn't find any tasks matching '{query}'."}
        
        task_list = "\n".join([f"- {t['title']} ({t['status']})" for t in tasks])
        return {
            "response": f"Here is what I found:\n{task_list}",
            "tasks": tasks
        }

    return {
        "response": "I heard you, but I don't know how to handle that yet. Try 'add Buy Milk'.",
        "echo": message
    }
