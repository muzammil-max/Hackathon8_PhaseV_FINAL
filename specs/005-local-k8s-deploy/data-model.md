# Data Model: Local Kubernetes Deployment

## Entities

### 1. Container Image
- **Description**: An immutable, versioned package of the application code and dependencies.
- **Attributes**:
  - `registry`: Image repository (e.g., `local` for Minikube).
  - `name`: Service name (e.g., `todo-backend`, `todo-frontend`).
  - `tag`: Version identifier (e.g., `v1.0.0`, `latest`).
  - `build_args`: Build-time variables.

### 2. Helm Release
- **Description**: A specific instance of the deployed application managed by Helm.
- **Attributes**:
  - `name`: Release name (e.g., `todo-app`).
  - `namespace`: Kubernetes namespace (e.g., `default`).
  - `chart`: Helm chart reference (e.g., `./deploy/helm/todo-app`).
  - `values`: User-provided configuration overrides (`values.yaml`).

### 3. Kubernetes ConfigMap
- **Description**: Non-confidential configuration data injected as environment variables.
- **Attributes**:
  - `DATABASE_URL`: Connection string for the database (internal cluster DNS).
  - `NEXT_PUBLIC_API_URL`: Backend API URL for the frontend.
  - `LOG_LEVEL`: Application logging verbosity.

### 4. Kubernetes Secret
- **Description**: Sensitive data injected as environment variables or mounted files.
- **Attributes**:
  - `POSTGRES_USER`: Database username.
  - `POSTGRES_PASSWORD`: Database password.
  - `JWT_SECRET`: Secret key for token generation.

### 5. Kubernetes Service
- **Description**: Network abstraction for accessing application pods.
- **Attributes**:
  - `type`: Service type (`ClusterIP`, `NodePort`, `LoadBalancer`).
  - `port`: Port exposed by the service.
  - `targetPort`: Port application listens on inside the container.

### 6. Kubernetes Deployment
- **Description**: Manages replica sets and pod updates for stateless services.
- **Attributes**:
  - `replicas`: Number of pod instances.
  - `image`: Container image to run.
  - `env`: Environment variables (from ConfigMaps/Secrets).
  - `resources`: CPU/Memory requests and limits.
  - `probes`: Liveness/Readiness checks.

### 7. Kubernetes StatefulSet (Optional/Database)
- **Description**: Manages stateful applications (PostgreSQL).
- **Attributes**:
  - `replicas`: Number of database instances (usually 1 for dev).
  - `volumeClaimTemplates`: Persistent Volume Claims for data storage.
