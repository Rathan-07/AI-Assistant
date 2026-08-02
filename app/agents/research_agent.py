from app.chains.research_chain import research_chain
from app.core.logger import logger
from app.planning.planner import planner
from app.tools import tool_manager
from app.tools.models import ToolRequest


class ResearchAgent:

    async def execute(
        self,
        query: str,
    ) -> str:

        logger.info("Planning...")

        plan = await planner.create_plan(query)

        context = ""

        if plan.use_tool:

            logger.info(f"Using tool: {plan.tool_name}")

            result = await tool_manager.execute(

                ToolRequest(
                    tool_name=plan.tool_name,
                    arguments=plan.tool_arguments,
                )

            )

            if result.success:

                context = result.data

        logger.info("Calling Research Chain")

        return await research_chain.invoke(
            query=query,
            context=context,
        )


research_agent = ResearchAgent()