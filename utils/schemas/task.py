from .base import BaseIdSchema


class TaskSchema(BaseIdSchema):
    title: str
    is_done: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True
        from_attributes = True
