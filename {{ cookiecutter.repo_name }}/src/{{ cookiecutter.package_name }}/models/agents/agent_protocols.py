# agent_protocols.py

from pydantic import BaseModel
from typing import List, Optional

class AgentCard(BaseModel):
    id: str
    name: str
    capabilities: List[str]
    endpoints: List[str]

class MCPRequest(BaseModel):
    tool: str
    input: str

class MCPResponse(BaseModel):
    result: str
    error: Optional[bool] = False