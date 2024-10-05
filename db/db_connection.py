from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLITE_URL = "sqlite:///test_knur.db"

engine = create_engine(
    SQLITE_URL,
    echo=True
)

Session = sessionmaker(
    bind=engine
)
