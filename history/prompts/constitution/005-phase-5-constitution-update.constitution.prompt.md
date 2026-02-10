---
id: 005
title: Phase 5 Constitution Update
stage: constitution
date: 2026-02-09
surface: agent
model: gemini-2.0-flash
feature: none
branch: main
user: Muzammil
command: /sp.constitution
labels: ["constitution", "phase-5", "cloud-native", "dapr", "kafka"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - null
---

## Prompt

/sp.constitution — Phase 5
## MyTodoApp · Advanced Cloud Deployment

## Role
You are a **Cloud-Native Platform Engineer** deploying an **event-driven, distributed Todo AI system** using Kubernetes, Kafka, and Dapr, with Gemini-style reasoning and spec-driven execution.

---

## Objective
Transform the Todo AI Chatbot into a **production-grade, cloud-native system** by adding advanced features, adopting **event-driven architecture**, and deploying to **managed Kubernetes platforms** after local validation.

---

## Core Principles
- Spec-driven development only
- No manual coding outside agent execution
- Event-driven, loosely coupled services
- Cloud portability via Dapr abstractions
- Kubernetes as the runtime contract

---

## Functional Mandate

### Advanced Application Features
- Recurring tasks
- Due dates and reminders
- Priorities and tags
- Search, filter, and sort

### Event-Driven Architecture
- Kafka used for async communication
- All task actions emit events
- Consumers handle reminders, recurrence, audit, and sync

---

## Platform Mandate

### Local First
- Deploy full system on Minikube
- Validate Kafka + Dapr integration locally
- Ensure feature parity with cloud deployment

### Cloud Deployment
- Deploy to AKS, GKE, or Oracle OKE
- Use managed or self-hosted Kafka
- Reuse Helm charts from Phase IV
- Production-grade Kubernetes configuration

---

## Dapr Mandate
Dapr must be used for:
- Pub/Sub (Kafka abstraction)
- State management
- Service invocation
- Scheduled jobs (reminders, recurrence)
- Secrets management

Application code must not depend directly on Kafka or infrastructure SDKs.

---

## Infrastructure Law
- All services run in Kubernetes
- One service per responsibility
- Communication via events, not tight coupling
- No hardcoded credentials
- Configuration via Helm and Dapr components

---

## CI/CD Mandate
- GitHub Actions for build and deploy
- Automated container builds
- Automated Kubernetes deployment

---

## Non-Negotiables
- No breaking changes to earlier phases
- No environment-specific logic in code
- No synchronous blocking for async workflows
- No cloud lock-in at code level

---

## Success Criteria
Phase V is complete when:
- Advanced features work end-to-end
- Kafka-backed workflows function correctly
- Dapr sidecars handle infrastructure concerns
- System runs on Minikube and cloud Kubernetes
- Deployment is reproducible and observable

## Response snapshot

Updated constitution to v5.0.0 reflecting Phase 5 requirements: Cloud-Native Platform Engineer role, Event-Driven Architecture (Kafka), Dapr integration, and Kubernetes deployment mandates.

## Outcome

- ✅ Impact: Constitution updated to v5.0.0.
- 🧪 Tests: N/A
- 📁 Files: Updated constitution.md
- 🔁 Next prompts: /sp.specify
- 🧠 Reflection: Major version bump required due to architectural shift.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): N/A
