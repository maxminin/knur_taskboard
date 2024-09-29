from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

from db.models.base_model import BaseModel
from db.models.task import Task


class User(BaseModel):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )
    password: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )
    task_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("task.id")
    )
    tasks: Mapped[List["Task"]] = relationship(
        "Task",
        back_populates="user"
    )
