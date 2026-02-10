import json
import os
import tempfile
from src import models

TASKS_FILE = "tasks.json"

def save_tasks(tasks, file_path=TASKS_FILE):
    data = {
        "version": "1.1",
        "tasks": [models.to_dict(t) for t in tasks]
    }
    dir_name = os.path.dirname(os.path.abspath(file_path)) or "."
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dir_name, encoding="utf-8") as tmp:
        json.dump(data, tmp, indent=2)
        temp_name = tmp.name
    try:
        os.replace(temp_name, file_path)
    except OSError:
        if os.path.exists(temp_name): os.remove(temp_name)
        raise

def load_tasks(file_path=TASKS_FILE):
    if not os.path.exists(file_path): return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not data or "tasks" not in data: return []
            return [models.from_dict(t) for t in data.get("tasks", [])]
    except: return []
