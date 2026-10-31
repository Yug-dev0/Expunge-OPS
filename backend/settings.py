import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = os.getenv("EXPUNGEOPS_DATABASE_URL") or os.getenv("ERASEOPS_DATABASE_URL") or "postgresql+psycopg://eraseops:eraseops_local_only@localhost:5432/eraseops"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="EXPUNGEOPS_", extra="ignore")


settings = Settings()
