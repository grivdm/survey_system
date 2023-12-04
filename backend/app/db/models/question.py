import enum
from sqlmodel import Field

from .base import BaseModel


class QuestionType(str, enum.Enum):
    SINGLE_CHOICE = "single_choice"
    MULTIPLE_CHOICE = "multiple_choice"
    TEXT = "text"


class Question(BaseModel, table=True):
    survey_id: int = Field(foreign_key="Survey.id")
    text: str
    type: QuestionType
    duration_min: int
