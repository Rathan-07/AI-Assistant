from langchain_community.document_loaders import PyPDFLoader

from app.core.logger import logger
from app.tools.base import BaseTool
from app.tools.models import ToolResponse


class PDFTool(BaseTool):

    name = "pdf_reader"

    description = "Read PDF content."

    async def execute(
        self,
        file_path: str,
    ) -> ToolResponse:

        logger.info(f"Reading PDF: {file_path}")

        try:

            loader = PyPDFLoader(file_path)

            documents = loader.load()

            text = "\n".join(
                doc.page_content
                for doc in documents
            )

            return ToolResponse(
                tool_name=self.name,
                success=True,
                data=text,
            )

        except Exception as e:

            return ToolResponse(
                tool_name=self.name,
                success=False,
                data=None,
                error=str(e),
            )