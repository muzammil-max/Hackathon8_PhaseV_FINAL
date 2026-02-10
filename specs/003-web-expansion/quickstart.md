# Quickstart: Phase 2 Web Expansion

## Prerequisites
- Node.js 18+
- Python 3.10+
- PostgreSQL (or access to Neon instance)

## Setup

1. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   cp .env.example .env  # Configure DB_URL and SECRET_KEY
   python -m src.db_init  # Run migrations/init db
   ```

2. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   cp .env.local.example .env.local  # Configure NEXT_PUBLIC_API_URL
   ```

## Running

1. **Start Backend**
   ```bash
   # From backend/
   uvicorn src.main:app --reload
   ```

2. **Start Frontend**
   ```bash
   # From frontend/
   npm run dev
   ```

3. **Access**
   Open http://localhost:3000
