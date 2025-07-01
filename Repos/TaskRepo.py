from typing import List, Optional

from fastapi import Query

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

    def get_all_tasks(self, status: Optional[str] = None,
    assigned_to: Optional[str] = None,
    limit: int = Query(default=10, ge=1),
    offset: int = Query(default=0, ge=0),) -> List[Task]:
        query = select(Task)
        if status:
            query = query.where(Task.status == status)
        if assigned_to:
            query = query.where(Task.assigned_to == assigned_to)
        tasks = self.session.exec(query.offset(offset).limit(limit)).all()
        return tasks

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
