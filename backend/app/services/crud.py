from typing import Generic, Optional, Sequence, Type, TypeVar
from sqlmodel import SQLModel, select
from app.db.models.base import BaseModel as BaseDBModel
from pydantic import BaseModel
from sqlmodel.ext.asyncio.session import AsyncSession


ModelType = TypeVar("ModelType", bound=BaseDBModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, db: AsyncSession, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def read(self, db: AsyncSession, id: int) -> Optional[ModelType]:
        result = await db.exec(select(self.model).where(self.model.id == id))
        return result.one_or_none()

    async def read_all(self, db: AsyncSession) -> Sequence[ModelType]:
        result = await db.exec(select(self.model))
        return result.all()

    async def update(self, db: AsyncSession, *, id: int, obj_in: UpdateSchemaType) -> Optional[ModelType]:
        db_obj = await self.read(db, id)
        if db_obj:
            update_data = obj_in.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_obj, key, value)
            db.add(db_obj)
            await db.commit()
            await db.refresh(db_obj)
            return db_obj
        return None

    async def delete(self, db: AsyncSession, *, id: int) -> bool:
        db_obj = await self.read(db, id)
        if db_obj:
            await db.delete(db_obj)
            await db.commit()
            return True
        return False
