from app.tools.pdf_tool import PDFTool


class ToolRegistry:

    @staticmethod
    def get_tools():

        return [
            PDFTool(),
        ]