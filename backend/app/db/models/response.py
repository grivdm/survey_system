from sqlmodel import Field, SQLModel
from typing import Optional


class Response(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    question_id: int = Field(foreign_key="question.id")
    answer_text: Optional[str] = None
