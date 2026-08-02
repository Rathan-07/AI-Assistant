from dataclasses import dataclass


@dataclass(slots=True)
class Plan:

    use_tool: bool

    tool_name: str | None = None

    tool_arguments: dict | None = None