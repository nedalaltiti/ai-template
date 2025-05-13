# agent_manager.py
from .agent_protocols import AgentCard, MCPRequest, MCPResponse

class AgentManager:
    def __init__(self):
        self.card = AgentCard(
            id="agent-001",
            name="ExampleAgent",
            capabilities=["summarize", "classify"],
            endpoints=["/agents/mcp"]
        )

    def get_agent_card(self) -> AgentCard:
        """
        Return this agent's A2A Agent Card.
        """
        return self.card

    def handle_mcp(self, request: MCPRequest) -> MCPResponse:
        """
        Handle an MCP request (e.g., tool invocation).
        """
        # Example: route to a summarization tool
        if request.tool == "summarize":
            summary = f"Summary: {request.input[:50]}..."
            return MCPResponse(result=summary)
        return MCPResponse(result="Tool not found", error=True)