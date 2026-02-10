# Research & Technical Decisions: Advanced CLI Todo Features

**Feature Branch**: `002-cli-todo-advanced`
**Date**: 2026-01-01

## Technology Stack Selection

### Date Parsing: `python-dateutil` (External) vs Standard Lib
**Decision**: Allow `python-dateutil`.
**Rationale**: 
- Standard `datetime` does not handle "next friday" or "tomorrow" easily.
- Implementing NLP for dates from scratch is error-prone.
- `dateutil` is a de-facto standard, lightweight, and stable.
- **Constraint Override**: Justified by "Advanced Features" requirement for natural language inputs (User Story 3).

### Notifications: OS-Native via `subprocess`
**Decision**: Use `subprocess` to invoke system tools.
- Windows: `msg` or PowerShell balloons.
- macOS: `osascript -e 'display notification ...'`
- Linux: `notify-send`
**Rationale**:
- Avoids heavy dependencies like `plyer` or GUI frameworks.
- Keeps Python environment minimal.
- Sufficient for simple "Task Due" alerts.

### Background Scheduling: Dedicated Command
**Decision**: Implement `todo notify-service` command.
**Rationale**:
- "Safe background scheduling" (User Story 4) is complex to auto-daemonize cross-platform without libs.
- User can run `todo notify-service &` (Linux/Mac) or `start python todo.py notify-service` (Windows).
- Uses standard `sched` or simple `time.sleep` loop.

## Constitution Alignment
- **Dependencies**: Added `python-dateutil` (justified).
- **Cross-Platform**: `subprocess` logic will detect OS (via `platform.system()`) to choose command.
- **Performance**: `dateutil` load time is negligible.

## Open Questions Resolved
- **Q**: How to handle recurrence? **A**: Check `recurrence` field on "Mark Done". If set, calculate `next_due` and create new task immediately.
