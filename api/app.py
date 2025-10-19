from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List
from api.models import Task, Priority, Status
from api.schemas import TaskCreate, TaskUpdate, TaskStatusUpdate
from api.storage import storage

app = FastAPI(title="Task Management API", version="1.0.0")


@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    new_task = storage.create(task.model_dump())
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
def update_task(task_id: int, updates: TaskUpdate):
    updated = storage.update(task_id, updates.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int):
    ok = storage.delete(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}


@app.patch("/tasks/{task_id}/status", response_model=Task)
def update_status(task_id: int, patch: TaskStatusUpdate):
    updated = storage.patch_status(task_id, patch.status)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated
