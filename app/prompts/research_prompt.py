from langchain_core.prompts import ChatPromptTemplate


RESEARCH_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert AI Research Assistant.

Use the provided context if available.
If context is empty, answer using your own knowledge.
"""
        ),
        (
            "human",
            """
Question:

{query}

Context:

{context}
"""
        ),
    ]
)