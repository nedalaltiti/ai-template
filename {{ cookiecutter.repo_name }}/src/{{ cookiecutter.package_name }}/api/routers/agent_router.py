# agent_router.py
from fastapi import APIRouter, Request
from ...models.agents.agent_manager import AgentManager
from ...models.agents.agent_protocols import AgentCard, MCPRequest, MCPResponse

router = APIRouter(prefix="/agents", tags=["Agents"])
manager = AgentManager()

@router.get("/card", response_model=AgentCard)
def get_agent_card():
    """
    Returns this agent's A2A Agent Card (capabilities, endpoints, etc.).
    """
    return manager.get_agent_card()

@router.post("/mcp", response_model=MCPResponse)
def handle_mcp(request: MCPRequest):
    """
    Handle an MCP (Model Context Protocol) request for tool invocation or context injection.
    """
    return manager.handle_mcp(request)