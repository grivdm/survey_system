from sqlmodel import SQLModel as _SQLModel, Field
from sqlalchemy.orm import declared_attr
from datetime import datetime


class SQLModel(_SQLModel):
    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__


class BaseModel(SQLModel):
    id: int = Field(default=None, primary_key=True)
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={
            "onupdate": datetime.utcnow}
    )
    created_at: datetime | None = Field(default_factory=datetime.utcnow)
