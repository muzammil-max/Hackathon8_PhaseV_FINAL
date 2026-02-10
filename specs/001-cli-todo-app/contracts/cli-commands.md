# CLI Interface Contracts: CLI Todo App

**Feature**: `001-cli-todo-app`

This document defines the CLI command structure, arguments, and output formats.

## Global Options

- `--help`: Show usage information.
- `--no-banner`: Suppress the ASCII branding banner.

## Commands

### 1. Add Task
Creates a new task.

**Usage**: `todo add <description>`

- **Arguments**:
  - `description` (Required): The text of the task.
- **Output (Success)**:
  ```text
  [MyTodoApp Banner]
  Task added: [ID] Buy milk
  ```
- **Output (Error)**:
  ```text
  Error: Description cannot be empty.
  ```

### 2. List Tasks
Displays all tasks.

**Usage**: `todo list [options]`

- **Options**:
  - `--all`: Show all tasks (default might be pending only, but MVP spec implies "view all"). For MVP, `list` shows all.
- **Output**:
  ```text
  [MyTodoApp Banner]
  ID   Status     Description
  ----------------------------------------
  1    [ ]        Buy milk
  2    [x]        Walk dog
  ```

### 3. Update Task
Modifies an existing task.

**Usage**: `todo update <id> <new_description>`

- **Arguments**:
  - `id` (Required): The ID of the task to update.
  - `new_description` (Required): The new text.
- **Output (Success)**:
  ```text
  [MyTodoApp Banner]
  Task [ID] updated.
  ```
- **Output (Error)**:
  ```text
  Error: Task ID [ID] not found.
  ```

### 4. Delete Task
Permanently removes a task.

**Usage**: `todo delete <id>`

- **Arguments**:
  - `id` (Required): The ID of the task.
- **Output (Success)**:
  ```text
  [MyTodoApp Banner]
  Task [ID] deleted.
  ```

### 5. Mark Done
Completes a task.

**Usage**: `todo done <id>`

- **Arguments**:
  - `id` (Required): The ID of the task.
- **Output (Success)**:
  ```text
  [MyTodoApp Banner]
  Task [ID] marked as completed.
  ```
