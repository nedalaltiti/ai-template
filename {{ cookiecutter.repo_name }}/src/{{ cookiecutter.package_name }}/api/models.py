# models.py
from pydantic import BaseModel

class TextGenerationRequest(BaseModel):
    prompt: str

class TextGenerationResponse(BaseModel):
    result: str

class HealthResponse(BaseModel):
    status: str
