from fastapi import FastAPI

from db.setup import setup_db
from core.routers.user import user_router
from core.routers.task import task_router

setup_db()

app = FastAPI()

app.include_router(user_router)
app.include_router(task_router)