---
description: "Task list for Advanced CLI Todo Features implementation"
---

# Tasks: Advanced CLI Todo Features

**Input**: Design documents from `/specs/002-cli-todo-advanced/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/cli-commands.md

**Tests**: Tests are OPTIONAL. Included based on `plan.md` strategy (unittest/pytest).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare project for new dependencies and structure updates

- [x] T001 Update `requirements-dev.txt` (or just install) `python-dateutil` for date parsing
- [x] T002 [P] Create `src/utils.py` module stub for helper functions
- [x] T003 [P] Update `src/models.py` Task dataclass to include new optional fields (priority, tags, due_date, recurrence)
- [x] T004 Create migration script or logic in `src/storage.py` to handle v1.1 schema (optional fields default to None)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core logic updates required for multiple stories

- [x] T005 [P] Implement `parse_date` function in `src/utils.py` using `dateutil`
- [x] T006 [P] Implement `format_date` function in `src/utils.py` for consistent display
- [x] T007 Update `to_dict` and `from_dict` in `src/models.py` to handle new fields
- [x] T008 Add unit tests for updated Task model in `tests/unit/test_models.py` (verify optional fields)
- [x] T009 Add unit tests for date parsing utilities in `tests/unit/test_utils.py`

**Checkpoint**: Data model updated and utilities tested.

---

## Phase 3: User Story 1 & 2 - Organization & Discovery (Priority: P1/P2)

**Goal**: Enable Priorities, Tags, Search, Filter, and Sort.

**Independent Test**: Add task with metadata -> Verify storage. Run list with filters -> Verify output.

### Tests
- [x] T010 [P] [US1] Add integration test for adding task with priority/tags in `tests/integration/test_advanced_features.py`
- [x] T011 [P] [US2] Add integration test for filtering and sorting in `tests/integration/test_advanced_features.py`

### Implementation
- [x] T012 [US1] Update `add_task` in `src/services.py` to accept priority, tags, due_date, recurrence
- [x] T013 [US1] Update `add` parser in `src/cli.py` to support new arguments (`--priority`, `--tags`, etc.)
- [x] T014 [US2] Implement `filter_tasks` helper in `src/services.py` (handling status, priority, tag)
- [x] T015 [US2] Implement `sort_tasks` helper in `src/services.py` (handling priority, due_date, created_at)
- [x] T016 [US2] Update `list_tasks` in `src/services.py` to accept filter/sort criteria
- [x] T017 [US2] Update `list` parser in `src/cli.py` to support `--filter` and `--sort`
- [x] T018 [P] [US2] Implement `search_tasks` in `src/services.py` (keyword match)
- [x] T019 [P] [US2] Register `search` command in `src/cli.py`

**Checkpoint**: Tasks can be organized and found efficiently.

---

## Phase 4: User Story 3 - Time Management (Priority: P3)

**Goal**: Natural language due dates and recurrence logic.

**Independent Test**: Add task with "tomorrow" -> Check saved date. Mark recurring task done -> Check next instance created.

### Tests
- [x] T020 [P] [US3] Add unit tests for recurrence calculation in `tests/unit/test_services.py`

### Implementation
- [x] T021 [US3] Update `add` command in `src/cli.py` to use `utils.parse_date` for `--due` input
- [x] T022 [US3] Implement `calculate_next_due` logic in `src/utils.py` or `src/services.py`
- [x] T023 [US3] Update `mark_done` in `src/services.py` to handle recurrence (create next task if recurring)

**Checkpoint**: Recurring tasks regenerate upon completion.

---

## Phase 5: User Story 4 - Notifications (Priority: P4)

**Goal**: Background service to alert on due tasks.

**Independent Test**: Run `notify-service` -> Verify output/notification for a due task.

### Implementation
- [x] T024 [US4] Implement `send_notification` in `src/utils.py` using `subprocess` (platform detection)
- [x] T025 [US4] Implement `check_due_tasks` logic in `src/services.py` (find pending tasks with due_date <= now)
- [x] T026 [US4] Implement `notify-service` command in `src/cli.py` (loop and sleep)

---

## Phase 6: Polish & Cross-Cutting Concerns

- [x] T027 Update `README.md` with new features usage guide
- [x] T028 [P] Enhance `list` output format in `src/cli.py` to show columns for Priority/Due Date if present

---

## Dependencies & Execution Order

### Phase Dependencies
1. **Setup & Foundational**: Must happen first to support data schema changes.
2. **US1 & US2**: Can happen together as they both touch `add` and `list` heavily.
3. **US3**: Depends on `utils.py` date parsing (Phase 2).
4. **US4**: Depends on US3 (due dates must exist to be notified).

### Implementation Strategy
1. **Schema Update**: Get the models right first.
2. **Input/Output**: Update `add` and `list` to handle the new data.
3. **Logic**: Add recurrence and notification loops last.
