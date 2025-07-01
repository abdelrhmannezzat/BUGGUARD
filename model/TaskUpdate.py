from pydantic import BaseModel, constr
from model.TaskStatus import TaskStatus
from model.TaskPriority import TaskPriority
from datetime import datetime


class TaskUpdate(BaseModel):
    title: constr(max_length=200) | None = None
    description: constr(max_length=1000) | None = None
    status: TaskStatus = TaskStatus.pending
    priority: TaskPriority = TaskPriority.medium
    due_date: datetime | None = None
    assigned_to: constr(max_length=100) | None = None
    updated_at: datetime | None = None
