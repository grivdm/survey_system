from sqlmodel import SQLModel
from typing import List

from .response import Response
from .base import BaseModel


class Result(BaseModel):
    survey_id: int
    responses: List[Response]
