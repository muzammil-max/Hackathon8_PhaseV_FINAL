# Quickstart: Advanced Features

**Feature**: `002-cli-todo-advanced`

## Installation

Same as base. If `python-dateutil` is used:
```bash
pip install python-dateutil
```

## Advanced Usage

### Priorities & Tags
```bash
todo add "Fix critical bug" --priority high --tags work,bug
todo add "Buy coffee" --priority low --tags personal
```

### Due Dates & Recurring
```bash
todo add "Team Sync" --due "every friday" --recurrence weekly
todo add "Submit Taxes" --due "2026-04-15"
```

### Finding Tasks
```bash
# Filter by tag
todo list --filter tag=work

# Sort by urgency
todo list --sort priority

# Search text
todo search "bug"
```

### Notifications
Run the background listener in a separate terminal:
```bash
todo notify-service
```
