from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    env: str
    log_level: str

    openai_api_key: str

    postgres_dsn: str
    redis_url: str

    class Config:
        env_file = ".env"


settings = Settings()
