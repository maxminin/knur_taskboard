import sqlalchemy as sa

from sqlalchemy.orm import joinedload

from db.db_connection import Session
from db.models.task import Task
from db.models.user import User


class TaskOrm:

    @staticmethod
    def get_tasks() -> list[Task]:
        query = sa.select(Task)
        with Session() as session:
            result = session.scalars(query)
            return result.all()

    @staticmethod
    def get_task_by_id(
            task_id: id
    ) -> Task:
        query = (
            sa.select(Task)
            .where(Task.id == task_id)
        )
        with Session() as session:
            user = session.scalar(query)
            return user

    @staticmethod
    def create_task(
            new_task: Task
    ) -> Task:
        with Session() as session:
            session.add(new_task)
            session.commit()
            session.refresh(new_task)
            return new_task

    @staticmethod
    def update_task(
            data: dict,
            task_id: int
    ) -> Task:
        query = (
            sa.update(Task)
            .where(Task.id == task_id)
            .values(**data)
        )
        with Session() as session:
            session.execute(query)
            session.commit()
            updated_task = TaskOrm.get_task_by_id(task_id)
            return updated_task

    @staticmethod
    def delete_task(
            task_id: int
    ) -> None:
        query = (
            sa.delete(Task)
            .where(Task.id == task_id)
        )
        with Session() as session:
            session.execute(query)
            session.commit()
