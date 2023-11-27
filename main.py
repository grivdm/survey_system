from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from db.session import get_session


app = FastAPI()


@app.get("/test_db")
async def test_db_connection(db: AsyncSession = Depends(get_session)):
    try:
        result = await db.execute(text("SELECT 1"))
        return {"db_test": True, "result": result.scalar_one()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
