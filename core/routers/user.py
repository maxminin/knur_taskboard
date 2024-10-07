from fastapi import APIRouter
from fastapi.responses import JSONResponse

from db.queries.user import UserORM
from utils.schemas.user import UserSchema
from utils.pydatic_to_orm.user import pydantic_to_sqlalchemy


user_router = APIRouter()


@user_router.get(
    "/users",
    response_model=UserSchema
)
def get_users() -> JSONResponse:
    users = UserORM.get_users()
    user_schemas = [
        UserSchema.
        from_orm(user).dict()
        for user in users
    ]
    return JSONResponse(
        content={
            "Users": user_schemas
        }
    )


@user_router.get(
    "/users/{user_id}",
    response_model=UserSchema
)
def get_user_by_id(
        user_id: int
) -> JSONResponse:
    user_data = UserORM.get_user_by_id(user_id)
    user = (
        UserSchema.
        from_orm(user_data).
        dict()
        )
    return JSONResponse(
        content={
            "User": user
        }
    )


@user_router.post(
    "/users/create",
    response_model=UserSchema
)
def create_user(
        new_user: UserSchema
) -> JSONResponse:
    new_user_data = (UserORM.
                     create_user(
                        pydantic_to_sqlalchemy(user=new_user)
                     ))
    new_user = (UserSchema.
                from_orm(new_user_data).
                dict())
    return JSONResponse(
        content={
            "new_user": new_user
        }
    )


@user_router.put(
    "/users/update"
)
def update_user(
        user: dict,
        user_id: int
) -> JSONResponse:
    updated_user_data = UserORM.update_user(user, user_id)
    updated_user = (UserSchema.
                    from_orm(updated_user_data)
                    .dict())
    return JSONResponse(
        content={
            "updated_user": updated_user
        }
    )


@user_router.delete(
    "/users/delete"
)
def delete_user(
        user_id: int
) -> JSONResponse:
    UserORM.delete_user(user_id)
    return JSONResponse(
        content="User deleted"
    )
