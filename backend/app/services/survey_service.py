from .crud import CRUDBase
from app.db.models import Survey
from app.schemas.survey import SurveyCreate, SurveyUpdate

class CRUDSurvey(CRUDBase[Survey, SurveyCreate, SurveyUpdate]):
    pass

survey = CRUDSurvey(Survey)