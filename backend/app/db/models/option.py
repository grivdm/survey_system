from sqlmodel import Field, SQLModel


class Option(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    question_id: int = Field(foreign_key="question.id")
    text: str
