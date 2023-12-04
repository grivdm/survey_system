from typing import Sequence
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.schemas.survey import SurveyCreate, SurveyRead, SurveyUpdate
from app.services.survey_service import survey
from app.db.session import get_session

router = APIRouter()


@router.post("/", response_model=SurveyRead, status_code=201)
async def create_survey(survey_create: SurveyCreate,
                                db: AsyncSession = Depends(get_session)):
    return await survey.create(db, obj_in=survey_create)


@router.put("/{survey_id}", response_model=SurveyRead)
async def update_survey(survey_id: int, survey_update: SurveyUpdate,
                                db: AsyncSession = Depends(get_session)):
    return await survey.update(db, id=survey_id, obj_in=survey_update)


@router.get("/{survey_id}", response_model=SurveyRead)
async def read_survey(survey_id: int, db: AsyncSession = Depends(get_session)):
    return await survey.read(db, survey_id)


@router.get("/", response_model=Sequence[SurveyRead])
async def read_all_surveys(db: AsyncSession = Depends(get_session)):
    return await survey.read_all(db)


@router.delete('/{survey_id}')
async def delete_survey_handler(survey_id: int, db: AsyncSession = Depends(get_session)):
    return await survey.delete(db, id=survey_id)