from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, field_validator
from api.models import Priority, Status


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    priority: Priority = Priority.medium
    due_date: Optional[date]

    @classmethod
    def validate_due_date(self, v):
        from datetime import date
        if v and v < date.today():
            raise ValueError("Due date cannot be in the past")
        return v


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    priority: Optional[Priority]
    due_date: Optional[date]

    @classmethod
    def validate_due_date(self, v):
        from datetime import date
        if v and v < date.today():
            raise ValueError("Due date cannot be in the past")
        return v


class TaskStatusUpdate(BaseModel):
    status: Status
