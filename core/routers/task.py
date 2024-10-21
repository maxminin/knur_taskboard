from fastapi import APIRouter
from fastapi.responses import JSONResponse

from db.queries.task import TaskOrm
from utils.schemas.task import TaskSchema, InputTaskSchema
from utils.pydatic_to_orm.task import pydantic_to_sqlalchemy
from utils.schemas.user import UserSchema

task_router = APIRouter(prefix="/tasks")


@task_router.get(
    "/",
    response_model=TaskSchema
)
def get_tasks() -> JSONResponse:
    task_schemas = [
        TaskSchema.
        from_orm(task).dict()
        for task in TaskOrm.get_tasks()
    ]
    return JSONResponse(content={"Tasks": task_schemas})


@task_router.get(
    "/{task_id}",
    response_model=TaskSchema
)
def get_task_by_id(
        task_id: int
) -> JSONResponse:
    task = TaskSchema.from_orm(
        TaskOrm.get_task_by_id(
            task_id
        )).dict()
    return JSONResponse(content={"Task": task})


@task_router.post(
    "/create",
    response_model=TaskSchema
)
def create_task(
        new_task: InputTaskSchema
) -> JSONResponse:
    new_task_data = TaskOrm.create_task(
        pydantic_to_sqlalchemy(
            task=new_task
        )
    )
    new_task = (
        TaskSchema.
        from_orm(new_task_data)
        .dict()
    )
    return JSONResponse(content={"Task": new_task})


@task_router.put(
    "/update",
    response_model=TaskSchema
)
def update_task(
        task_data: dict,
        task_id: int
) -> JSONResponse:
    updated_task = TaskSchema.from_orm(
        TaskOrm.update_task(
            data=task_data,
            task_id=task_id
        )
    ).dict()
    return JSONResponse(content={"Task": updated_task})


@task_router.delete(
    "/delete",
    response_model=TaskSchema
)
def delete_task(
        task_id: int
) -> JSONResponse:
    TaskOrm.delete_task(task_id=task_id)
    return JSONResponse(content="Task deleted")

