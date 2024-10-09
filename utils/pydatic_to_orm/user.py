from db.models.user import User
from utils.schemas.user import UserSchema


def pydantic_to_sqlalchemy(user: UserSchema) -> User:
    user_in_db = User(**user.dict())
    return user_in_db
