# 🚀 TaskFlow Implementation Guide

Welcome to **TaskFlow**, a premium, secure, multi-user task management application. This guide will help you get the system up and running on your local machine.

---

## 🛠 Prerequisites

Ensure you have the following installed:
- **Python 3.10+**
- **Node.js 18+** (with npm)
- **PostgreSQL** (or a cloud provider like Neon.tech)

---

## 🏗 Setup Instructions

### 1. Backend (FastAPI)

1.  **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Unix/macOS
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**:
    Create a `.env` file in the `backend` folder:
    ```env
    DATABASE_URL=postgresql+asyncpg://user:password@localhost/mytodo_db
    SECRET_KEY=your_random_secret_key_here
    ```

5.  **Initialize Database**:
    ```bash
    python init_db.py
    ```

6.  **Run the Server**:
    ```bash
    uvicorn src.main:app --reload
    ```
    *The backend will be available at `http://localhost:8000`*

---

### 2. Frontend (Next.js)

1.  **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```

2.  **Install dependencies**:
    ```bash
    npm install --legacy-peer-deps
    ```

3.  **Configure Environment**:
    Create a `.env.local` file in the `frontend` folder:
    ```env
    NEXT_PUBLIC_API_URL=http://localhost:8000
    BETTER_AUTH_URL=http://localhost:3000
    BETTER_AUTH_SECRET=your_better_auth_secret
    DATABASE_URL=your_postgresql_url_for_better_auth
    ```

4.  **Run the Development Server**:
    ```bash
    npm run dev
    ```
    *The frontend will be available at `http://localhost:3000`*

---

## ✨ Key Features

-   **Premium UI**: A high-end, motion-rich design using Tailwind CSS and Framer Motion.
-   **Dark Mode**: Native support for dark/light/system themes.
-   **Secure Auth**: Multi-user isolation powered by Better Auth.
-   **Inline Editing**: Update your tasks directly in the list with a seamless interface.
-   **Real-time Progress**: Visual progress tracking and productivity insights.
-   **Responsive**: Works beautifully on mobile, tablet, and desktop.

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

---

## 🛠 Troubleshooting

-   **Styles not applying?**: Delete the `frontend/.next` folder and restart the dev server.
-   **Database Errors?**: Ensure your `DATABASE_URL` is correct and the PostgreSQL service is running.
-   **Auth Issues?**: Clear browser cookies and ensure `BETTER_AUTH_URL` matches your frontend URL.

---

Enjoy your productivity journey with **TaskFlow**! 🌟
