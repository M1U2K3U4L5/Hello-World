from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Indian Stock Analysis Platform"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/stock_platform"
    allowed_origins: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
