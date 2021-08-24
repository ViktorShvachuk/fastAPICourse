import os
from pathlib import Path
from dotenv import load_dotenv
from jose.constants import ALGORITHMS

env_path = Path('.') / '.env'
load_dotenv(env_path)


class Settings:
    PROJECT_TITLE: str = "Job board"
    PROJECT_VERSION: str = "0.1.0"

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER', 'localhost')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT', 5432)
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', "db_course")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRES_IN_MINUTES = 30

settings = Settings()
