# {{ cookiecutter.repo_name }}

## Overview

**{{ cookiecutter.repo_name }}** is a production-ready, modular AI/ML project template designed for rapid prototyping and robust deployment of AI services. It supports GenAI, classical ML, RAG, and more, with best practices for engineering, testing, and DevOps.

---

## Why This Repo Exists

- **Accelerate AI/ML project setup** with a proven, extensible structure.
- **Support both GenAI and classical ML** workflows out of the box.
- **Enable best practices** for configuration, testing, CI/CD, and deployment.
- **Make it easy for teams** to understand, extend, and maintain AI services.

---

## Project Structure

```
.
├── configs/                # Environment and app configs
├── docker/                 # Dockerfiles and Compose for local/dev/prod
├── docs/                   # Documentation and architecture decisions
├── k8s/                    # Kubernetes manifests (base/overlays)
├── model_registry/         # Model versioning and registry
├── notebooks/              # Jupyter notebooks (exploration, prototyping)
├── scripts/                # Automation scripts (seed, migrate, update)
├── src/
│   └── {{ cookiecutter.package_name }}/
│       ├── api/            # FastAPI app and routers
│       ├── cli/            # CLI entrypoints (Typer)
│       ├── config/         # Pydantic settings and environment loader
│       ├── core/           # Core logic, schemas, errors
│       ├── data/           # Data samples, fixtures
│       ├── infrastructure/ # LLM providers, storage, messaging, tracking
│       ├── models/         # ML, GenAI, agent models
│       ├── pipelines/      # Data/ML pipelines (ingest, preprocess, train, eval)
│       ├── prompts/        # Prompt templates and evaluators
│       ├── services/       # Service layer (RAG, sentiment, etc.)
│       ├── utils/          # Utilities (logging, retry, etc.)
│       └── version.py      # Version info
├── tests/                  # E2E and fixture tests
├── Makefile                # Common dev commands
├── pyproject.toml          # Python dependencies and metadata
├── bitbucket-pipelines.yml # CI/CD pipeline config
└── README.md               # This file
```

---

## Template Flags & Customization

When generating a new project, you can toggle features using these flags (from `cookiecutter.json`):

| Flag                | Description                                 | Options      |
|---------------------|---------------------------------------------|--------------|
| repo_name           | Name of the repo/project                    | str          |
| package_name        | Python package name                         | str          |
| project_description | Short description                           | str          |
| lightweight_mode    | Minimal structure (no expanded dirs)        | yes / no     |
| use_genai           | Include GenAI models and endpoints          | yes / no     |
| use_agents          | Include agent models and endpoints          | yes / no     |
| use_ml              | Include ML models and endpoints             | yes / no     |
| use_prompts         | Include prompt templates/evaluators         | yes / no     |
| use_classification  | Include classification ML pipeline          | yes / no     |
| use_forecasting     | Include forecasting ML pipeline             | yes / no     |
| use_regression      | Include regression ML pipeline              | yes / no     |
| use_sentiment       | Include sentiment service                   | yes / no     |
| include_rag         | Include RAG (Retrieval-Augmented Gen)       | yes / no     |
| use_summarization   | Include summarization service               | yes / no     |
| use_mlflow          | Include MLflow tracking                     | yes / no     |
| use_feature_store   | Include feature store infra                 | yes / no     |
| use_vector_db       | Include vector DB infra                     | yes / no     |
| use_messaging       | Include messaging infra                     | yes / no     |

---

## Prerequisites

- Python 3.9+ (recommend using [pyenv](https://github.com/pyenv/pyenv) or [conda](https://docs.conda.io/))
- [Poetry](https://python-poetry.org/) or `pip`
- [Docker](https://www.docker.com/) (for local dev and deployment)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) (install via `pipx install cookiecutter`)
- (Optional) [Alembic](https://alembic.sqlalchemy.org/) for DB migrations

---

## Getting Started

### 1. Generate a New Project

```bash
cookiecutter git@github.com:nedalaltiti/ai-template.git \
  --checkout v0.1.10 \
  --no-input \
  repo_name=myproject \
  package_name=my_package \
  project_description="My AI Service" \
  lightweight_mode=yes \
  use_genai=yes \
  use_agents=no \
  use_ml=yes \
  # ...other flags as needed
```

### 2. Initialize Git & Install Dependencies

```bash
cd myproject
git init && git add . && git commit -m "initial"
poetry install  # or: pip install -e .
```

### 3. Seed Demo Data (optional)

```bash
python scripts/seed_demo_data.py
```

### 4. Run Database Migrations (if using DB)

```bash
python scripts/migrate_db.py
```

### 5. Start the API Locally

```bash
uvicorn src.my_package.api.app:app --reload
# or, if __main__.py is present:
python -m src.my_package
```

### 6. Run the CLI

```bash
python src/my_package/cli/app.py hello Nedal
```

### 7. Run Tests

```bash
pytest tests/
```

---

## Docker & Deployment

- **Build and run with Docker Compose:**
  ```bash
  docker compose up --build
  ```
- **Build API image:**
  ```bash
  docker build -f docker/api.Dockerfile -t myproject-api .
  ```
- **Kubernetes manifests** are in `k8s/` (see overlays for dev/prod).

---

## Updating from Template

To pull the latest template changes and re-apply:

```bash
python scripts/update_from_template.py
# Then manually resolve any merge conflicts and re-run cookiecutter if needed.
```

---

## Configuration & Environments

- All config is managed via Pydantic settings in `src/{{ cookiecutter.package_name }}/config/`.
- Use `.env`, `.env.dev`, `.env.prod`, etc. for environment-specific settings.
- Switch environments by setting `APP_ENV=dev` (or `prod`, `test`).

---

## Testing

- Place E2E tests in `tests/e2e/`
- Place fixtures in `tests/fixtures/`
- Use `pytest` for running tests.

---

## Notebooks

- Place exploratory notebooks in `notebooks/exploration/`
- Place prototype notebooks in `notebooks/prototypes/`

---

## CI/CD

- Bitbucket Pipelines config is in `bitbucket-pipelines.yml`
- Add your test, build, and deploy steps as needed.

---

## Contributing

1. Fork the repo and create your branch.
2. Commit your changes with clear messages.
3. Ensure all tests pass.
4. Open a pull request.

---

**Happy hacking! 🚀**
