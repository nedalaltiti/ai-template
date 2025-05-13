# Job Dockerfile

FROM python:3.10-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
COPY src/ ./src/
COPY docker/job_entrypoint.sh /job_entrypoint.sh
RUN chmod +x /job_entrypoint.sh

# Create a non-root user
RUN useradd -m appuser
USER appuser

ENTRYPOINT ["/job_entrypoint.sh"]
