from sqlmodel import SQLModel
from typing import List

from response import Response


class Result(SQLModel):
    survey_id: int
    responses: List[Response]
