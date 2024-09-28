from .base import BaseIdSchema

from .user import UserSchema


class TaskSchema(BaseIdSchema):
    title: str
    is_done: str
    created_at: str
    updated_at: str
    user: UserSchema
