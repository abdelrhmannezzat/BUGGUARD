from datetime import datetime

from sqlmodel import SQLModel, Field
from sqlalchemy import String, DateTime, func
from pydantic import constr

from model.TaskStatus import TaskStatus
from model.TaskPriority import TaskPriority


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)

    title: constr(max_length=200) = Field(
        sa_type=String(200),
        nullable=False
    )

    description: constr(max_length=1000) = Field(
        sa_type=String(1000),
        nullable=True
    )

    status: TaskStatus = Field(
        default=TaskStatus.pending,
        nullable=False
    )

    priority: TaskPriority = Field(
        default=TaskPriority.medium,
        nullable=False
    )

    created_at: datetime = Field(
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={
            "default": func.now()
        },
        nullable=False
    )

    updated_at: datetime = Field(
        sa_type=DateTime,
        nullable=True
    )

    due_date: datetime = Field(
        sa_type=DateTime,
        nullable=True
    )

    assigned_to: constr(max_length=100) = Field(
        sa_type=String(100),
        nullable=True
    )



