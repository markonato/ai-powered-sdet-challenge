from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field

from api.models import Priority, Status

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    priority: Priority = Priority.medium
    due_date: datetime
    status: Optional[Status] = Status.pending

class Task(TaskCreate):
    id: int

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    priority: Optional[Priority]
    due_date: datetime

class TaskStatusUpdate(BaseModel):
    status: Status
