from db.models import base_model
from db.db_connection import engine


def setup_db():
    base_model.BaseModel.metadata.create_all(
        bind=engine
    )