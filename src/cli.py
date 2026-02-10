import argparse
import sys
import time
from src import services, utils

def print_banner():
    banner = r"""
    __  ___      ______          __      ___                
   /  |/  /_  __/_  __/___  ____/ /___  /   |  ____  ____ 
  / /|_/ / / / / / / / __ \/ __  / __ \/ /| | / __ \/ __ \
 / /  / / /_/ / / / / /_/ / /_/ / /_/ / ___ |/ /_/ / /_/ /
/_/  /_/\__, / /_/  \____/\__,_/___/_/  |_/ .___/ .___/ 
       /____/                              /_/   /_/      
    """
    print(banner)

def setup_parser():
    parser = argparse.ArgumentParser(description="MyTodoApp - Simple CLI Todo List")
    parser.add_argument("--no-banner", action="store_true", help="Suppress the ASCII banner")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")
    add_parser.add_argument("--priority", choices=["high", "medium", "low"], default="medium", help="Set task priority")
    add_parser.add_argument("--tags", help="Comma-separated tags")
    add_parser.add_argument("--due", help="Natural language due date")
    add_parser.add_argument("--recurrence", choices=["daily", "weekly", "monthly"], help="Repeat pattern")
    
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--filter", help="Filter tasks")
    list_parser.add_argument("--sort", choices=["priority", "due_date", "created_at"], help="Sort tasks")
    
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("--description", help="New description")
    update_parser.add_argument("--priority", choices=["high", "medium", "low"], help="New priority")
    update_parser.add_argument("--tags", help="New comma-separated tags")
    update_parser.add_argument("--due", help="New due date")
    update_parser.add_argument("--recurrence", choices=["daily", "weekly", "monthly"], help="New recurrence")
    
    done_parser = subparsers.add_parser("done", help="Mark task as done")
    done_parser.add_argument("id", type=int, help="Task ID")
    
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    search_parser = subparsers.add_parser("search", help="Search tasks")
    search_parser.add_argument("keyword", help="Search keyword")

    subparsers.add_parser("notify-service", help="Start background notification checker")
    
    return parser

def handle_add(args):
    if not args.description or not args.description.strip():
        print("Error: Description cannot be empty.")
        return
    tags = [t.strip() for t in args.tags.split(",")] if args.tags else []
    due_date = utils.parse_date(args.due) if args.due else None
    task = services.add_task(args.description, priority=args.priority, tags=tags, due_date=due_date, recurrence=args.recurrence)
    print(f"Task added: {task.id} {task.description}")

def handle_list(args):
    tasks = services.list_tasks(filter_by=args.filter, sort_by=args.sort)
    display_tasks(tasks)

def handle_search(args):
    tasks = services.search_tasks(args.keyword)
    display_tasks(tasks)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print(f"{ 'ID':<4} {'Status':<8} {'Prio':<8} {'Due':<18} {'Description'}")
    print("-" * 70)
    for t in tasks:
        status_mark = "[x]" if t.status == "completed" else "[ ]"
        prio = t.priority or "medium"
        due = utils.format_date(t.due_date) if t.due_date else "-"
        print(f"{t.id:<4} {status_mark:<8} {prio:<8} {due:<18} {t.description}")
        if t.tags:
            print(f"     Tags: {', '.join(t.tags)}")

def handle_update(args):
    tags = [t.strip() for t in args.tags.split(",")] if args.tags else None
    due_date = utils.parse_date(args.due) if args.due else None
    task = services.update_task(args.id, description=args.description, priority=args.priority, tags=tags, due_date=due_date, recurrence=args.recurrence)
    if task:
        print(f"Task {task.id} updated.")
    else:
        print(f"Error: Task ID {args.id} not found.")

def handle_done(args):
    task = services.mark_done(args.id)
    if task:
        print(f"Task {task.id} marked as completed.")
    else:
        print(f"Error: Task ID {args.id} not found.")

def handle_delete(args):
    success = services.delete_task(args.id)
    if success:
        print(f"Task {args.id} deleted.")
    else:
        print(f"Error: Task ID {args.id} not found.")

def handle_notify_service():
    print("Notification service started. Press Ctrl+C to stop.")
    notified_tasks = set()
    try:
        while True:
            due_tasks = services.check_due_tasks()
            for t in due_tasks:
                if t.id not in notified_tasks:
                    utils.send_notification("Task Due!", f"Task: {t.description}")
                    notified_tasks.add(t.id)
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nNotification service stopped.")

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = setup_parser()
    parsed_args = parser.parse_args(args)
    if not parsed_args.no_banner:
        print_banner()
    if not parsed_args.command:
        parser.print_help()
    elif parsed_args.command == "add":
        handle_add(parsed_args)
    elif parsed_args.command == "list":
        handle_list(parsed_args)
    elif parsed_args.command == "update":
        handle_update(parsed_args)
    elif parsed_args.command == "done":
        handle_done(parsed_args)
    elif parsed_args.command == "delete":
        handle_delete(parsed_args)
    elif parsed_args.command == "search":
        handle_search(parsed_args)
    elif parsed_args.command == "notify-service":
        handle_notify_service()
