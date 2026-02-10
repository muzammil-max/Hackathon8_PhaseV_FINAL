# CLI Interface Contracts: Advanced Features

**Feature**: `002-cli-todo-advanced`

## Updated Commands

### 1. Add Task (Enhanced)
**Usage**: `todo add <description> [options]`

- **Options**:
  - `--priority <level>`: Set priority (`high`, `medium`, `low`). Default: `medium`.
  - `--tags <tags>`: Comma-separated tags (e.g., "work,urgent").
  - `--due <date>`: Natural language due date (e.g., "tomorrow").
  - `--recurrence <pattern>`: Repeat pattern (`daily`, `weekly`, `monthly`).

**Example**:
```bash
todo add "Submit report" --priority high --tags work --due "friday" --recurrence weekly
```

### 2. List Tasks (Enhanced)
**Usage**: `todo list [options]`

- **Options**:
  - `--filter <expression>`: Filter tasks. Format `field=value`. Supported fields: `status`, `priority`, `tag`.
  - `--sort <field>`: Sort by field. Supported: `priority` (desc), `due_date` (asc), `created_at` (desc).

**Examples**:
```bash
todo list --filter status=pending --sort priority
todo list --filter tag=work
```

### 3. Update Task (Enhanced)
**Usage**: `todo update <id> [options]`

- **Options**:
  - Same as `add` (allows modifying priority, tags, due date, recurrence).

### 4. Search Tasks (New)
**Usage**: `todo search <keyword>`

- **Arguments**:
  - `keyword`: Text to match in description or tags (case-insensitive).

**Output**:
Table view of matching tasks.

### 5. Notification Service (New)
**Usage**: `todo notify-service`

- **Behavior**:
  - Runs indefinitely (foreground).
  - Checks for pending tasks with `due_date` <= now every 60 seconds.
  - Triggers OS notification for due tasks.
  - Marks task as "notified" (in runtime memory or separate state) to avoid spamming? -> *MVP*: Just notify once per minute if due? Better: track last notified timestamp or rely on user to complete/reschedule. *Decision*: Simple check, notify if due and not completed.

**Output**: Logs to stdout ("Checked at [Time]... Found X due tasks").
