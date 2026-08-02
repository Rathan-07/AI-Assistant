from app.tools.pdf_tool import PDFTool
from app.tools.tool_manager import ToolManager

tool_manager = ToolManager()

tool_manager.register(PDFTool())