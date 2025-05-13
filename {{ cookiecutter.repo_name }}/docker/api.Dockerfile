# FastAPI Dockerfile

# --- Build stage ---
FROM python:3.10-slim AS builder
WORKDIR /app
COPY pyproject.toml .
RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# --- Runtime stage ---
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY src/ ./src/
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create a non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
