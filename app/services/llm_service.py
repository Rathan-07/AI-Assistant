from langchain_anthropic import ChatAnthropic

from app.core.config import settings
from app.core.logger import logger


class LLMService:
    def __init__(self):
        self.llm = ChatAnthropic(
            model=settings.MODEL_NAME,
            temperature=settings.TEMPERATURE,
            api_key=settings.ANTHROPIC_API_KEY,
        )

        logger.info("Claude LLM initialized")

    def get_llm(self) -> ChatAnthropic:
        return self.llm


llm_service = LLMService()