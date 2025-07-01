from datetime import datetime
from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status

from Service.TaskService import TaskService
from model.Task import Task
from model.TaskCreate import TaskCreate
from model.TaskPriority import TaskPriority
from model.TaskStatus import TaskStatus
from model.TaskUpdate import TaskUpdate

router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, service: TaskService = Depends()):
    if task.due_date and task.due_date < datetime.now():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="due_date must be in the future"
        )
    if task.title and task.title.strip() == '':
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="title cannot be empty"
        )
    task.title = task.title.strip()
    return service.create_task(task)


@router.get("", response_model=List[Task])
def get_all_tasks(
    status: Optional[str] = None,
    assigned_to: Optional[str] = None,
    limit: int = Query(default=10, ge=1),
    offset: int = Query(default=0, ge=0),
    service: TaskService = Depends()
):
    return service.get_all_tasks(status,assigned_to,limit,offset)


@router.get("/{task_id}")
def get_task(task_id: int, service: TaskService = Depends()):
    return service.get_task_by_id(task_id)


@router.delete("/{task_id}")
def delete_task(task_id: int, service: TaskService = Depends()):
    return service.delete_task_by_id(task_id)


@router.put("/{task_id}")
def update_task(task_id: int, task: TaskUpdate, service: TaskService = Depends()):
    if task.due_date and task.due_date < datetime.now():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="due_date must be in the future"
        )
    if task.title and task.title.strip() == '':
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="title cannot be empty"
        )
    task.title = task.title.strip()
    return service.update_task(task_id, task)


@router.get("/status/{status}")
def get_tasks_by_status(status: TaskStatus, service: TaskService = Depends()):
    return service.get_tasks_by_status(status)


@router.get("/priority/{priority}")
def get_tasks_by_status(priority: TaskPriority, service: TaskService = Depends()):
    return service.get_tasks_by_priority(priority)
