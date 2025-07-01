from fastapi import Depends
from sqlmodel import Session

from Repos.TaskRepo import TaskRepo
from model.TaskCreate import TaskCreate
from db.session import get_session


class TaskService:
    def __init__(self, session: Session = Depends(get_session)):
        self.repo = TaskRepo(session)

    def create_task(self, task: TaskCreate):
        return self.repo.create_task(task)

    def get_all_tasks(self):
        return self.repo.get_all_tasks()

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
