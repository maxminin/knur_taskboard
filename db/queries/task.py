import sqlalchemy as sa

from db.db_connection import Session
from db.models.task import Task

class TaskOrm:

    @staticmethod
    def get_tasks() -> list[Task]:
        query = sa.select(Task)
        with Session() as session:
            result = session.scalars(query)
            return result
