from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional


class Survey(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
