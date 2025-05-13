#!/bin/bash
set -e

# Run database migrations if script exists
if [ -f scripts/migrate_db.py ]; then
  python scripts/migrate_db.py || true
fi

# Seed demo data if script exists
if [ -f scripts/seed_demo_data.py ]; then
  python scripts/seed_demo_data.py || true
fi

# Start the API
exec uvicorn src.{{ cookiecutter.package_name }}.api.app:app --host 0.0.0.0 --port 8000 