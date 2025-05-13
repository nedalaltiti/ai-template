# health_router.py
from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok"}