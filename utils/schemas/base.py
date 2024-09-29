from abc import ABC

from pydantic import BaseModel


class BaseIdSchema(BaseModel, ABC):
    id: int
