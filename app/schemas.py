from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class FileOut(BaseModel):
    id: int
    original_filename: str
    stored_filename: str
    content_type: Optional[str] = None
    size_bytes: int
    sha256: Optional[str] = None
    uploaded_at: datetime
    subdir: Optional[str] = None
    url_view: str = Field(..., description="Browser-viewable URL")
    url_download: str = Field(..., description="Direct download URL")

    class Config:
        from_attributes = True

class FilesPage(BaseModel):
    total: int
    items: List[FileOut]
