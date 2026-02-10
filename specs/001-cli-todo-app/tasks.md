---
description: "Task list for CLI Todo App implementation"
---

# Tasks: CLI Todo App

**Input**: Design documents from `/specs/001-cli-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/cli-commands.md

**Tests**: Tests are OPTIONAL. Included based on `plan.md` strategy (pytest).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure (src/, tests/, tests/unit/, tests/integration/) per plan
- [x] T002 Initialize Python environment (create requirements-dev.txt for pytest)
- [x] T003 [P] Create initial empty `src/todo.py` entry point
- [x] T004 [P] Create `src/storage.py` module stub
- [x] T005 [P] Create `src/models.py` module stub
- [x] T006 [P] Create `src/cli.py` module stub

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Implement Task entity class in `src/models.py` with `to_dict` and `from_dict` methods
- [x] T008 [P] Implement `save_tasks` in `src/storage.py` with atomic write (write to temp then rename)
- [x] T009 [P] Implement `load_tasks` in `src/storage.py` handling file not found (return empty list)
- [x] T010 Create unit tests for Task model in `tests/unit/test_models.py`
- [x] T011 Create unit tests for Storage (save/load) in `tests/unit/test_storage.py`

**Checkpoint**: Models and Storage are implemented and tested.

---

## Phase 3: User Story 1 - Branding & Help (Priority: P1)

**Goal**: Display "MyTodoApp" banner and help usage on startup.

**Independent Test**: Run `python src/todo.py --help` to see banner. Run with `--no-banner` to verify suppression.

### Tests for User Story 1

- [x] T012 [P] [US1] Create integration test for banner display in `tests/integration/test_cli.py`

### Implementation for User Story 1

- [x] T013 [US1] Implement `print_banner` function in `src/cli.py` (ASCII art)
- [x] T014 [US1] Setup `argparse` in `src/cli.py` with global `--no-banner` argument
- [x] T015 [US1] Connect `src/todo.py` to `src/cli.py` main entry point
- [x] T016 [US1] Implement logic to conditionally show banner based on flag in `src/cli.py`

**Checkpoint**: Application runs, shows banner, and handles help command.

---

## Phase 4: User Story 2 - Task Management MVP (Priority: P1)

**Goal**: Enable Add, List, Update, Done, Delete commands.

**Independent Test**: Complete full CRUD cycle via CLI.

### Tests for User Story 2

- [x] T017 [P] [US2] Add unit tests for `add_task`, `delete_task` logic in `src/models.py` (or service layer if added)
- [x] T018 [P] [US2] Add integration tests for CLI commands (`add`, `list`, `done`) in `tests/integration/test_cli.py`

### Implementation for User Story 2

- [x] T019 [US2] Implement `add` command logic in `src/cli.py` calling `storage.save_tasks`
- [x] T020 [US2] Implement `list` command logic in `src/cli.py` formatting output as table
- [x] T021 [P] [US2] Implement `update` command logic in `src/cli.py`
- [x] T022 [P] [US2] Implement `done` command logic in `src/cli.py`
- [x] T023 [P] [US2] Implement `delete` command logic in `src/cli.py`
- [x] T024 [US2] Wire up all subcommands to `argparse` parsers in `src/cli.py`

**Checkpoint**: Fully functional Todo CLI.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements, edge cases, and documentation.

- [x] T025 [P] Implement error handling for invalid IDs in `src/cli.py`
- [x] T026 [P] Ensure startup time is <100ms (verify with `time` command)
- [x] T027 Update `README.md` or `quickstart.md` with final usage examples

---

## Dependencies & Execution Order

### Phase Dependencies

1. **Setup (Phase 1)**: Independent.
2. **Foundational (Phase 2)**: Depends on Phase 1. Blocks all stories.
3. **User Story 1 (P1)**: Depends on Phase 2.
4. **User Story 2 (P1)**: Depends on Phase 2. Can run parallel to US1 (mostly), but shares `cli.py` entry point logic. Best to merge US1 `main` skeleton first.

### Parallel Opportunities

- **Phase 1**: All tasks [P] can be parallel.
- **Phase 2**: Storage and Model implementation can be parallel.
- **Phase 3/4**: Once `cli.py` structure is set (T014), individual commands (Add, List, etc.) in US2 can be implemented in parallel.

## Implementation Strategy

### MVP Delivery

1. **Skeleton**: Setup + Foundational + US1 (Banner/Help)
2. **Core**: US2 (Add/List/Done) -> **Shippable MVP**
3. **Polish**: Error handling and speed checks.