# DB Migration Script
import subprocess
import logging
import sys
from pathlib import Path

def migrate_db():
    """
    Run database migrations using Alembic.
    """
    logging.basicConfig(level=logging.INFO)
    alembic_ini = Path(__file__).parent.parent / "alembic.ini"
    if not alembic_ini.exists():
        logging.info("Alembic not initialized. Initializing...")
        subprocess.run(["alembic", "init", "alembic"], check=True)
    try:
        logging.info("Running Alembic migrations...")
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        logging.info("Database migrated successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Migration failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    migrate_db()
