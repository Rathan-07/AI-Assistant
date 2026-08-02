from fastapi import APIRouter

from app.agents.research_agent import research_agent
from app.schemas.research import (
    ResearchRequest,
    ResearchResponse,
)

router = APIRouter(
    prefix="/research",
    tags=["Research"],
)


@router.post(
    "",
    response_model=ResearchResponse,
)
async def research(
    request: ResearchRequest,
):

    answer = await research_agent.execute(
        query=request.query
    )

    return ResearchResponse(
        answer=answer
    )