#!/usr/bin/env python3
"""
create_template.py

Generates the AI project template repository structure as described in the provided layout, using {{ cookiecutter.variable }} placeholders in file contents and paths where appropriate.
Supports conditional creation of files/folders based on options (like Cookiecutter).
"""

import os
import json
from pathlib import Path
import argparse

# Helper to create a file with content
def create_file(path, content=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Helper to create an empty directory
def create_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

# Parse options from command line (or set defaults)
def parse_options():
    parser = argparse.ArgumentParser(description="Generate AI template repo structure with options.")
    parser.add_argument('--output', default='api-template', help='Output directory')
    parser.add_argument('--lightweight_mode', choices=['yes', 'no'], default='no')
    parser.add_argument('--use_genai', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_agents', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_ml', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_prompts', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_classification', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_forecasting', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_regression', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_sentiment', choices=['yes', 'no'], default='yes')
    parser.add_argument('--include_rag', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_summarization', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_mlflow', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_feature_store', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_vector_db', choices=['yes', 'no'], default='yes')
    parser.add_argument('--use_messaging', choices=['yes', 'no'], default='yes')
    args = parser.parse_args()
    return vars(args)

options = parse_options()

base_dir = Path(options['output'])
create_dir(base_dir)

# Root files (always created)
create_file(base_dir / "cookiecutter.json", json.dumps({
    "repo_name": "ai-sentiment-analysis",
    "package_name": "ai_sentiment_analysis",
    "project_description": "AI service for sentiment analysis",
    "lightweight_mode": ["yes", "no"],
    "use_genai": ["yes", "no"],
    "use_agents": ["yes", "no"],
    "use_ml": ["yes", "no"],
    "use_prompts": ["yes", "no"],
    "use_classification": ["yes", "no"],
    "use_forecasting": ["yes", "no"],
    "use_regression": ["yes", "no"],
    "use_sentiment": ["yes", "no"],
    "include_rag": ["yes", "no"],
    "use_summarization": ["yes", "no"],
    "use_mlflow": ["yes", "no"],
    "use_feature_store": ["yes", "no"],
    "use_vector_db": ["yes", "no"],
    "use_messaging": ["yes", "no"],
    "_copy_without_render": ["*.html", "*.js"]
}, indent=2))
create_file(base_dir / "pyproject.toml", "# pyproject.toml\n")
create_file(base_dir / "README.md", "# {{ cookiecutter.repo_name }}\n")
create_file(base_dir / "LICENSE", "MIT License\n")
create_file(base_dir / "Makefile", "# Makefile\n")
create_file(base_dir / ".gitignore", "# .gitignore\n")
create_file(base_dir / ".env.example", "# .env.example\n")
create_file(base_dir / ".pre-commit-config.yaml", "# pre-commit config\n")
create_file(base_dir / "bitbucket-pipelines.yml", "# Bitbucket Pipelines\n")
create_file(base_dir / ".template-version", "1.0.0\n")

# Configuration
def config_section():
    configs_dir = base_dir / "configs"
    create_dir(configs_dir)
    create_file(configs_dir / "dev.yaml", "# Development environment config\n")
    create_file(configs_dir / "staging.yaml", "# Staging environment config\n")
    create_file(configs_dir / "prod.yaml", "# Production environment config\n")

# Docs & Research
def docs_section():
    docs_dir = base_dir / "docs"
    create_dir(docs_dir)
    create_file(docs_dir / "index.md", "# Documentation Home\n")
    create_file(docs_dir / "api.md", "# API Docs\n")
    create_file(docs_dir / "user_guide.md", "# User Guide\n")
    create_file(docs_dir / "development.md", "# Development Guide\n")
    create_file(docs_dir / "testing.md", "# Testing Strategy\n")
    create_file(docs_dir / "template_updates.md", "# Template Updates\n")
    adr_dir = docs_dir / "adr"
    create_dir(adr_dir)
    create_file(adr_dir / "adr-001-template.md", "# ADR Template\n")

# Notebooks
def notebooks_section():
    notebooks_dir = base_dir / "notebooks"
    create_dir(notebooks_dir / "exploration")
    create_dir(notebooks_dir / "prototypes")
    create_file(notebooks_dir / "exploration" / "README.md", "# Data Exploration Notebooks\n")
    create_file(notebooks_dir / "prototypes" / "README.md", "# Prototypes\n")

# DevOps Assets
def devops_section():
    docker_dir = base_dir / "docker"
    create_dir(docker_dir)
    create_file(docker_dir / "api.Dockerfile", "# FastAPI Dockerfile\n")
    create_file(docker_dir / "job.Dockerfile", "# Job Dockerfile\n")
    create_file(docker_dir / "compose.yaml", "# Docker Compose\n")
    k8s_dir = base_dir / "k8s"
    create_dir(k8s_dir / "base")
    for env in ["dev", "staging", "prod"]:
        create_dir(k8s_dir / "overlays" / env)
    scripts_dir = base_dir / "scripts"
    create_dir(scripts_dir)
    create_file(scripts_dir / "migrate_db.py", "# DB Migration Script\n")
    create_file(scripts_dir / "seed_demo_data.py", "# Seed Demo Data\n")
    create_file(scripts_dir / "update_from_template.py", "# Update from Template\n")

# Model Registry
def model_registry_section():
    model_registry_dir = base_dir / "model_registry"
    create_dir(model_registry_dir)
    create_file(model_registry_dir / "README.md", "# Model Registry Info\n")

# Tests
def tests_section():
    tests_dir = base_dir / "tests"
    for sub in ["unit/api", "unit/core", "unit/services", "unit/models",
                "integration/api", "integration/pipelines",
                "e2e", "fixtures"]:
        create_dir(tests_dir / sub)
    create_file(tests_dir / "e2e" / "test_api_flows.py", "# E2E Test Example\n")
    create_file(tests_dir / "fixtures" / "samples.json", "[]\n")
    create_file(tests_dir / "fixtures" / "responses.json", "[]\n")

# Application Source
def src_section():
    src_dir = base_dir / "src" / "{{ cookiecutter.package_name }}"
    create_dir(src_dir)
    create_file(src_dir / "__init__.py", "")
    create_file(src_dir / "__main__.py", "# Entry point\n")
    create_file(src_dir / "version.py", "# Version info\n")
    create_file(src_dir / "run.py", "# App entry point\n")
    # Config
    config_dir = src_dir / "config"
    create_dir(config_dir)
    create_file(config_dir / "__init__.py", "")
    create_file(config_dir / "settings.py", "# Pydantic settings\n")
    create_file(config_dir / "environment.py", "# Env loader\n")
    # Core/Lightweight
    if options['lightweight_mode'] == 'yes':
        create_file(src_dir / "core.py", "# Collapsed core domain\n")
    else:
        core_dir = src_dir / "core"
        create_dir(core_dir)
        for f in ["__init__.py", "schemas.py", "tasks.py", "errors.py", "taxonomy.py", "validation.py"]:
            create_file(core_dir / f, f"# {f}\n")
    # Prompts
    if options['use_prompts'] == 'yes':
        prompts_dir = src_dir / "prompts"
        create_dir(prompts_dir)
        for f in ["__init__.py", "templates.py", "formatters.py", "evaluators.py"]:
            create_file(prompts_dir / f, f"# {f}\n")
    # Models
    models_dir = src_dir / "models"
    create_dir(models_dir)
    create_file(models_dir / "__init__.py", "")
    # GenAI
    if options['use_genai'] == 'yes':
        genai_dir = models_dir / "genai"
        create_dir(genai_dir)
        for f in ["__init__.py", "llm_base.py", "text_generation.py", "embeddings.py"]:
            create_file(genai_dir / f, f"# {f}\n")
    # Agents
    if options['use_agents'] == 'yes':
        agents_dir = models_dir / "agents"
        create_dir(agents_dir)
        for f in ["__init__.py", "agent_manager.py", "tool_interfaces.py", "agent_protocols.py"]:
            create_file(agents_dir / f, f"# {f}\n")
    # ML
    if options['use_ml'] == 'yes':
        ml_dir = models_dir / "ml"
        create_dir(ml_dir)
        create_file(ml_dir / "__init__.py", "")
        if options['lightweight_mode'] == 'yes':
            # Collapsed ML modules
            if options['use_classification'] == 'yes':
                create_file(ml_dir / "classification.py", "# Collapsed classification module\n")
            if options['use_forecasting'] == 'yes':
                create_file(ml_dir / "forecasting.py", "# Collapsed forecasting module\n")
            if options['use_regression'] == 'yes':
                create_file(ml_dir / "regression.py", "# Collapsed regression module\n")
        else:
            # Full ML subdirs
            if options['use_classification'] == 'yes':
                sub_dir = ml_dir / "classification"
                create_dir(sub_dir)
                for f in ["model.py", "train.py", "predict.py"]:
                    create_file(sub_dir / f, f"# {f}\n")
            if options['use_forecasting'] == 'yes':
                sub_dir = ml_dir / "forecasting"
                create_dir(sub_dir)
                for f in ["model.py", "train.py", "predict.py"]:
                    create_file(sub_dir / f, f"# {f}\n")
            if options['use_regression'] == 'yes':
                sub_dir = ml_dir / "regression"
                create_dir(sub_dir)
                for f in ["model.py", "train.py", "predict.py"]:
                    create_file(sub_dir / f, f"# {f}\n")
    # Services
    services_dir = src_dir / "services"
    create_dir(services_dir)
    create_file(services_dir / "__init__.py", "")
    if options['include_rag'] == 'yes':
        create_file(services_dir / "rag_service.py", "# rag_service.py\n")
    if options['use_summarization'] == 'yes':
        create_file(services_dir / "summarization_service.py", "# summarization_service.py\n")
    if options['use_classification'] == 'yes':
        create_file(services_dir / "classification_service.py", "# classification_service.py\n")
    if options['use_forecasting'] == 'yes':
        create_file(services_dir / "forecasting_service.py", "# forecasting_service.py\n")
    if options['use_sentiment'] == 'yes':
        create_file(services_dir / "sentiment_service.py", "# sentiment_service.py\n")
    # API
    api_dir = src_dir / "api"
    create_dir(api_dir)
    for f in ["__init__.py", "app.py", "middleware.py", "models.py"]:
        create_file(api_dir / f, f"# {f}\n")
    routers_dir = api_dir / "routers"
    create_dir(routers_dir)
    create_file(routers_dir / "__init__.py", "")
    create_file(routers_dir / "health_router.py", "# health_router.py\n")
    if options['use_genai'] == 'yes':
        create_file(routers_dir / "genai_router.py", "# genai_router.py\n")
    if options['use_agents'] == 'yes':
        create_file(routers_dir / "agent_router.py", "# agent_router.py\n")
    if options['use_ml'] == 'yes':
        create_file(routers_dir / "ml_router.py", "# ml_router.py\n")
    # CLI
    cli_dir = src_dir / "cli"
    create_dir(cli_dir)
    for f in ["__init__.py", "commands.py", "app.py"]:
        create_file(cli_dir / f, f"# {f}\n")
    # Pipelines
    if options['lightweight_mode'] == 'yes':
        create_file(src_dir / "pipelines.py", "# Collapsed pipelines module\n")
    else:
        pipelines_dir = src_dir / "pipelines"
        create_dir(pipelines_dir)
        for f in ["__init__.py", "data_ingestion.py", "preprocessing.py", "training.py", "evaluation.py"]:
            create_file(pipelines_dir / f, f"# {f}\n")
    # Infrastructure
    infra_dir = src_dir / "infrastructure"
    create_dir(infra_dir)
    create_file(infra_dir / "__init__.py", "")
    # LLM Providers
    if options['use_genai'] == 'yes':
        llm_dir = infra_dir / "llm_providers"
        create_dir(llm_dir)
        for f in ["__init__.py", "base.py", "openai.py", "anthropic.py"]:
            create_file(llm_dir / f, f"# {f}\n")
    # Tracking
    if options['use_mlflow'] == 'yes':
        tracking_dir = infra_dir / "tracking"
        create_dir(tracking_dir)
        for f in ["__init__.py", "tracker.py"]:
            create_file(tracking_dir / f, f"# {f}\n")
    # Storage
    storage_dir = infra_dir / "storage"
    create_dir(storage_dir)
    create_file(storage_dir / "__init__.py", "")
    if options['use_feature_store'] == 'yes':
        create_file(storage_dir / "feature_store.py", "# feature_store.py\n")
    if options['use_vector_db'] == 'yes':
        create_file(storage_dir / "vector_db.py", "# vector_db.py\n")
    # Messaging
    if options['use_messaging'] == 'yes':
        messaging_dir = infra_dir / "messaging"
        create_dir(messaging_dir)
        for f in ["__init__.py", "queue.py"]:
            create_file(messaging_dir / f, f"# {f}\n")
    # Utils
    utils_dir = src_dir / "utils"
    create_dir(utils_dir)
    for f in ["__init__.py", "logging.py", "result.py", "retry.py", "timers.py", "helpers.py"]:
        create_file(utils_dir / f, f"# {f}\n")
    # Data
    samples_dir = src_dir / "data" / "samples"
    create_dir(samples_dir)
    create_file(samples_dir / "prompts.json", "[]\n")
    create_file(samples_dir / "responses.json", "[]\n")

# Run all sections
config_section()
docs_section()
notebooks_section()
devops_section()
model_registry_section()
tests_section()
src_section()

print(f"AI template repository structure created successfully in {base_dir}!") 