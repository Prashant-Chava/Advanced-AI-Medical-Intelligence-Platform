from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import router

from app.database.database import Base
from app.database.database import engine

import app.database.models


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Medical Image Analysis API",
    version="1.0",
)

app.include_router(router)

app.mount(
    "/reports",
    StaticFiles(directory="reports"),
    name="reports",
)