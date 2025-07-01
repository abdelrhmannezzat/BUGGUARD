from typing import List

from model.Task import Task
from model.TaskCreate import TaskCreate
from sqlmodel import Session, select


class TaskRepo:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, task: TaskCreate) -> Task:
        task = Task(**task.model_dump())
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.session.exec(select(Task)).all()

    def get_task_by_id(self, task_id: int) -> Task:
        return self.session.exec(select(Task).where(Task.id == task_id)).first()

    def delete_task_by_id(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            self.session.delete(task)
            self.session.commit()
            return True
        return False

    def update_task(self, task_id, task_update) -> Task | None:
        task = self.get_task_by_id(task_id)
        if not task:
            return None
        for key, value in task_update.model_dump().items():
            if value:
                setattr(task, key, value)

        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def get_tasks_by_status(self, status) -> List[Task]:
        return self.session.exec(select(Task).where(Task.status == status)).all()

    def get_tasks_by_priority(self, priority) -> List[Task]:
        return self.session.exec(select(Task).where(Task.priority == priority)).all()
