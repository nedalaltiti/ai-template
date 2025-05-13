# Update from Template
import subprocess
import logging
import sys

def update_template():
    """
    Pull the latest template and show the diff. Optionally apply updates.
    """
    logging.basicConfig(level=logging.INFO)
    logging.info("Pulling latest template...")
    try:
        subprocess.run(["git", "pull"], check=True)
        logging.info("Template updated. Run 'cookiecutter' to re-apply if needed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to update template: {e}")
        sys.exit(1)

if __name__ == "__main__":
    update_template()
