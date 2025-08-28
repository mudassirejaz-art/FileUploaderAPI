import os
import shutil
import hashlib
import uuid
from typing import Tuple, Optional
from fastapi import HTTPException, UploadFile, status
from .config import settings

def ensure_upload_dir(subdir: Optional[str] = None) -> str:
    base = settings.UPLOAD_DIR
    path = os.path.join(base, subdir) if subdir else base
    os.makedirs(path, exist_ok=True)
    return path

def generate_stored_name(original: str) -> str:
    # keep extension
    ext = ""
    if "." in original:
        ext = "." + original.rsplit(".", 1)[1]
    return f"{uuid.uuid4().hex}{ext}"

def validate_file_type(content_type: Optional[str]):
    if settings.ALLOW_ALL_TYPES:
        return
    if not content_type:
        raise HTTPException(status_code=415, detail="Unknown content-type")
    ok = any(content_type.startswith(prefix) for prefix in settings.ALLOWED_MIME_PREFIXES)
    if not ok:
        raise HTTPException(
            status_code=415,
            detail=f"Unsupported type: {content_type}. Allowed prefixes: {list(settings.ALLOWED_MIME_PREFIXES)}",
        )

def max_bytes() -> int:
    return settings.MAX_FILE_SIZE_MB * 1024 * 1024

async def save_upload_stream(file: UploadFile, dst_path: str) -> Tuple[int, str]:
    """
    Streams to disk in chunks; returns (size_bytes, sha256_hex)
    """
    hasher = hashlib.sha256()
    total = 0
    with open(dst_path, "wb") as out:
        while True:
            chunk = await file.read(1024 * 1024)  # 1MB chunks
            if not chunk:
                break
            total += len(chunk)
            if total > max_bytes():
                try:
                    out.close()
                    os.remove(dst_path)
                except Exception:
                    pass
                raise HTTPException(status_code=413, detail="File too large")
            hasher.update(chunk)
            out.write(chunk)
    return total, hasher.hexdigest()

def delete_file_silent(path: str):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
