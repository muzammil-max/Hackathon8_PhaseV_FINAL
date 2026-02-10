# Implementation Plan: Advanced Cloud-Native Deployment

**Branch**: `006-advanced-cloud-deployment` | **Date**: 2026-02-09 | **Spec**: [specs/006-advanced-cloud-deployment/spec.md](./spec.md)

## Summary
Transform the Todo Chatbot into an event-driven, cloud-native system using **Dapr** and **Kafka** on **Kubernetes**. Features include recurring tasks, complex scheduling, and full local/cloud parity.

## Technical Context
**Language**: Python 3.10+ (FastAPI)
**Framework**: Dapr (Python SDK)
**Orchestration**: Kubernetes (Minikube / Managed)
**Event Bus**: Kafka (via Dapr Pub/Sub)
**State Store**: Redis (via Dapr State)
**Packaging**: Helm v3
**Constraints**: No direct DB/Kafka access in app code; "Dapr API only".

## Constitution Check
*   **Event-Driven**: ✅ Architecture uses Kafka + Dapr Pub/Sub.
*   **Cloud Portability**: ✅ Dapr abstracts infrastructure.
*   **Kubernetes Contract**: ✅ All services containerized and Helmed.
*   **Local-First**: ✅ Minikube deployment validation included.

## Project Structure

### Documentation
```text
specs/006-advanced-cloud-deployment/
├── plan.md              # This file
├── research.md          # Technology decisions (Dapr Query, Service Split)
├── data-model.md        # Entities (Task, Event)
├── quickstart.md        # Minikube guide
├── contracts/           # API & Event schemas
└── tasks.md             # Implementation tasks
```

### Source Code (Microservices)
```text
backend/
├── services/
│   ├── chat/           # API Gateway / Chatbot logic
│   ├── task/           # Core Domain (CRUD, State)
│   ├── scheduler/      # Cron bindings, Reminders
│   └── notification/   # Event consumer (Logger/Email)
├── shared/             # Shared Pydantic models (Task, Event)
deploy/
├── helm/
│   └── todo-app/       # Unified Helm Chart
│       ├── templates/
│       ├── charts/     # Subcharts (Kafka, Redis dependencies)
│       └── values.yaml
```

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Microservices | Separation of concerns (Task vs Scheduler) | Monolith doesn't scale for independent event processing and limits "Cloud Native" learning scope. |
| Dapr | Cloud portability mandate | Direct SDKs create vendor lock-in and violate Phase 5 constitution. |
| Kafka | Event backbone requirement | RabbitMQ/HTTP is simpler but less robust for "Event Sourcing" style requirements. |

## Implementation Strategy (Phased)

### Phase 1: Infrastructure & Shared
- Scaffold `deploy/helm` with Dapr components (Kafka, Redis).
- Create `backend/shared` for Pydantic models (`Task`, `Event`).

### Phase 2: Core Services (Task & Chat)
- Implement **Task Service** (Dapr State CRUD).
- Implement **Chat Service** (Dapr Invoke -> Task).
- Validate synchronous "Create Task" flow.

### Phase 3: Event Backbone (Kafka)
- Enable Dapr Pub/Sub in Task Service (emit events).
- Implement **Notification Service** (consume events).
- Validate async flow (Task Created -> Logged).

### Phase 4: Advanced Logic (Scheduler)
- Implement **Scheduler Service**.
- Add Dapr Bindings for Cron/Timer.
- Implement "Recurrence" logic (Task Completed -> Schedule Next).
- Implement "Reminders" (Due Date -> Event).

### Phase 5: Search & Polish
- Implement Dapr Query API (or fallback) in Task Service for Search/Filter.
- Finalize Minikube testing.
- Verify Cloud Parity.
