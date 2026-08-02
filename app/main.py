from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import logger
from app.services.llm_service import llm_service
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.on_event("startup")
async def startup():
    logger.info("Application Started")


# @app.get("/")
# async def home():
#     logger.info("Home endpoint called")

#     return {
#         "app": settings.APP_NAME,
#         "model": settings.MODEL_NAME,
#     }


@app.get("/")
async def home():

    response = await llm_service.generate_response(
        "Say Hello from Research Agent"
    )

    return {
        "response": response
    }