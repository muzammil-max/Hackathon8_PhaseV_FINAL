# Quickstart: Local Kubernetes Deployment

## Prerequisites

1.  **Minikube**: Install Minikube.
    -   Windows: `winget install minikube`
    -   Verify: `minikube version`
2.  **Helm**: Install Helm.
    -   Windows: `winget install Helm.Helm`
    -   Verify: `helm version`
3.  **Docker Desktop**: Ensure Docker Desktop is installed and running.
    -   Verify: `docker version`
4.  **kubectl**: Usually installed with Docker Desktop, but can be separate.
    -   Verify: `kubectl version --client`

## Setup

1.  **Start Minikube**:
    ```bash
    minikube start --driver=docker
    ```
2.  **Enable Ingress (Optional)**:
    ```bash
    minikube addons enable ingress
    ```
3.  **Set Docker Environment**:
    -   **PowerShell**: `minikube -p minikube docker-env --shell powershell | Invoke-Expression`
    -   **Bash**: `eval $(minikube -p minikube docker-env)`

## Building Images

1.  **Build Backend**:
    ```bash
    cd backend
    docker build -t todo-backend:v1 .
    ```
2.  **Build Frontend**:
    ```bash
    cd frontend
    docker build -t todo-frontend:v1 .
    ```

## Deployment

1.  **Install/Upgrade Helm Chart**:
    ```bash
    helm upgrade --install todo-app ./deploy/helm/todo-app
    ```
2.  **Verify Pods**:
    ```bash
    kubectl get pods
    ```
3.  **Access Application**:
    -   Get the service URL: `minikube service todo-frontend --url`
    -   Open in browser.

## Troubleshooting

-   **Check Pod Logs**: `kubectl logs <pod-name>`
-   **Describe Pod**: `kubectl describe pod <pod-name>`
-   **AI Help**: Use `kubectl-ai explain pod <pod-name>`
