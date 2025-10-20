from typing import List, Optional
from .models import Task, Priority, Status

class TaskStorage:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1

    def create(self, task_data: dict) -> Task:
        task = Task(
            id=self._next_id,
            **task_data
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list(self, priority: Optional[Priority] = None, status: Optional[Status] = None):
        results = self._tasks
        if priority:
            results = [t for t in results if t.priority == priority]
        if status:
            results = [t for t in results if t.status == status]
        return results

    def get(self, task_id: int) -> Optional[Task]:
        for t in self._tasks:
            if t.id == task_id:
                return t
        return None

    def update(self, task_id: int, updates: dict) -> Optional[Task]:
        task = self.get(task_id)
        if not task:
            return None
        for key, value in updates.items():
            setattr(task, key, value)
        return task

    def patch_status(self, task_id: int, status: str) -> Optional[Task]:
        task = self.get(task_id)
        if not task:
            return None
        task.status = status
        return task

    def delete(self, task_id: int) -> bool:
        task = self.get(task_id)
        if not task:
            return False
        self._tasks.remove(task)
        return True

storage = TaskStorage()
