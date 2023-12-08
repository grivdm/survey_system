from typing import Sequence
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.schemas.survey import SurveyCreate, SurveyRead, SurveyUpdate
from app.services import survey
from app.db.session import get_session
from app.core.utils import handle_response
from backend.app.core.exceptions import NotFoundException


router = APIRouter()


@router.post("/", response_model=SurveyRead, status_code=201)
async def create_survey(survey_create: SurveyCreate,
                        db: AsyncSession = Depends(get_session)):

    return await survey.create(db, obj_in=survey_create)


@router.put("/{survey_id}", response_model=SurveyRead)
async def update_survey(survey_id: int, survey_update: SurveyUpdate,
                        db: AsyncSession = Depends(get_session)):
    res = await survey.update(db, id=survey_id, obj_in=survey_update)
    if res is None:
            raise NotFoundException(f"Survey with id {survey_id} not found")
    return res


@router.get("/{survey_id}", response_model=SurveyRead)
async def read_survey(survey_id: int, db: AsyncSession = Depends(get_session)):
    res = await survey.read(db, survey_id)
    if res is None:
        raise NotFoundException(f"Survey with id {survey_id} not found")
    return res


@router.get("/", response_model=Sequence[SurveyRead])
async def read_all_surveys(db: AsyncSession = Depends(get_session)):
    return await survey.read_all(db)


@router.delete('/{survey_id}')
async def delete_survey(survey_id: int, db: AsyncSession = Depends(get_session)):
    res = await survey.delete(db, id=survey_id)
    if res is None:
        raise NotFoundException(f"Survey with id {survey_id} not found")
    return res
