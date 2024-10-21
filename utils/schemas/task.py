from datetime import datetime

from .base import BaseIdSchema


class TaskSchema(BaseIdSchema):
    title: str
    is_done: bool
    user_id: int

    class Config:
        orm_mode = True
        from_attributes = True


class InputTaskSchema(TaskSchema):
    created_at: datetime
    updated_at: datetime
