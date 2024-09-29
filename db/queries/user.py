from sqlalchemy.orm import joinedload
import sqlalchemy as sa

from db.db_connection import Session
from db.models.user import User


class UserORM:

    @staticmethod
    def get_users() -> list[User]:
        """
        Example
        """
        query = sa.select(User)
        with Session() as session:
            result = session.scalars(query)
            return result.all()

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        with Session() as session:
            user = session.query(User).options(
                joinedload(User.tasks)
            ).filter(
                User.id == user_id
            ).first()
            return user

    @staticmethod
    def create_user(data: dict) -> User:
        new_user = User(**data)
        with Session() as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user
