import asyncio
import sys
from src.database import init_db
from src.models import User, Task, Session, Account, Verification, Conversation, Message # Ensure all models are registered
from src.database import engine
from sqlmodel import SQLModel

async def recreate_db():
    print("Dropping existing tables...")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
    print("Initializing database...")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    print("Database initialized successfully with Better Auth tables.")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(recreate_db())