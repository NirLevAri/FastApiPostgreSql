import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgres://user:pass@localhost:5432/mydb")

settings = Settings()
