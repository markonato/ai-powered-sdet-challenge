from typing import Dict, List, Optional

from api.models import Task, Priority, Status


class TaskStorage:
    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self._id_counter = 1

    def create(self, data: dict) -> Task:
        task = Task(id=self._id_counter, **data)
        self.tasks[self._id_counter] = task
        self._id_counter += 1
        return task

    def list(self, priority: Optional[Priority] = None, status: Optional[Status] = None) -> List[Task]:
        tasks = list(self.tasks.values())
        if priority:
            tasks = [t for t in tasks if t.priority == priority]
        if status:
            tasks = [t for t in tasks if t.status == status]
        return tasks

    def get(self, task_id: int) -> Optional[Task]:
        return self.tasks.get(task_id)

    def update(self, task_id: int, data: dict) -> Optional[Task]:
        if task_id not in self.tasks:
            return None
        updated_data = self.tasks[task_id].model_copy(update=data, deep=True)
        self.tasks[task_id] = updated_data
        return updated_data

    def delete(self, task_id: int) -> bool:
        return self.tasks.pop(task_id, None) is not None

    def patch_status(self, task_id: int, status: Status) -> Optional[Task]:
        if task_id not in self.tasks:
            return None
        task = self.tasks[task_id]
        task.status = status
        self.tasks[task_id] = task
        return task


# Singleton instance
storage = TaskStorage()
