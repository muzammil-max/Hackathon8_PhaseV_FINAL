# Cloud Deployment Guide (Phase 5)

This guide covers deploying the **Event-Driven Todo AI system** to a Managed Kubernetes cluster (AKS, GKE, or OKE).

## Prerequisites
1.  **Cloud CLI**: `az`, `gcloud`, or `oci` installed and authenticated.
2.  **Kubeconfig**: Pointing to your cloud cluster (`kubectl get nodes`).
3.  **Container Registry (ACR/GCR/OCIR)**: A registry to host your images.
4.  **Dapr Extension**: Dapr must be installed on your cloud cluster.
    - `dapr init -k` or via Cloud marketplace.

## Step 1: Build and Push Images
Replace `REGISTRY` with your registry URL (e.g., `myregistry.azurecr.io`).

```bash
export REGISTRY=myregistry.azurecr.io/todo

docker build -t $REGISTRY/chat-service:latest backend/services/chat
docker build -t $REGISTRY/task-service:latest backend/services/task
docker build -t $REGISTRY/scheduler-service:latest backend/services/scheduler
docker build -t $REGISTRY/notification-service:latest backend/services/notification

docker push $REGISTRY/chat-service:latest
docker push $REGISTRY/task-service:latest
docker push $REGISTRY/scheduler-service:latest
docker push $REGISTRY/notification-service:latest
```

## Step 2: Configure Infrastructure
Ensure your `deploy/helm/todo-app/cloud-values.yaml` has the correct connection strings for your managed Redis and Kafka.

## Step 3: Deploy with Helm
```bash
helm upgrade --install todo-app deploy/helm/todo-app \
  -f deploy/helm/todo-app/cloud-values.yaml \
  --set image.repository=$REGISTRY
```

## Step 4: Verify Deployment
1.  **Check Pods**: `kubectl get pods -w` (Verify Dapr sidecars are running).
2.  **Get Public IP**: 
    ```bash
    kubectl get svc chat-service
    ```
3.  **Test API**:
    ```bash
    curl -X POST http://<EXTERNAL-IP>/api/chat -d '{"message": "Add Buy Milk every day"}'
    ```

## Step 5: Observability
Use Dapr Dashboard to monitor the event flow:
```bash
dapr dashboard -k
```
