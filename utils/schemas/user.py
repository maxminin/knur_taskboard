from .base import BaseIdSchema


class UserSchema(BaseIdSchema):
    username: str
    email: str
    password: str
