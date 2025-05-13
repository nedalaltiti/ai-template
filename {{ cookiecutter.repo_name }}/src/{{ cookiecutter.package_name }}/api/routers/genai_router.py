# genai_router.py
from fastapi import APIRouter
from ...models.genai.text_generation import generate_text

router = APIRouter(prefix="/genai", tags=["GenAI"])

@router.post("/generate")
def generate(prompt: str):
    """
    Generate text using a GenAI model.
    """
    result = generate_text(prompt)
    return {"result": result}