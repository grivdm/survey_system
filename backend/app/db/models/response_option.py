from __future__ import annotations
from sqlmodel import Field

from .base import BaseModel


class ResponseOption(BaseModel, table=True):
    response_id: int = Field(foreign_key="Response.id")
    option_id: int = Field(foreign_key="Option.id")
