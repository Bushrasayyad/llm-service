from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    groq_api_key: str
    default_model: str = "openai/gpt-oss-20b"
    max_tokens: int = 500
    request_timeout: int = 60

    class Config:
        env_file = ".env"

settings = Settings()