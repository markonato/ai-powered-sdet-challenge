from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Status(str, Enum):
    pending = "pending"
    completed = "completed"


class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    priority: Priority = Priority.medium
    due_date: Optional[date]
    status: Status = Status.pending

    @classmethod
    def validate_due_date(self, v):
        from datetime import date
        if v and v < date.today():
            raise ValueError("Due date cannot be in the past")
        return v
