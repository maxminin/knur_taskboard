from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from db.models.base_model import BaseModel


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
    tasks: Mapped[list["Task"]] = relationship(
        'Task',
        back_populates='user'
    )