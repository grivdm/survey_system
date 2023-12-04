from sqlmodel import Field, SQLModel
from typing import Optional

from .base import BaseModel


class Response(BaseModel, table=True):
    user_id: int = Field(foreign_key="User.id")
    question_id: int = Field(foreign_key="Question.id")
    answer_text: Optional[str] = None
