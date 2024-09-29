from .base import BaseIdSchema
from .task import TaskSchema


class UserSchema(BaseIdSchema):
    username: str
    email: str
    password: str
    tasks: [list[TaskSchema | None]]


