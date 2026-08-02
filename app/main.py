from fastapi import FastAPI

from app.api.research import router as research_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(research_router)