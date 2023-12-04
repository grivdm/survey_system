from sqlmodel import Field, SQLModel
from .base import BaseModel


class User(BaseModel, table=True):
    username: str
    email: str
    hashed_password: str
    salt_password: str
    is_active: bool = Field(default=True)
