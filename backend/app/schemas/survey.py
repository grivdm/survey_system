from datetime import datetime
from pydantic import BaseModel


class SurveyBase(BaseModel):
    title: str
    description: str


class SurveyCreate(SurveyBase):
    pass


class SurveyUpdate(SurveyBase):
    pass


class SurveyRead(SurveyBase):
    id: int

class SurveyDelete(SurveyBase):
    pass