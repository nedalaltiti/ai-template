# app.py
from fastapi import FastAPI
from .routers import health_router, genai_router, ml_router

def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    app = FastAPI(
        title="AI Template API",
        description="API for AI/ML operations",
        version="0.1.0"
    )
    app.include_router(health_router.router)
    app.include_router(genai_router.router)
    app.include_router(ml_router.router)
    return app

app = create_app()