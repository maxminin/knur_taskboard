from .base import BaseIdSchema
from .task import TaskSchema

from typing import Optional, List


class UserSchema(BaseIdSchema):
    username: str
    email: str
    password: str
    tasks: Optional[List[TaskSchema]]


