from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    database_url: str = "sqlite:///./url_shortener.db"
    qr_code_api_url: str = "https://api.qr-code-generator.com/v1/create"

    class Config:
        env_file = ".env"
