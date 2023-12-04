from typing import Optional, Sequence
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.models.question import Question
from sqlmodel import select


class QuestionService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_question(self, question_data: Question) -> Question:
        self.db.add(question_data)
        await self.db.commit()
        await self.db.refresh(question_data)
        return question_data

    async def get_question(self, question_id: int) -> Optional[Question]:
        result = await self.db.exec(select(Question).where(Question.id == question_id))
        return result.first()

    async def get_all_questions(self) -> Sequence[Question]:
        result = await self.db.exec(select(Question))
        return result.all()

