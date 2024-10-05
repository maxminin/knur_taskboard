import sqlalchemy as sa

from fastapi import Response

from db.db_connection import Session
from db.models.user import User


class UserORM:

    @staticmethod
    def get_users() -> list[User]:
        query = sa.select(User)
        with Session() as session:
            result = session.scalars(query)
            return result.all()

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        query = (sa.select(User)
                 .where(User.id == user_id))

        with Session() as session:
            user = session.scalar(query)
            return user

    @staticmethod
    def create_user(data: dict) -> User:
        new_user = User(**data)

        with Session() as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user

    @staticmethod
    def update_user(data: dict) -> User:
        user_id = data.get('id')
        query = (sa.update(User).
                 where(User.id == user_id).
                 values(data))

        with Session() as session:
            session.execute(query)
            session.commit()
            updated_user = (session.
                            scalar(sa.select(User).
                                   where(User.id == user_id)))
            return updated_user

    @staticmethod
    def delete_user(user_id): #tut ne jebu type hint
        query = (sa.delete(User).
                 where(User.id == user_id))
        with Session() as session:
            session.execute(query)
            session.commit()
            return Response(content="200 OK") #jebu kak tut response postroitb
