import os
from dotenv import load_dotenv
from sqlalchemy import URL


load_dotenv()


class Settings:
    DATABASE_URL: str | URL = os.getenv("DATABASE_URL", "default_database_url")


settings = Settings()
