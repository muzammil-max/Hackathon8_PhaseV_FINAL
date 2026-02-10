# Tasks: Local Kubernetes Deployment

**Feature Branch**: `005-local-k8s-deploy`
**Status**: In Progress

## Phase 1: Setup
**Goal**: Ensure all necessary tools are installed and configured.

- [x] T001 Install Minikube on local environment (Windows)
- [x] T002 Install Helm on local environment (Windows)
- [ ] T003 Install kubectl-ai and kagent (AI DevOps tools)
- [x] T004 Verify Minikube, Helm, and kubectl installations
- [x] T005 Start Minikube cluster with Docker driver
- [x] T006 Enable Minikube ingress addon

## Phase 2: Foundational (Dockerization)
**Goal**: Create production-ready container images for frontend and backend.
**Prerequisite**: Phase 1 complete.

- [x] T007 [P] Create multi-stage Dockerfile for backend in `backend/Dockerfile`
- [x] T008 [P] Create multi-stage Dockerfile for frontend in `frontend/Dockerfile`
- [x] T009 Configure local Docker client to use Minikube docker-env
- [x] T010 Build backend Docker image `todo-backend:v1` in Minikube registry
- [x] T011 Build frontend Docker image `todo-frontend:v1` in Minikube registry

## Phase 3: Run Application on Minikube (User Story 1 - P1)
**Goal**: Deploy the full application stack to Minikube using Helm.
**Independent Test**: Application is accessible and functional on Minikube.

### Helm Chart scaffolding
- [x] T012 [US1] Create basic Helm chart structure in `deploy/helm/todo-app/Chart.yaml`
- [x] T013 [US1] Create default `values.yaml` in `deploy/helm/todo-app/values.yaml`

### Database & Secrets
- [x] T014 [US1] Define Postgres StatefulSet (or dependency) in `deploy/helm/todo-app/templates/db-statefulset.yaml`
- [x] T015 [US1] Define Postgres Service in `deploy/helm/todo-app/templates/db-service.yaml`
- [x] T016 [US1] Define Secrets for DB credentials in `deploy/helm/todo-app/templates/secrets.yaml`
- [x] T017 [US1] Define ConfigMap for global settings in `deploy/helm/todo-app/templates/configmap.yaml`

### Backend Deployment
- [x] T018 [US1] Define Backend Deployment in `deploy/helm/todo-app/templates/backend-deployment.yaml`
- [x] T019 [US1] Define Backend Service in `deploy/helm/todo-app/templates/backend-service.yaml`
- [x] T020 [US1] Add Readiness/Liveness probes to Backend Deployment

### Frontend Deployment
- [x] T021 [US1] Define Frontend Deployment in `deploy/helm/todo-app/templates/frontend-deployment.yaml`
- [x] T022 [US1] Define Frontend Service in `deploy/helm/todo-app/templates/frontend-service.yaml`
- [x] T023 [US1] Add Readiness/Liveness probes to Frontend Deployment

### Ingress/Access
- [x] T024 [US1] Define Ingress resource (or NodePort) in `deploy/helm/todo-app/templates/ingress.yaml`

### Deployment & Verification
- [x] T025 [US1] Deploy chart to Minikube using `helm install`
- [x] T026 [US1] Verify all pods are running and services are accessible

## Phase 4: Reproducible Deployment (User Story 2 - P2)
**Goal**: Ensure the deployment is configurable and reproducible.
**Independent Test**: `helm uninstall` followed by `helm install` works perfectly.

- [x] T027 [US2] Refactor `values.yaml` to parameterize all image tags and resource limits
- [x] T028 [US2] Refactor `values.yaml` to parameterize ports and replica counts
- [x] T029 [US2] Test `helm upgrade` by changing a configuration value (e.g., replicas)
- [x] T030 [US2] Verify complete teardown with `helm uninstall`
- [x] T031 [US2] Verify fresh install from scratch works without manual intervention

## Phase 5: AI-Assisted Operations (User Story 3 - P3)
**Goal**: Validate and optimize using AI tools.
**Independent Test**: AI tools provide actionable output.

- [ ] T032 [US3] Run `kubectl-ai` to analyze the deployed resources (Skipped: Tool install failed in current environment)
- [ ] T033 [US3] Run `kubectl-ai` to explain a specific pod status (Skipped)
- [ ] T034 [US3] (If available) Run `kagent` to inspect logs and metrics (Skipped)
- [ ] T035 [US3] Document AI tool usage and outputs in `specs/005-local-k8s-deploy/ai-ops-report.md` (Documented in DEPLOY.md)

## Phase 6: Polish & Documentation
**Goal**: Finalize documentation and artifacts.

- [x] T036 Create `DEPLOY.md` with detailed Kubernetes deployment instructions
- [x] T037 Update project `README.md` to reference new deployment method
- [x] T038 Review and cleanup unused files or temporary configs

## Dependencies

- Phase 2 (Docker) depends on Phase 1 (Setup)
- Phase 3 (US1) depends on Phase 2 (Docker images must exist)
- Phase 4 (US2) depends on Phase 3 (Chart must exist)
- Phase 5 (US3) depends on Phase 3 (Cluster must be running)

## Parallel Execution Opportunities

- T007 (Backend Dockerfile) and T008 (Frontend Dockerfile) can be done in parallel.
- T010 (Build Backend) and T011 (Build Frontend) can be done in parallel.
- T018 (Backend K8s) and T021 (Frontend K8s) can be done in parallel once DB/Config is defined.

## Implementation Strategy

1.  **MVP**: Get the services running on Minikube manually or with a basic chart (Phase 1-3).
2.  **Refinement**: Make the chart robust and configurable (Phase 4).
3.  **Verification**: Use AI tools to validate best practices (Phase 5).
