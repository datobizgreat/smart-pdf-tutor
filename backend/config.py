"""
Configuration settings for Smart PDF Tutor
"""

from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # API Settings
    api_title: str = "Smart PDF Tutor"
    api_version: str = "0.1.0"
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # Database Settings
    database_url: Optional[str] = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost/smartpdf"
    )
    
    # OpenAI Settings
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    # Vector Database Settings
    faiss_index_path: str = os.getenv("FAISS_INDEX_PATH", "./data/faiss_index")
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "500"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", "50"))
    
    # File Upload Settings
    max_file_size_mb: int = int(os.getenv("MAX_FILE_SIZE_MB", "50"))
    upload_directory: str = os.getenv("UPLOAD_DIRECTORY", "./uploads")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Create settings instance
settings = Settings()
