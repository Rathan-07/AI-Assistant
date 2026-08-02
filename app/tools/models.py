from dataclasses import dataclass
from typing import Any


# 💡 I also added slots=True for a small memory/performance optimization. It's a nice production touch for simple data containers.

@dataclass(slots=True)
class ToolRequest:
    tool_name: str
    arguments: dict[str, Any]


@dataclass(slots=True)
class ToolResponse:
    tool_name: str
    success: bool
    data: Any
    error: str | None = None    