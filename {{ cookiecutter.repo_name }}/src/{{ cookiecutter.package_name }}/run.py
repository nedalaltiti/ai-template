# App entry point
import os
import uvicorn

# If this file is in src/{{ cookiecutter.package_name }}/, use relative import
from .api.app import app

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)
