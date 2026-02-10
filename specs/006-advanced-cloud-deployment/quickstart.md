# Quickstart: Local Minikube Deployment

**Feature**: `006-advanced-cloud-deployment`

## Prerequisites
1.  **Docker Desktop**: Installed and running.
2.  **Minikube**: `minikube start --cpus 4 --memory 8192`
3.  **Helm v3**: Installed.
4.  **Dapr CLI**: `dapr init -k` (Initialize Dapr on K8s).
5.  **Kafka (Optional/Manual)**: If not using the included Helm chart dependency.

## Deployment Steps

1.  **Build Docker Images**:
    ```bash
    eval $(minikube docker-env)
    docker build -t todo/chat-service:local ./backend/services/chat
    docker build -t todo/task-service:local ./backend/services/task
    docker build -t todo/scheduler-service:local ./backend/services/scheduler
    docker build -t todo/notification-service:local ./backend/services/notification
    ```

2.  **Install via Helm**:
    ```bash
    helm install todo-app ./deploy/helm/todo-app 
      --set global.env=local 
      --set dapr.enabled=true
    ```

3.  **Verify Pods**:
    ```bash
    kubectl get pods
    # Expect: chat-service, task-service, scheduler, notification + dapr sidecars + kafka/redis
    ```

4.  **Port Forward**:
    ```bash
    kubectl port-forward svc/chat-service 8000:80
    ```

5.  **Test**:
    ```bash
    curl -X POST http://localhost:8000/api/chat -d '{"message": "Test task"}'
    ```

## Troubleshooting
- **Dapr Sidecar Missing**: Check `dapr.io/enabled: "true"` annotation.
- **Kafka Connection**: Check `pubsub.yaml` component broker address (usually `my-cluster-kafka-bootstrap.default.svc.cluster.local:9092`).
