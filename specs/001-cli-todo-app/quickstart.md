# Quickstart: CLI Todo App

**Feature**: `001-cli-todo-app`

## Prerequisites

- Python 3.10 or higher
- Terminal (PowerShell, Bash, Zsh, CMD)

## Installation

1. Clone the repository.
2. No external dependencies required (Standard Library only).

## Usage

Run the application via the entry point script:

```bash
# Windows
python src/todo.py list

# macOS/Linux
python3 src/todo.py list
```

### Examples

```bash
# Add a task
python src/todo.py add "Buy milk"

# List tasks
python src/todo.py list

# Mark as done
python src/todo.py done 1
```

## Testing

Run unit tests using pytest (requires dev installation):

```bash
pip install pytest
pytest tests/
```

## Data Location

Tasks are stored in `tasks.json` in the current directory (for MVP/Development).
In production, this might move to `~/.mytodo/tasks.json`.
