# tool_interfaces.py
from abc import ABC, abstractmethod

class AgentToolInterface(ABC):
    """
    Abstract base class for agent tool interfaces.
    Each tool should implement the execute method, which can be invoked via MCP or A2A protocols.
    """
    @abstractmethod
    def execute(self, input_data: str) -> str:
        """
        Execute the tool with the given input and return the result.
        """
        pass
