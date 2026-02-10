# Research & Technical Decisions: CLI Todo App

**Feature Branch**: `001-cli-todo-app`
**Date**: 2026-01-01

## Technology Stack Selection

### Language: Python 3.10+
**Decision**: Use Python.
**Rationale**: 
- Ubiquitous, cross-platform, and rapid development.
- Standard library (`argparse`) is sufficient for the MVP requirements.
- Startup time is within acceptable limits (<100ms) for this scope.
**Alternatives**: 
- **Go/Rust**: Better performance/single binary, but slower iteration for a simple todo app if not specified.
- **Node.js**: Similar to Python but dependency management (node_modules) can be heavier.

### CLI Library: `argparse` (Standard Library)
**Decision**: Use Python's built-in `argparse`.
**Rationale**: 
- Strictly adheres to Constitution Principle "Minimize external dependencies".
- No need for `pip install` for end users if they have Python.
- Powerful enough for subcommands (`add`, `list`, etc.).
**Alternatives**:
- **Typer/Click**: Better DX, but introduces external dependencies. Rejected to keep it lightweight.

### Storage: JSON
**Decision**: Local JSON file (`~/.mytodo/tasks.json`).
**Rationale**:
- Human-readable (debuggable).
- Built-in `json` library support.
- Sufficient performance for typical personal todo lists (<1000 items).
**Alternatives**:
- **SQLite**: Overkill for MVP, requires SQL knowledge. Good upgrade path later.
- **CSV**: Harder to handle nested data or extensions later.

## Constitution Alignment
- **Minimal Dependencies**: Validated (Standard lib only).
- **Cross-Platform**: Python handles path differences (`os.path`).
- **Reliability**: will implement atomic writes (write temp -> rename) to prevent corruption.

## Open Questions Resolved
- **Q**: Platform support? **A**: Python `os` and `pathlib` abstraction ensures Win/Mac/Linux compat.
