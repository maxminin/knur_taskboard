from db.models.task import Task
from utils.schemas.task import TaskSchema


def pydantic_to_sqlalchemy(task: TaskSchema):
    task_in_db = Task(**task.dict())
    return task_in_db
