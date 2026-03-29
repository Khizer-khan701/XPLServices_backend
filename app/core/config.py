from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # OpenAI
    OPENAI_API_KEY: str

    # LLMs
    GEMINI_API_KEY: str
    OPENROUTER_API_KEY: str


    # Database
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()