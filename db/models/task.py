import datetime

from db.models.base_model import BaseModel
from db.models.user import User

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, DateTime


class Task(BaseModel):
    __tablename__ = "task"

    title: Mapped[str] = mapped_column(
        String(2000),
        nullable=False
    )
    is_done: Mapped[bool] = mapped_column(
        default=False,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("user.id")
    )
    user: Mapped['User'] = relationship(
        "User",
        back_populates="tasks"
    )
