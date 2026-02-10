# Implementation Plan: Advanced CLI Todo Features

**Branch**: `002-cli-todo-advanced` | **Date**: 2026-01-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `spec.md`

## Summary

This update transforms the simple Todo list into a robust personal task manager. It adds metadata (priorities, tags), discovery tools (search, filter, sort), and time management features (due dates, recurrence, notifications). The architecture remains file-based (JSON) but evolves the Data Model and Service Layer to handle complex queries and background checking.

## Technical Context

**Language/Version**: Python 3.10+
**Primary Dependencies**: 
- Standard Lib: `argparse`, `json`, `datetime`, `subprocess`, `sched`, `time`.
- External: `python-dateutil` (for natural language date parsing).
**Storage**: `tasks.json` (Version 1.1 schema update).
**Testing**: `pytest` or `unittest`.
**Target Platform**: Windows, macOS, Linux.
**Constraints**: 
- Notification "background" process is a simple foreground loop command (`notify-service`).
- Date parsing relies on `dateutil` to minimize custom NLP code.

## Constitution Check

- **Minimal Dependencies**: ⚠️ Added `python-dateutil`. Justified by requirement for "natural language date parsing" (User Story 3) which is error-prone to implement from scratch.
- **Clear Structure**: ✅ New commands follow existing patterns.
- **Reliability**: ✅ Storage updates are backward compatible.
- **Modularity**: ✅ Date parsing and notification logic isolated in `src/utils.py` (or similar).

## Project Structure

### Documentation

```text
specs/002-cli-todo-advanced/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
└── contracts/
    └── cli-commands.md
```

### Source Code

```text
src/
├── todo.py          # Entry point (unchanged)
├── cli.py           # Updated with new args/commands
├── storage.py       # Unchanged (handles arbitrary dicts mostly)
├── models.py        # Updated Task fields
├── services.py      # Updated CRUD + Search/Filter/Sort logic
└── utils.py         # NEW: Date parsing & Notification helpers
```

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| External Lib (`dateutil`) | Natural language dates | Regex is too brittle for "next friday" etc. |
| `notify-service` command | User Story 4 | OS Cron/Service is too complex to install portably. |