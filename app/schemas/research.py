from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=3,
        description="Research query"
    )


class ResearchResponse(BaseModel):
    answer: str