import sqlalchemy as sa

from db.db_connection import Session
from db.models.task import Task
from db.models.user import User
from utils.schemas.user import UserSchema


class UserORM:

    @staticmethod
    def get_users() -> list[User]:
        query = sa.select(User)
        with Session() as session:
            result = session.scalars(query)
            return result.all()

    @staticmethod
    def get_user_by_id(
            user_id: int
    ) -> User:
        query = (
            sa.select(User)
            .where(User.id == user_id)
        )
        with Session() as session:
            user = session.scalar(query)
            return user

    @staticmethod
    def create_user(
            new_user: User
    ) -> User:
        with Session() as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user

    @staticmethod
    def update_user(
            user_data: dict,
            user_id: int
    ) -> User:
        query = (
            sa.update(User)
            .where(User.id == user_id).
            values(**user_data)
        )
        with Session() as session:
            session.execute(query)
            session.commit()
            updated_user = UserORM.get_user_by_id(user_id)
            return updated_user

    @staticmethod
    def delete_user(
            user_id: int
    ) -> None:
        query = (
            sa.delete(User).
            where(User.id == user_id)
        )
        with Session() as session:
            session.execute(query)
            session.commit()

    @staticmethod
    def get_user_tasks(
            user_id: int
    ) -> list[Task]:
        query = sa.select(User).where(User.id == user_id)
        with Session() as session:
            user_tasks = session.scalar(query).tasks
            return user_tasks
