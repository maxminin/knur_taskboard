from sqlalchemy.orm import Mapped, mapped_column, declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(
        primary_key=True,
        sort_order=-1,
        autoincrement=True
    )
