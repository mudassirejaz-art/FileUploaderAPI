import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .database import Base, engine
from .models import FileRecord   # <-- ensure model loads
from .config import settings
from .routers import files as files_router

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Snake File Uploader API",
    version="1.0.0",
    description="Upload any file (images, videos, docs). Browse, download, delete.",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure upload dir exists
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

# Static mounts
app.mount("/public", StaticFiles(directory=settings.UPLOAD_DIR), name="public")
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# API routes
app.include_router(files_router.router)

@app.get("/", tags=["health"], include_in_schema=False)
def root():
    return FileResponse("frontend/index.html")
