from fastapi import FastAPI

from db.setup import setup_db
from core.routers.user import user_router

setup_db()

app = FastAPI()

app.include_router(user_router)