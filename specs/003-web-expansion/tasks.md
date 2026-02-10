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

- [x] T001 Create project directories (backend/, frontend/) per plan in `specs/003-web-expansion/plan.md`
- [x] T002 Initialize Backend (FastAPI) environment and dependencies in `backend/`
- [x] T003 [P] Initialize Frontend (Next.js) project in `frontend/`
- [x] T004 [P] Configure Backend linting (Ruff/Black) in `backend/pyproject.toml`
- [x] T005 [P] Configure Frontend linting (ESLint/Prettier) in `frontend/.eslintrc.json`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Setup PostgreSQL connection and SQLModel engine in `backend/src/database.py`
- [x] T007 Define shared configurations (env vars) in `backend/src/config.py` and `frontend/.env.local`
- [x] T008 [P] Implement global error handling middleware in `backend/src/main.py`
- [x] T009 [P] Setup centralized API client with base URL in `frontend/src/lib/api.ts`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Secure Account Access (Priority: P1) 🎯 MVP

**Goal**: Users can sign up and sign in to receive a JWT.

**Independent Test**: Register a new user via API/UI and receive a token; verify token allows access.

### Implementation for User Story 1

- [x] T010 [US1] Create User SQLModel entity in `backend/src/models.py`
- [x] T011 [US1] Implement password hashing and JWT utility functions in `backend/src/auth.py`
- [x] T012 [US1] Create Auth API routes (login, signup) in `backend/src/routes/auth.py`
- [x] T013 [US1] Integrate Auth routes into main app in `backend/src/main.py`
- [x] T014 [US1] Create Login page with form handling in `frontend/src/app/login/page.tsx`
- [x] T015 [US1] Create Signup page with form handling in `frontend/src/app/signup/page.tsx`
- [x] T016 [US1] Integrate "Better Auth" (or JWT handling) in `frontend/src/lib/auth.ts`
- [x] T017 [US1] Connect Login/Signup forms to API in `frontend/src/app/login/page.tsx` and `frontend/src/app/signup/page.tsx`

**Checkpoint**: User Story 1 functional - Users can register and login

---

## Phase 4: User Story 2 - Private Task Management (Priority: P1)

**Goal**: Authenticated users can CRUD their own tasks in isolation.

**Independent Test**: User A creates tasks; User B cannot see them.

### Implementation for User Story 2

- [x] T018 [US2] Create Task SQLModel entity with foreign key to User in `backend/src/models.py`
- [x] T019 [US2] Implement `get_current_user` dependency in `backend/src/auth.py`
- [x] T020 [US2] Create Task CRUD routes (GET, POST, PUT, DELETE) in `backend/src/routes/tasks.py`
- [x] T021 [US2] Enforce owner filtering in all Task routes in `backend/src/routes/tasks.py`
- [x] T022 [US2] Integrate Task routes into main app in `backend/src/main.py`
- [x] T023 [US2] Create Task API service functions in `frontend/src/services/tasks.ts`
- [x] T024 [US2] Create Task List component in `frontend/src/components/TaskList.tsx`
- [x] T025 [US2] Create Task Item component with actions (edit, delete) in `frontend/src/components/TaskItem.tsx`
- [x] T026 [US2] Create Task Form component (create/edit) in `frontend/src/components/TaskForm.tsx`
- [x] T027 [US2] Assemble Dashboard page in `frontend/src/app/page.tsx`

**Checkpoint**: User Stories 1 AND 2 functional - Full private task management

---

## Phase 5: User Story 3 - Unified Web Interface (Priority: P2)

**Goal**: Responsive UI across devices.

**Independent Test**: UI layout adapts to mobile/desktop; loading states visible.

### Implementation for User Story 3

- [x] T028 [US3] Implement responsive layout wrapper (Navbar, Container) in `frontend/src/app/layout.tsx`
- [x] T029 [US3] Add loading skeletons/spinners for async states in `frontend/src/components/ui/Loading.tsx`
- [x] T030 [US3] Style Task List for mobile responsiveness (stack vs table) in `frontend/src/components/TaskList.tsx`
- [x] T031 [US3] Implement toast notifications for success/error feedback in `frontend/src/components/ui/Toast.tsx`

**Checkpoint**: All user stories functional and polished

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T032 Update README.md with setup instructions from `specs/003-web-expansion/quickstart.md`
- [x] T033 Verify API contract compliance (run manual checks against `specs/003-web-expansion/contracts/api.md`)
- [x] T034 [P] Cleanup unused code and temporary files
- [x] T035 [P] Security audit (verify JWT expiration handling, strict user isolation)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Phase 1. BLOCKS all user stories.
- **User Stories (Phase 3+)**: All depend on Phase 2.
- **Polish (Phase 6)**: Depends on all stories.

### User Story Dependencies

- **US1 (Auth)**: Independent.
- **US2 (Tasks)**: Depends on US1 (needs User entity and Auth dependency).
- **US3 (UI)**: Depends on US2 (needs Task components to style).

### Parallel Opportunities

- Frontend and Backend setup (Phase 1) can run in parallel.
- Frontend components and Backend routes within US2 can be developed in parallel (once API contract is agreed).
- Polish tasks can run in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 & 2)

1. Complete Setup & Foundation.
2. Implement US1 (Auth) to establish user context.
3. Implement US2 (Tasks) to deliver core value.
4. **STOP and VALIDATE**: Verify strict user isolation.

### Incremental Delivery

1. Foundation + Auth (US1) -> "Login enabled"
2. Tasks (US2) -> "Functional Todo App"
3. UI Polish (US3) -> "Mobile-ready App"
