import os
from pydantic import BaseModel
from typing import Set

class Settings(BaseModel):
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "uploads")
    MAX_FILE_SIZE_MB: int = int(os.getenv("MAX_FILE_SIZE_MB", "100"))
    ALLOWED_MIME_PREFIXES: Set[str] = set(
        os.getenv("ALLOWED_MIME_PREFIXES", "image/,video/,application/pdf").split(",")
    )
    ALLOW_ALL_TYPES: bool = os.getenv("ALLOW_ALL_TYPES", "").strip() == "*"
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "*")

settings = Settings()
