from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

env_from = Path(".") / ".env"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="NA_USERMGMT_", env_file=env_from)
    
    POSTGRES_DB: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    
    PROJECT_TITLE: str
    PROJECT_VERSION: str


settings = Settings()