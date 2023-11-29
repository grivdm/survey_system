import os
from sqlalchemy import URL


class Settings:
    DATABASE_URL: str | URL = os.getenv("DATABASE_URL", "default_database_url")


settings = Settings()
