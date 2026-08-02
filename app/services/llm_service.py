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

        logger.info("LLM initialized")

    async def generate_response(
        self,
        prompt: str,
    ) -> str:

        logger.info("Sending request to LLM")

        response = await self.llm.ainvoke(prompt)

        logger.info("Received response from LLM")

        return response.content


llm_service = LLMService()