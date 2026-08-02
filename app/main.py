from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
async def home():
    return {
        "app": settings.APP_NAME,
        "model": settings.MODEL_NAME,
        "version": settings.APP_VERSION,
    }