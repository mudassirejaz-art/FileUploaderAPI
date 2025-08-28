import os
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import FileRecord
from ..config import settings

router = APIRouter(prefix="/api/files", tags=["files"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_files(db: Session = Depends(get_db)):
    return db.query(FileRecord).all()

@router.post("/upload")
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = os.path.join(settings.UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(file.file.read())

    record = FileRecord(
        filename=file.filename,
        filepath=file_location,
        content_type=file.content_type,
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return {"status": "uploaded", "file": record}

@router.delete("/{file_id}")
def delete_file(file_id: int, db: Session = Depends(get_db)):
    record = db.query(FileRecord).filter(FileRecord.id == file_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="File not found")

    if os.path.exists(record.filepath):
        os.remove(record.filepath)

    db.delete(record)
    db.commit()
    return {"status": "deleted", "id": file_id}
