from datetime import datetime, timezone, timedelta

from fastapi import FastAPI, HTTPException, Query, Response
from typing import Optional, List

from api.schemas import TaskStatusUpdate
from api.models import Task, TaskCreate, Priority, Status
from api.storage import storage

app = FastAPI(title="Task Management API", version="1.0.0")

# prepopulate task at startup if storage is empty
if not storage.list():
    storage.create({
        "title": "Pre-populated Task",
        "description": "Task created for tests",
        "priority": Priority.medium,
        "due_date": datetime.now(timezone.utc) + timedelta(days=1),
        "status": Status.pending
    })

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    # ensure due_date is in the future
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

@app.get("/tasks/{id}", response_model=Task)
def get_task(id: int):
    existing_task = storage.get(id)
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return existing_task

@app.put("/tasks/{id}", response_model=Task)
def update_task(id: int, updates: TaskCreate):
    existing_task = storage.get(id)
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    updated = storage.update(id, updates.model_dump(exclude_unset=True))
    return updated

@app.delete("/tasks/{id}", response_model=dict)
def delete_task(id: int):
    existing_task = storage.get(id)
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    storage.delete(id)
    return Response(status_code=204)

@app.patch("/tasks/{id}/status", response_model=Task)
def update_status(id: int, status_update: TaskStatusUpdate):
    existing_task = storage.get(id)
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    try:
        new_status = Status(status_update.status)
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid status value")
    updated = storage.patch_status(id, status_update.status)
    return updated
