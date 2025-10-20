from datetime import datetime, timezone, timedelta

from fastapi import FastAPI, HTTPException, Query, Response
from typing import Optional, List

from .schemas import TaskStatusUpdate
from .models import Task, TaskCreate, Priority, Status
from .storage import storage

app = FastAPI(title="Task Management API", version="1.0.0")

# Prepopulate task ID 1 at startup
if not storage.list():  # Only if storage is empty
    storage.create({
        "title": "Pre-populated Task",
        "description": "Task created for tests",
        "priority": Priority.medium,
        "due_date": datetime.now(timezone.utc) + timedelta(days=1),
        "status": Status.pending
    })

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    # Ensure due_date is in the future
    due_date = task.due_date
    if due_date.tzinfo is None:
        due_date = due_date.replace(tzinfo=timezone.utc)
    if due_date < datetime.now(timezone.utc):
        raise HTTPException(status_code=422, detail="Due_date cannot be in the past")

    task_data = task.model_dump(mode="json")  # convert Pydantic model to dict
    new_task = storage.create(task_data)
    return new_task

@app.get("/tasks", response_model=List[Task])
def list_tasks(
        priority: Optional[Priority] = Query(None),
        status: Optional[Status] = Query(None)
):
    return storage.list(priority=priority, status=status)

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = storage.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updates: TaskCreate):
    updated = storage.update(task_id, updates.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int):
    ok = storage.delete(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return Response(status_code=204)

@app.patch("/tasks/{task_id}/status", response_model=Task)
def update_status(task_id: int, status_update: TaskStatusUpdate):
    updated = storage.patch_status(task_id, status_update.status)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated
