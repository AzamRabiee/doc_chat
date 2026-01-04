import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from .constants import ALLOWED_TYPES, MAX_FILE_SIZE, MAX_TOTAL_SIZE

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    # Required settings
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    CANLII_API_KEY: str = os.getenv("CANLII_API_KEY", "")

    OPENAI_MODEL_NAME: str = "gpt-5.2-2025-12-11"

    # Optional settings with defaults
    MAX_FILE_SIZE: int = MAX_FILE_SIZE
    MAX_TOTAL_SIZE: int = MAX_TOTAL_SIZE
    ALLOWED_TYPES: list = ALLOWED_TYPES

    # Database settings
    CHROMA_DB_PATH: str = "./chroma_db"
    CHROMA_COLLECTION_NAME: str = "documents"

    # Retrieval settings
    VECTOR_SEARCH_K: int = 10
    HYBRID_RETRIEVER_WEIGHTS: list = [0.4, 0.6]

    # Logging settings
    LOG_LEVEL: str = "INFO"

    # New cache settings with type annotations
    CACHE_DIR: str = "document_cache"
    CACHE_EXPIRE_DAYS: int = 7

settings = Settings()
