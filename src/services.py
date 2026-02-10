from typing import List, Optional
from src import models, storage, utils
from datetime import datetime, timezone, timedelta

def add_task(description: str, priority: str = "medium", tags: List[str] = None, due_date: str = None, recurrence: str = None):
    tasks = storage.load_tasks()
    new_id = 1
    if tasks:
        new_id = max(t.id for t in tasks) + 1
    task = models.Task.create(new_id, description, priority, tags, due_date, recurrence)
    tasks.append(task)
    storage.save_tasks(tasks)
    return task

def list_tasks(filter_by: Optional[str] = None, sort_by: Optional[str] = None):
    tasks = storage.load_tasks()
    if filter_by:
        tasks = filter_tasks(tasks, filter_by)
    if sort_by:
        tasks = sort_tasks(tasks, sort_by)
    return tasks

def filter_tasks(tasks, filter_expr):
    try:
        if "=" not in filter_expr: return tasks
        key, val = filter_expr.split("=", 1)
        if key == "status": return [t for t in tasks if t.status == val]
        if key == "priority": return [t for t in tasks if t.priority == val]
        if key == "tag": return [t for t in tasks if val in t.tags]
    except: pass
    return tasks

def sort_tasks(tasks, sort_key):
    if sort_key == "priority":
        prio_map = {"high": 0, "medium": 1, "low": 2}
        return sorted(tasks, key=lambda t: prio_map.get(t.priority, 1))
    if sort_key == "due_date":
        return sorted(tasks, key=lambda t: t.due_date or "9999-12-31")
    if sort_key == "created_at":
        return sorted(tasks, key=lambda t: t.created_at, reverse=True)
    return tasks

def search_tasks(keyword):
    tasks = storage.load_tasks()
    k = keyword.lower()
    return [t for t in tasks if k in t.description.lower() or any(k in tag.lower() for tag in t.tags)]

def update_task(task_id, description=None, priority=None, tags=None, due_date=None, recurrence=None):
    tasks = storage.load_tasks()
    task = next((t for t in tasks if t.id == task_id), None)
    if task:
        if description is not None: task.description = description
        if priority is not None: task.priority = priority
        if tags is not None: task.tags = tags
        if due_date is not None: task.due_date = due_date
        if recurrence is not None: task.recurrence = recurrence
        task.updated_at = datetime.now(timezone.utc).isoformat()
        storage.save_tasks(tasks)
        return task
    return None

def calculate_next_due(current_due, pattern):
    dt = datetime.fromisoformat(current_due)
    if pattern == "daily": dt += timedelta(days=1)
    elif pattern == "weekly": dt += timedelta(weeks=1)
    elif pattern == "monthly": dt += timedelta(days=30)
    return dt.isoformat()

def mark_done(task_id):
    tasks = storage.load_tasks()
    task = next((t for t in tasks if t.id == task_id), None)
    if task:
        task.status = "completed"
        task.updated_at = datetime.now(timezone.utc).isoformat()
        if task.recurrence and task.due_date:
            next_due = calculate_next_due(task.due_date, task.recurrence)
            new_id = max(t.id for t in tasks) + 1
            new_task = models.Task.create(new_id, task.description, priority=task.priority, tags=task.tags, due_date=next_due, recurrence=task.recurrence)
            tasks.append(new_task)
        storage.save_tasks(tasks)
        return task
    return None

def delete_task(task_id):
    tasks = storage.load_tasks()
    initial_len = len(tasks)
    tasks = [t for t in tasks if t.id != task_id]
    if len(tasks) < initial_len:
        storage.save_tasks(tasks)
        return True
    return False

def check_due_tasks():
    tasks = storage.load_tasks()
    now = datetime.now(timezone.utc).isoformat()
    return [t for t in tasks if t.status == "pending" and t.due_date and t.due_date <= now]