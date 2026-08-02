from typing import Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.services.llm_service import llm_service


class BaseChain:
    def __init__(self, prompt: ChatPromptTemplate,parser=None):
        self.chain = (
            prompt
            | llm_service.get_llm()
            |  (parser or StrOutputParser())
        )

    async def invoke(self, **kwargs: Any) -> str:
        return await self.chain.ainvoke(kwargs)