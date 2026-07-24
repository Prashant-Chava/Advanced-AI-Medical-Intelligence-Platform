import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import router
from app.database.database import Base, engine
import app.database.models

# Create database tables
Base.metadata.create_all(bind=engine)

# Create required directories
os.makedirs("reports", exist_ok=True)
os.makedirs("uploads", exist_ok=True)

# Create FastAPI app
app = FastAPI(
    title="Medical Image Analysis API",
    version="1.0",
)

# Include routes
app.include_router(router)

# Mount static files
app.mount(
    "/reports",
    StaticFiles(directory="reports"),
    name="reports",
)