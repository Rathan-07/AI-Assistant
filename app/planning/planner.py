
from app.planning.models import Plan
class Planner:

    async def create_plan(
        self,
        query: str,
    ) -> Plan:

        query = query.lower()

        if "pdf" in query:

            return Plan(
                use_tool=True,
                tool_name="pdf_reader",
                tool_arguments={
                    "file_path": "data/pdfs/sample.pdf"
                },
            )

        return Plan(
            use_tool=False
        )


planner = Planner()