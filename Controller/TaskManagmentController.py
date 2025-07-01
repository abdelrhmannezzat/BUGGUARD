from fastapi import APIRouter, Depends
from Service.TaskService import TaskService
from model.TaskCreate import TaskCreate
from model.TaskPriority import TaskPriority
from model.TaskStatus import TaskStatus
from model.TaskUpdate import TaskUpdate

router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.post("")
def create_task(task: TaskCreate, service: TaskService = Depends()):
    return service.create_task(task)


@router.get("")
def get_all_tasks(service: TaskService = Depends()):
    return service.get_all_tasks()


@router.get("/{task_id}")
def get_task(task_id: int, service: TaskService = Depends()):
    return service.get_task_by_id(task_id)


@router.delete("/{task_id}")
def delete_task(task_id: int, service: TaskService = Depends()):
    return service.delete_task_by_id(task_id)


@router.put("/{task_id}")
def update_task(task_id: int, task: TaskUpdate, service: TaskService = Depends()):
    return service.update_task(task_id, task)


@router.get("/status/{status}")
def get_tasks_by_status(status: TaskStatus, service: TaskService = Depends()):
    return service.get_tasks_by_status(status)


@router.get("/priority/{priority}")
def get_tasks_by_status(priority: TaskPriority, service: TaskService = Depends()):
    return service.get_tasks_by_priority(priority)
