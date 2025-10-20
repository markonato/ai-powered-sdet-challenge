from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Status(str, Enum):
    pending = "pending"
    completed = "completed"

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
