from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    APP_NAME: str = "Research Agent"
    APP_VERSION: str = "1.0.0"

    # OpenAI
    OPENAI_API_KEY: str
    MODEL_NAME: str = "gpt-4.1-mini"
    TEMPERATURE: float = 0.2

    # Directories
    CHROMA_DB_PATH: str = "./db"
    REPORT_PATH: str = "./reports"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()



# Why @lru_cache?
# @lru_cache
# def get_settings():

# It creates the Settings object once and reuses it throughout the application.

# Without it:

# Every import would reload the .env file.