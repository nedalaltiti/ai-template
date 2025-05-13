# settings.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Template"
    debug: bool = False

settings = Settings()