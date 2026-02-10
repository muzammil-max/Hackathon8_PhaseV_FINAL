# MyTodoApp — Web Expansion

A secure, multi-user full-stack web application for task management.

## Tech Stack
- **Frontend**: Next.js 14 (App Router), TailwindCSS, Sonner (Toasts)
- **Backend**: FastAPI (Python), SQLModel, PostgreSQL
- **Auth**: JWT (JSON Web Tokens)

## Prerequisites
- Node.js 18+
- Python 3.10+
- PostgreSQL (or Neon.tech account)

## Setup & Running

### 1. Backend
```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# Unix/macOS
source venv/bin/activate

pip install -r requirements.txt

# Configure environment
cp .env.example .env # Or create manually
# In .env:
# DATABASE_URL=postgresql+asyncpg://user:password@localhost/mytodo_db
# SECRET_KEY=your_random_secret_key

# Run the server
uvicorn src.main:app --reload
```

### 2. Frontend
```bash
cd frontend
npm install

# Configure environment
cp .env.local.example .env.local
# In .env.local:
# NEXT_PUBLIC_API_URL=http://localhost:8000

# Run the development server
npm run dev
```

## Features
- **User Authentication**: Secure signup and login.
- **Private Tasks**: Each user has their own private task list.
- **Task Management**: Create, Read, Update, Delete, and Toggle completion.
- **Responsive Design**: Works on mobile and desktop.
- **Real-time Feedback**: Toast notifications for user actions.

## Phase 4: Cloud-Native Local Kubernetes Deployment

The application is now containerized and ready for local Kubernetes deployment using Helm and Minikube.

- **Dockerization**: Multi-stage builds for frontend (Next.js) and backend (FastAPI).
- **Orchestration**: Managed via Helm charts in `deploy/helm/todo-app`.
- **Infrastructure**: Runs on local Minikube cluster with Docker driver.

For detailed instructions, see [DEPLOY.md](./DEPLOY.md).

### Quick Start (K8s)
1. `minikube start --driver=docker`
2. `minikube -p minikube docker-env --shell powershell | Invoke-Expression`
3. `docker build -t todo-backend:v1 ./backend`
4. `docker build -t todo-frontend:v1 ./frontend`
5. `helm upgrade --install todo-app ./deploy/helm/todo-app`