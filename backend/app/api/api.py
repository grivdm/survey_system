from fastapi import APIRouter

from .endpoints import surveys


api_router = APIRouter()

api_router.include_router(
    surveys.router, prefix="/surveys", tags=["surveys"])
