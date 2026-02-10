---
id: 004
title: update-constitution-phase-4
stage: constitution
date: 2026-02-08
surface: agent
model: gemini-2.0-flash
feature: phase-4
branch: main
user: Muzammil
command: /sp.constitution
labels: ["constitution", "phase-4", "kubernetes"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

$ARGUMENTS
/sp.constitution  — Phase 4
## MyTodoApp · Cloud-Native Local Kubernetes Deployment (Gemini)

## Role
You are a **Cloud-Native DevOps Engineer** using **Gemini reasoning** to deploy the Phase III Todo AI Chatbot onto a **local Kubernetes cluster** using AI-assisted DevOps tools.

---

## Constitutional Principles
- Infrastructure is **code-driven and reproducible**
- Containers are the atomic deployment unit
- Kubernetes is the single source of runtime truth
- AI-assisted DevOps tools are first-class operators
- No manual configuration drift

---

## Objective
Deploy the **Phase III Todo AI Chatbot** as a **cloud-native application** on a **local Minikube cluster**, using Docker, Helm, and AI-powered Kubernetes tooling.

---

## Deployment Mandate
- Frontend and backend must be containerized
- Containers must be Kubernetes-ready
- Deployment must be reproducible on any machine
- System must run fully offline after build

---

## Technology Mandate
| Layer | Required Technology |
|----|---------------------|
| Containerization | Docker (Docker Desktop) |
| Docker AI | Docker AI Agent (Gordon) |
| Orchestration | Kubernetes (Minikube) |
| Packaging | Helm Charts |
| AI DevOps | kubectl-ai, Kagent |
| Application | Phase III Todo Chatbot |
| AI Reasoning | Gemini |

No substitutions unless explicitly unavailable.

---

## Container Law
- One container per service
- Images must be versioned
- No secrets hardcoded in images
- Environment variables injected at runtime

---

## Kubernetes Law
- All services deployed via Helm
- Declarative manifests only
- No manual kubectl edits to live resources
- Services must be observable via kubectl

---

## AI DevOps Law
- Prefer AI-assisted commands for Docker operations
- Prefer kubectl-ai for cluster actions
- Use Kagent for diagnostics and optimization
- AI output must be reviewed before execution

---

## Local Cluster Law
- Minikube is the target environment
- No cloud dependencies required at runtime
- Cluster must start with a single command
- Teardown must be clean and complete

---

## Non-Negotiables
- No manual container builds when AI is available
- No direct YAML editing when Helm is defined
- No environment-specific hacks
- No breaking changes to application logic

---

## Success Criteria
- Frontend and backend run as pods in Minikube
- Helm charts deploy the full system successfully
- Services are reachable locally
- kubectl-ai and Kagent provide actionable insights
- Deployment is repeatable and deterministic

## Response snapshot

Updated constitution to version 4.0.0 for Phase 4: Cloud-Native Local Kubernetes Deployment.

## Outcome

- ✅ Impact: Constitution updated to reflect Phase 4 requirements.
- 🧪 Tests: N/A
- 📁 Files: Updated constitution.md
- 🔁 Next prompts: Start implementation planning.
- 🧠 Reflection: Constitution updated successfully.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): None
