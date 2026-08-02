from app.tools.base import BaseTool
from app.tools.models import ToolRequest, ToolResponse
from app.tools.registry import ToolRegistry

class ToolManager:

    def __init__(self):
        self._tools: dict[str, BaseTool] = {}
        for tool in ToolRegistry.get_tools():
            self.register(tool)

    def register(self, tool: BaseTool):

        self._tools[tool.name] = tool

    def get(self, tool_name: str) -> BaseTool:
        return self._tools[tool_name]

    async def execute(
        self,
        request: ToolRequest,
    ):

        tool = self.get(request.tool_name)

        tool_response =  await tool.execute(
            **request.arguments
        )

        return tool_response


# **kwargs in a function definition collects keyword arguments into a dictionary.
# **dictionary in a function call unpacks a dictionary into keyword arguments.