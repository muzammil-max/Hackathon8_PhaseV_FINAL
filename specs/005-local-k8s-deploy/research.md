# Research: Local Kubernetes Deployment

## Decisions & Rationale

### 1. Local Kubernetes Environment
- **Decision**: Use Minikube.
- **Rationale**: Mandated by the constitution and feature spec. It provides a lightweight, local Kubernetes cluster suitable for development and testing.
- **Alternatives Considered**: Kind (Kubernetes in Docker), Docker Desktop Kubernetes. Minikube was chosen per project mandate.
- **Gap**: `minikube` is currently not installed or not in the PATH.

### 2. Package Manager
- **Decision**: Use Helm.
- **Rationale**: Mandated by the constitution ("Kubernetes Law") and feature spec. Helm allows for templated, versioned, and reproducible deployments.
- **Alternatives Considered**: Kustomize, plain manifests. Helm was chosen for better lifecycle management and configuration injection.
- **Gap**: `helm` is currently not installed or not in the PATH.

### 3. Containerization
- **Decision**: Use Docker.
- **Rationale**: Standard for containerization and mandated by the constitution.
- **Implementation**: Will create multi-stage Dockerfiles for optimized image sizes (frontend and backend).

### 4. Image Registry
- **Decision**: Use Minikube's internal Docker daemon (`eval $(minikube docker-env)`) or load images directly (`minikube image load`).
- **Rationale**: Avoids the need for an external registry (Docker Hub, etc.) during local development and keeps the loop tight.
- **Constraint**: Need to ensure the shell is configured correctly before building images.

### 5. AI DevOps Tools
- **Decision**: Integrate `kubectl-ai` and `kagent`.
- **Rationale**: Mandated by "AI DevOps Law".
- **Gap**: Need to verify installation/availability of these tools (assumed available or installable via pip/npm/brew equivalent).

## Outstanding Questions (Resolved)
- **Tool Availability**: Confirmed `minikube` and `helm` are missing. Implementation plan MUST include steps to install/verify these prerequisites or fail gracefully with instructions.
- **Database**: Will use a standard Postgres Helm chart or a simple StatefulSet for the local database to match the "Stateless backend" requirement.

## Action Items
1.  **Prerequisite Check**: The implementation tasks must start with verifying and installing Minikube and Helm.
2.  **Docker Config**: Ensure the plan covers pointing the local Docker CLI to Minikube's engine.
