from .base import BaseIdSchema


class UserSchema(BaseIdSchema):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True
        from_attributes = True
