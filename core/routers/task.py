from fastapi import APIRouter
from fastapi.responses import JSONResponse

from db.queries.task import TaskOrm
from utils.schemas.task import TaskSchema
from utils.pydatic_to_orm.task import pydantic_to_sqlalchemy

task_router = APIRouter()


@task_router.get("/tasks", response_model=TaskSchema)
def get_tasks() -> JSONResponse:
    tasks = TaskOrm.get_tasks()
    return JSONResponse(content={"Tasks": tasks})


@task_router.get("/tasks/{task_id}", response_model=TaskSchema)
def get_task_by_id(task_id: int) -> JSONResponse:
    task_data = TaskOrm.get_task_by_id(task_id)
    task = TaskSchema.from_orm(task_data).dict()
    return JSONResponse(content={"Task": task})


@task_router.post("tasks", response_model=TaskSchema)
def create_task(new_task: TaskSchema) -> JSONResponse:
    new_task_data = TaskOrm.create_task(pydantic_to_sqlalchemy(task=new_task))
    new_task = TaskSchema.from_orm(new_task_data).dict()
    return JSONResponse(content={"Task": new_task})


@task_router.put("tasks", response_model=TaskSchema)
def update_task(task_data, task_id):
    data_to_update = TaskOrm.update_task(data=task_data, task_id=task_id)
    updated_task = TaskSchema.from_orm(data_to_update).dict()
    return JSONResponse(content={"Task": updated_task})


@task_router.delete("tasks", response_model=TaskSchema)
def delete_task(task_id: int):
    TaskOrm.delete_task(task_id=task_id)
    return JSONResponse(content={"Task deleted"})
