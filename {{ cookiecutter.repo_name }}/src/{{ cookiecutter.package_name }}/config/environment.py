# Env loader
from pydantic import BaseSettings
from typing import Literal
import os

class EnvironmentSettings(BaseSettings):
    environment: Literal["dev", "prod", "test"] = "dev"
    debug: bool = False
    database_url: str = "sqlite:///./app.db"
    api_key: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Load settings based on environment variable, default to dev
ENV = os.getenv("APP_ENV", "dev")
settings = EnvironmentSettings(_env_file=f".env.{ENV}" if os.path.exists(f".env.{ENV}") else ".env")
