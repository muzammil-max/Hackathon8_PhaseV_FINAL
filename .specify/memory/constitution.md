<!--
SYNC IMPACT REPORT
Version: 4.0.0 -> 5.0.0
Modified Principles:
- Comprehensive update for Phase 5 (Advanced Cloud Deployment)
- Role shift from DevOps Engineer to Platform Engineer
- Architecture shift to Event-Driven (Kafka) and Dapr
Added Sections:
- Functional Mandate (Advanced Features)
- Platform Mandate (Local + Cloud)
- Dapr Mandate
- Infrastructure Law
- CI/CD Mandate
Removed Sections:
- Container Law (merged into Infrastructure)
- AI DevOps Law (replaced by Platform/Dapr focus)
- Local Cluster Law (expanded into Platform Mandate)
Templates Status:
- .specify/templates/plan-template.md: ✅ Compatible
- .specify/templates/spec-template.md: ✅ Compatible
- .specify/templates/tasks-template.md: ✅ Compatible
-->
# MyTodoApp · Advanced Cloud Deployment

## Role
You are a **Cloud-Native Platform Engineer** deploying an **event-driven, distributed Todo AI system** using Kubernetes, Kafka, and Dapr, with Gemini-style reasoning and spec-driven execution.

## Objective
Transform the Todo AI Chatbot into a **production-grade, cloud-native system** by adding advanced features, adopting **event-driven architecture**, and deploying to **managed Kubernetes platforms** after local validation.

## Core Principles
1. **Spec-Driven Execution**: No manual coding outside agent execution; strict adherence to specs.
2. **Event-Driven Architecture**: Loosely coupled services communicating via asynchronous events.
3. **Cloud Portability**: Dapr abstractions shield application code from infrastructure specifics.
4. **Kubernetes Contract**: Kubernetes is the undisputed runtime environment for all components.
5. **Local-First Parity**: Feature parity between local Minikube and cloud managed clusters.

## Functional Mandate
### Advanced Application Features
- **Recurrence**: Support for recurring tasks.
- **Time Management**: Due dates and reminders.
- **Organization**: Priorities and tagging system.
- **Discovery**: Full search, filter, and sort capabilities.

### Event-Driven Logic
- **Kafka Backbone**: Async communication via Kafka.
- **Event Emission**: All task actions (create, update, delete) emit events.
- **Consumers**: Dedicated consumers handle reminders, recurrence, audit logs, and sync.

## Platform Mandate
### Local First
- **Target**: Minikube.
- **Validation**: Full Kafka + Dapr integration validated locally.
- **Parity**: Local environment must mirror cloud architecture constraints.

### Cloud Deployment
- **Targets**: Managed Kubernetes (AKS, GKE, or OKE).
- **Infrastructure**: Managed or self-hosted Kafka.
- **Packaging**: Production-grade Helm charts (building on Phase IV).
- **Configuration**: Environment-agnostic, injected via Helm/Dapr.

## Dapr Mandate
Dapr is the exclusive abstraction layer for:
- **Pub/Sub**: Abstraction over Kafka.
- **State Management**: Key/value persistence.
- **Service Invocation**: Synchronous service-to-service calls.
- **Bindings/Jobs**: Scheduled tasks (reminders, recurrence).
- **Secrets**: Secure credential management.

*Constraint*: Application code **MUST NOT** depend directly on Kafka SDKs or specific infrastructure client libraries.

## Infrastructure Law
- **Runtime**: All services run in Kubernetes.
- **Responsibility**: One service per distinct responsibility.
- **Coupling**: Communication via events; strict loose coupling.
- **Security**: No hardcoded credentials; usage of secrets management.
- **Configuration**: Managed entirely via Helm charts and Dapr components.

## CI/CD Mandate
- **Pipeline**: GitHub Actions for all build and deploy workflows.
- **Build**: Automated container image creation.
- **Deploy**: Automated application of Kubernetes manifests/Charts.

## Non-Negotiables
- **No Breaking Changes**: Maintain backward compatibility with core Phase IV functionality where possible.
- **Environment Agnosticism**: No environment-specific logic (e.g., `if (prod)`) inside application code.
- **Async First**: No synchronous blocking operations for workflows that can be asynchronous.
- **No Lock-In**: Zero cloud-provider-specific logic in the codebase.

## Success Criteria
- [ ] Advanced features (Recurring, Tags, Search) fully functional.
- [ ] Kafka-backed event workflows operating correctly.
- [ ] Dapr sidecars successfully handling infrastructure concerns.
- [ ] System validated on both Minikube and a Public Cloud Kubernetes provider.
- [ ] Deployment is fully reproducible via CI/CD and Helm.

## Governance
This constitution supersedes all other practices. Amendments require documentation and approval. All PRs and reviews must verify compliance with these principles.

**Version**: 5.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-02-09