from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from typing import Optional, List

@dataclass
class Task:
    id: int
    description: str
    status: str
    created_at: str
    updated_at: str
    priority: str = "medium"
    tags: List[str] = field(default_factory=list)
    due_date: Optional[str] = None
    recurrence: Optional[str] = None

    @classmethod
    def create(cls, id, description, priority="medium", tags=None, due_date=None, recurrence=None):
        now_str = datetime.now(timezone.utc).isoformat()
        return cls(
            id=id, description=description, status="pending",
            created_at=now_str, updated_at=now_str,
            priority=priority, tags=tags or [],
            due_date=due_date, recurrence=recurrence
        )

def to_dict(task: Task) -> dict:
    return asdict(task)

def from_dict(data: dict) -> Task:
    return Task(
        id=data['id'], description=data['description'],
        status=data['status'], created_at=data['created_at'],
        updated_at=data['updated_at'],
        priority=data.get('priority', 'medium'),
        tags=data.get('tags', []),
        due_date=data.get('due_date'),
        recurrence=data.get('recurrence')
    )