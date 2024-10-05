from fastapi import APIRouter
from fastapi.responses import JSONResponse

from db.queries.user import UserORM
from utils.schemas.user import UserSchema
from db.models.user import User


user_router = APIRouter()


@user_router.get(
    "/users",
    response_model=UserSchema
)
def get_users() -> JSONResponse:
    users = UserORM.get_users()
    return JSONResponse(content={"Users": users})


@user_router.get(
    "/users/{user_id}"
)
def get_user_by_id(
        user_id: int
) -> JSONResponse:
    user = UserORM.get_user_by_id(user_id)
    return JSONResponse(content={"User": user})


@user_router.post(
    "/users/create"
)
def create_user(
        new_user: User
) -> JSONResponse:
    new_user = UserORM.create_user(new_user)
    return JSONResponse(content={"new_user": new_user})


@user_router.put(
    "/users/update"
)
def update_user(
        user: dict,
        user_id: int
) -> JSONResponse:
    updated_user = UserORM.update_user(user, user_id)
    return JSONResponse(content={"updated_user": updated_user})


@user_router.delete(
    "/users/delete"
)
def delete_user(
        user_id: int
) -> JSONResponse:
    UserORM.delete_user(user_id)
    return JSONResponse(content="User deleted")
