---
id: 005
title: generate phase 2 tasks
stage: tasks
date: 2026-02-05
surface: agent
model: gemini
feature: 003-web-expansion
branch: 003-web-expansion
user: user
command: /sp.tasks
labels: ["task-generation", "web-expansion"]
links:
  spec: specs/003-web-expansion/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/003-web-expansion/tasks.md
tests:
 - none
---

## Prompt

# Tasks: Phase 2 Web Expansion

**Input**: Design documents from `specs/003-web-expansion/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are OPTIONAL (not requested), so the tasks below focus on implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: [US1], [US2], [US3]
- **File paths**: Explicit paths relative to repo root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project directories (backend/, frontend/) per plan in `specs/003-web-expansion/plan.md`
- [ ] T002 Initialize Backend (FastAPI) environment and dependencies in `backend/`
- [ ] T003 [P] Initialize Frontend (Next.js) project in `frontend/`
- [ ] T004 [P] Configure Backend linting (Ruff/Black) in `backend/pyproject.toml`
- [ ] T005 [P] Configure Frontend linting (ESLint/Prettier) in `frontend/.eslintrc.json`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 Setup PostgreSQL connection and SQLModel engine in `backend/src/database.py`
- [ ] T007 Define shared configurations (env vars) in `backend/src/config.py` and `frontend/.env.local`
- [ ] T008 [P] Implement global error handling middleware in `backend/src/main.py`
- [ ] T009 [P] Setup centralized API client with base URL in `frontend/src/lib/api.ts`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Secure Account Access (Priority: P1) 🎯 MVP

**Goal**: Users can sign up and sign in to receive a JWT.

**Independent Test**: Register a new user via API/UI and receive a token; verify token allows access.

### Implementation for User Story 1

- [ ] T010 [US1] Create User SQLModel entity in `backend/src/models.py`
- [ ] T011 [US1] Implement password hashing and JWT utility functions in `backend/src/auth.py`
- [ ] T012 [US1] Create Auth API routes (login, signup) in `backend/src/routes/auth.py`
- [ ] T013 [US1] Integrate Auth routes into main app in `backend/src/main.py`
- [ ] T014 [US1] Create Login page with form handling in `frontend/src/app/login/page.tsx`
- [ ] T015 [US1] Create Signup page with form handling in `frontend/src/app/signup/page.tsx`
- [ ] T016 [US1] Integrate "Better Auth" (or JWT handling) in `frontend/src/lib/auth.ts`
- [ ] T017 [US1] Connect Login/Signup forms to API in `frontend/src/app/login/page.tsx` and `frontend/src/app/signup/page.tsx`

**Checkpoint**: User Story 1 functional - Users can register and login

---

## Phase 4: User Story 2 - Private Task Management (Priority: P1)

**Goal**: Authenticated users can CRUD their own tasks in isolation.

**Independent Test**: User A creates tasks; User B cannot see them.

### Implementation for User Story 2

- [ ] T018 [US2] Create Task SQLModel entity with foreign key to User in `backend/src/models.py`
- [ ] T019 [US2] Implement `get_current_user` dependency in `backend/src/auth.py`
- [ ] T020 [US2] Create Task CRUD routes (GET, POST, PUT, DELETE) in `backend/src/routes/tasks.py`
- [ ] T021 [US2] Enforce owner filtering in all Task routes in `backend/src/routes/tasks.py`
- [ ] T022 [US2] Integrate Task routes into main app in `backend/src/main.py`
- [ ] T023 [US2] Create Task API service functions in `frontend/src/services/tasks.ts`
- [ ] T024 [US2] Create Task List component in `frontend/src/components/TaskList.tsx`
- [ ] T025 [US2] Create Task Item component with actions (edit, delete) in `frontend/src/components/TaskItem.tsx`
- [ ] T026 [US2] Create Task Form component (create/edit) in `frontend/src/components/TaskForm.tsx`
- [ ] T027 [US2] Assemble Dashboard page in `frontend/src/app/page.tsx`

**Checkpoint**: User Stories 1 AND 2 functional - Full private task management

---

## Phase 5: User Story 3 - Unified Web Interface (Priority: P2)

**Goal**: Responsive UI across devices.

**Independent Test**: UI layout adapts to mobile/desktop; loading states visible.

### Implementation for User Story 3

- [ ] T028 [US3] Implement responsive layout wrapper (Navbar, Container) in `frontend/src/app/layout.tsx`
- [ ] T029 [US3] Add loading skeletons/spinners for async states in `frontend/src/components/ui/Loading.tsx`
- [ ] T030 [US3] Style Task List for mobile responsiveness (stack vs table) in `frontend/src/components/TaskList.tsx`
- [ ] T031 [US3] Implement toast notifications for success/error feedback in `frontend/src/components/ui/Toast.tsx`

**Checkpoint**: All user stories functional and polished

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T032 Update README.md with setup instructions from `specs/003-web-expansion/quickstart.md`
- [ ] T033 Verify API contract compliance (run manual checks against `specs/003-web-expansion/contracts/api.md`)
- [ ] T034 [P] Cleanup unused code and temporary files
- [ ] T035 [P] Security audit (verify JWT expiration handling, strict user isolation)

## Response snapshot

Generated actionable tasks for Phase 2: Web Expansion.
- **Total Tasks**: 35
- **Phases**: Setup (5), Foundational (4), US1 (8), US2 (10), US3 (4), Polish (4).
- **Format**: All tasks follow strict `[ID] [P?] [Story] Description` format.
- **Scope**: Covers Backend (FastAPI), Frontend (Next.js), DB (Postgres), Auth, and UI.

## Outcome

- ✅ Impact: Actionable work plan created.
- 🧪 Tests: N/A
- 📁 Files: specs/003-web-expansion/tasks.md
- 🔁 Next prompts: /sp.implement
- 🧠 Reflection: Clear separation between Frontend and Backend tasks.
- 🚧 Failure modes: none
- 📝 Grader results: PASS
- 🔄 Prompt variant: default
- 🧪 Next experiment: none
