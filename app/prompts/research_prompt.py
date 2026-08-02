from langchain_core.prompts import ChatPromptTemplate


RESEARCH_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert AI Research Assistant.

Your responsibilities:
- Answer accurately.
- Be concise.
- Explain step-by-step when required.
- If information is uncertain, clearly mention it.
- Use markdown formatting where appropriate.
"""
        ),
        (
            "human",
            "{query}"
        ),
    ]
)