from typing import List
import uuid
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database import get_session
from src.models import Task, TaskCreate, TaskRead, TaskUpdate, User, TaskStatus
from src.auth import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(
    task: TaskCreate, 
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    print(f"Creating task for user {current_user.id}: {task}")
    try:
        new_task = Task(**task.model_dump(), owner_id=current_user.id)
        session.add(new_task)
        await session.commit()
        await session.refresh(new_task)
        print(f"Task created successfully: {new_task.id}")
        return new_task
    except Exception as e:
        print(f"Error creating task: {e}")
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[TaskRead])
async def read_tasks(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    stmt = select(Task).where(Task.owner_id == current_user.id).order_by(Task.created_at.desc())
    result = await session.execute(stmt)
    tasks = result.scalars().all()
    return tasks

@router.get("/{task_id}", response_model=TaskRead)
async def read_task(
    task_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    stmt = select(Task).where(Task.id == task_id, Task.owner_id == current_user.id)
    result = await session.execute(stmt)
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskRead)
async def update_task(
    task_id: uuid.UUID,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    stmt = select(Task).where(Task.id == task_id, Task.owner_id == current_user.id)
    result = await session.execute(stmt)
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task_data = task_update.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(task, key, value)
    
    task.updated_at = datetime.utcnow()
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    stmt = select(Task).where(Task.id == task_id, Task.owner_id == current_user.id)
    result = await session.execute(stmt)
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    await session.delete(task)
    await session.commit()
    return None

@router.patch("/{task_id}/complete", response_model=TaskRead)
async def toggle_task_completion(
    task_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    stmt = select(Task).where(Task.id == task_id, Task.owner_id == current_user.id)
    result = await session.execute(stmt)
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task.status == TaskStatus.DONE:
        task.status = TaskStatus.TODO
    else:
        task.status = TaskStatus.DONE
        
    task.updated_at = datetime.utcnow()
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task
