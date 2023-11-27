import enum
from sqlmodel import Field, SQLModel


class QuestionType(str, enum.Enum):
    SINGLE_CHOICE = "single_choice"
    MULTIPLE_CHOICE = "multiple_choice"
    TEXT = "text"


class Question(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    survey_id: int = Field(foreign_key="survey.id")
    text: str
    type: QuestionType
