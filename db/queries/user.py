import sqlalchemy as sa

from db.db_connection import Session
from db.models.user import User


class UserORM:

    @staticmethod
    def get_users() -> list[User]:
        query = sa.select(User)
        with Session() as session:
            result = session.execute(query)
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
            return user.first()

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
            user: dict,
            user_id: int
    ) -> User:
        query = (
            sa.update(User)
            .where(User.id == user_id).
             values(user)
        )
        with Session() as session:
            session.execute(query)
            session.commit()
            session.refresh()
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
