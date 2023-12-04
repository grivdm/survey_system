from __future__ import annotations
from sqlmodel import Field

from .base import BaseModel


class Option(BaseModel, table=True):
    question_id: int = Field(foreign_key="Question.id")
    text: str
