# E2E Test Example
import pytest
from httpx import AsyncClient
import importlib.util
import sys
import os

# Dynamically import the app module
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, src_path)
app_module = importlib.import_module('src.{{ cookiecutter.package_name }}.api.app')
app = app_module.app

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health/")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_genai_generate():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {"prompt": "Hello, world!"}
        response = await ac.post("/genai/generate", json=payload)
        assert response.status_code == 200
        assert "result" in response.json()
