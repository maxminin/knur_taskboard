from fastapi import APIRouter
from fastapi.responses import JSONResponse

from db.queries.user import UserORM
from utils.schemas.task import TaskSchema
from utils.schemas.user import UserSchema
from utils.pydatic_to_orm.user import pydantic_to_sqlalchemy


user_router = APIRouter(prefix="/users")


@user_router.get(
    "/",
    response_model=UserSchema
)
def get_users() -> JSONResponse:
    user_schemas = [
        UserSchema.
        from_orm(user).dict()
        for user in UserORM.get_users()
    ]
    return JSONResponse(content={"Users": user_schemas})


@user_router.get(
    "/{user_id}",
    response_model=UserSchema
)
def get_user_by_id(
        user_id: int
) -> JSONResponse:
    user = (
        UserSchema.
        from_orm(UserORM.get_user_by_id(user_id)).
        dict()
        )
    return JSONResponse(content={"User": user})


@user_router.post(
    "/create",
    response_model=UserSchema
)
def create_user(
        new_user: UserSchema
) -> JSONResponse:
    new_user_data = UserORM.create_user(
        pydantic_to_sqlalchemy(
            user=new_user
        )
    )
    new_user = UserSchema.from_orm(
        new_user_data
    ).dict()
    return JSONResponse(content={"new_user": new_user})


@user_router.put(
    "/update"
)
def update_user(
        user: dict,
        user_id: int
) -> JSONResponse:
    updated_user = UserSchema.from_orm(
        UserORM.update_user(
            user, user_id
        )
    ).dict()
    return JSONResponse(content={"updated_user": updated_user})


@user_router.delete(
    "   /delete"
)
def delete_user(
        user_id: int
) -> JSONResponse:
    UserORM.delete_user(user_id)
    return JSONResponse(content="User deleted")


@user_router.get("{user_id}/tasks")
def get_user_tasks(user_id: int) -> JSONResponse:
    user_tasks = UserORM.get_user_tasks(user_id=user_id)
    tasks_serializable = [TaskSchema.from_orm(task).dict() for task in user_tasks]
    return JSONResponse(content={"Tasks": tasks_serializable})

