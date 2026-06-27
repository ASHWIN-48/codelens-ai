from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GROQ_API_KEY: str
    GOOGLE_API_KEY: str
    MONGO_URI: str
    FAISS_INDEX_PATH: str = "storage/index.faiss"
    CHUNKS_PATH: str = "storage/chunks.json"
    LANGCHAIN_API_KEY: str
    LANGCHAIN_TRACING_V2: str = "true"
    LANGCHAIN_PROJECT: str = "codelens"
    REPO_STORAGE_PATH: str = "storage/repo"

    MODEL_NAME: str = "llama-3.3-70b-versatile"
    APP_NAME: str = "CodeLens AI Service"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()