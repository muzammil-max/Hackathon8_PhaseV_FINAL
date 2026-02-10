---
description: "Task list for Advanced Cloud-Native Deployment"
---

# Tasks: Advanced Cloud-Native Deployment

**Input**: Design documents from `specs/006-advanced-cloud-deployment/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: [US1], [US2], [US3], [US4]
- File paths are relative to repository root

## Phase 1: Infrastructure & Shared Setup (Prerequisites)

**Purpose**: Initialize Helm charts, Dapr components, and shared code.

- [x] T001 Initialize Helm chart structure in deploy/helm/todo-app
- [x] T002 Configure Dapr Redis State component in deploy/helm/todo-app/templates/statestore.yaml
- [x] T003 Configure Dapr Kafka PubSub component in deploy/helm/todo-app/templates/pubsub.yaml
- [x] T004 Create backend/shared/models.py with Pydantic models for Task and Event
- [x] T005 [P] Setup Dockerfiles for chat, task, scheduler, and notification services
- [ ] T006 Configure Skaffold or Makefile for local Minikube dev loop

## Phase 2: Foundational Services (Blocking US1)

**Purpose**: Core Task CRUD and Chat Gateway.

- [x] T007 Implement Task Service main.py with Dapr State CRUD ops in backend/services/task/
- [x] T008 Implement Chat Service main.py with Dapr Invoke logic in backend/services/chat/
- [x] T009 [P] Create Kubernetes deployment manifests for Task Service in deploy/helm/todo-app/templates/
- [x] T010 [P] Create Kubernetes deployment manifests for Chat Service in deploy/helm/todo-app/templates/
- [ ] T011 Verify synchronous "Create Task" flow on Minikube (Chat -> Task -> Redis)

## Phase 3: User Story 1 - Advanced Task Management (Priority: P1)

**Goal**: Recurring tasks, due dates, priorities, tags via Chat.
**Independent Test**: Create recurring/tagged tasks via Chat API and verify in Redis.

- [ ] T012 [US1] Update Task model in backend/shared/models.py to support recurrence, priority, tags
- [ ] T013 [US1] Update Task Service logic in backend/services/task/main.py to handle new fields
- [x] T014 [US1] Update Chat Service NLP logic in backend/services/chat/main.py to parse dates/tags
- [ ] T015 [US1] Add Dapr Pub/Sub event emission (TaskCreated) in backend/services/task/main.py
- [ ] T016 [US1] Create integration test for complex task creation in tests/integration/test_us1_advanced_tasks.py

## Phase 4: User Story 3 - Event-Driven Consistency (Priority: P2/P3)

**Goal**: Scheduler and Notification services reacting to events.
**Independent Test**: Emit event -> Scheduler logs/acts.

- [x] T017 [US3] Implement Notification Service to consume events in backend/services/notification/main.py
- [x] T018 [US3] Implement Scheduler Service to consume TaskCreated/Deleted in backend/services/scheduler/main.py
- [x] T019 [US3] Configure Dapr Binding (Cron) in backend/services/scheduler/ for recurrence checks
- [x] T020 [US3] Implement logic to spawn next recurring task instance in Scheduler Service
- [x] T021 [US3] Create K8s manifests for Scheduler and Notification services in deploy/helm/todo-app/templates/
- [ ] T022 [US3] Verify async event flow (Task -> Kafka -> Scheduler/Notification)

## Phase 5: User Story 2 - Task Discovery (Priority: P2)

**Goal**: Search and filter tasks.
**Independent Test**: Search query returns correct filtered subset.

- [x] T023 [US2] Implement Dapr Query API (or fallback scan) in backend/services/task/main.py
- [x] T024 [US2] Expose search endpoint in Task Service
- [x] T025 [US2] Add search command support in Chat Service
- [ ] T026 [US2] Create integration test for search/filter in tests/integration/test_us2_discovery.py

## Phase 6: User Story 4 - Cloud & Local Parity (Priority: P4)

**Goal**: Deploy same artifacts to Cloud K8s.

- [x] T027 [US4] Parameterize Helm chart values for Cloud vs Local (global.env) in deploy/helm/todo-app/values.yaml
- [ ] T028 [US4] Document Cloud deployment steps in GUIDE.md
- [ ] T029 [US4] Validate deployment on Cloud Cluster (Manual/CI)

## Phase 7: Polish & Cleanup

- [ ] T030 Refactor hardcoded configuration to use Helm values
- [ ] T031 Ensure all services have health probes (Liveness/Readiness)
- [ ] T032 Finalize README.md with Phase 5 instructions

## Dependencies

- **Phase 1 & 2** are blocking for all User Stories.
- **Phase 3 (US1)** is the functional core.
- **Phase 4 (US3)** can run in parallel with **Phase 5 (US2)** after Phase 3.
- **Phase 6 (US4)** requires all previous phases.

## Implementation Strategy

1. **Infrastructure First**: Get Minikube + Dapr + Kafka running.
2. **Vertical Slice (MVP)**: Chat -> Task -> Redis (Basic CRUD).
3. **Event Backbone**: Turn on Kafka, add Notification consumer.
4. **Complexity Layer**: Add Recurrence/Scheduler logic.
5. **Discovery Layer**: Add Search.
6. **Deployment**: Verify Cloud.
