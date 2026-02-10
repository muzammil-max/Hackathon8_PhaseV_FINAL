import os
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.routes import tasks, chat

# Set event loop policy for Windows to support asyncpg/SQLAlchemy correctly
if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(title="MyTodoApp Backend", version="0.1.0")

# CORS
# In production, set BACKEND_CORS_ORIGINS="https://your-frontend.vercel.app"
origins = settings.BACKEND_CORS_ORIGINS.split(",") if hasattr(settings, "BACKEND_CORS_ORIGINS") and settings.BACKEND_CORS_ORIGINS else [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "*" # Allow all for hackathon/testing ease - REMOVE in strict production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router)
app.include_router(chat.router)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Print exception for debugging
    print(f"Global exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )

@app.get("/health")
async def health_check():
    return {"status": "ok"}