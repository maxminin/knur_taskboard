from fastapi import APIRouter

from db.queries.user import UserORM
from utils.schemas.user import UserSchema

user_router = APIRouter()


@user_router.get("/users", response_model=UserSchema)
def get_users() -> list[UserSchema]:
    users = UserORM.get_users()
    return users


@user_router.get("/users/{user_id}", response_model=UserSchema)
def get_user_by_id(user_id) -> UserSchema:
    user = (UserORM.
            get_user_by_id(user_id=user_id))
    return user


@user_router.post("/users", response_model=UserSchema)
def create_user(user: UserSchema) -> UserSchema:
    user = (UserORM.
            create_user(data=user.dict()))
    return user


@user_router.put("/users", response_model=UserSchema)
def update_user(user: UserSchema) -> UserSchema:
    updated_user = (UserORM.
                    update_user(data=user.dict()))
    return updated_user


@user_router.delete("/users", response_model=UserSchema)
def delete_user(user_id: int) -> None:
    user = (UserORM.
            delete_user(user_id=user_id))
    return user
