from db.models.task import Task
from utils.schemas.task import InputTaskSchema


def pydantic_to_sqlalchemy(task: InputTaskSchema):
    task_in_db = Task(**task.dict())
    return task_in_db
