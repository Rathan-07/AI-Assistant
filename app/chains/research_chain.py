from app.chains.base_chain import BaseChain
from app.prompts.research_prompt import RESEARCH_PROMPT


class ResearchChain(BaseChain):
    def __init__(self):
        super().__init__(RESEARCH_PROMPT)


research_chain = ResearchChain()