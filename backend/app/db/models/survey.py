from sqlmodel import Field, SQLModel
from .base import BaseModel


class Survey(BaseModel, table=True):
    title: str
    description: str
