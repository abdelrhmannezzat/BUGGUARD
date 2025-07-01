from typing import Optional

from fastapi import Depends, Query
from sqlmodel import Session

from Repos.TaskRepo import TaskRepo
from model.TaskCreate import TaskCreate
from db.session import get_session


class TaskService:
    def __init__(self, session: Session = Depends(get_session)):
        self.repo = TaskRepo(session)

    def create_task(self, task: TaskCreate):
        return self.repo.create_task(task)

    def get_all_tasks(self,status: Optional[str] = None,
    assigned_to: Optional[str] = None,
    limit: int = Query(default=10, ge=1),
    offset: int = Query(default=0, ge=0),):
        return self.repo.get_all_tasks(status,assigned_to,limit,offset)

    def get_task_by_id(self, task_id):
        return self.repo.get_task_by_id(task_id)

    def delete_task_by_id(self, task_id):
        return self.repo.delete_task_by_id(task_id)

    def update_task(self, task_id, task):
        return self.repo.update_task(task_id, task)

    def get_tasks_by_status(self, status):
        return self.repo.get_tasks_by_status(status)

    def get_tasks_by_priority(self, priority):
        return self.repo.get_tasks_by_priority(priority)
