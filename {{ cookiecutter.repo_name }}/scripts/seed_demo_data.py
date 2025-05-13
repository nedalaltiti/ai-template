# Seed Demo Data
import json
import logging
from pathlib import Path

def seed_demo_data():
    """
    Seed demo data into the data/samples directory.
    """
    logging.basicConfig(level=logging.INFO)
    samples_dir = Path(__file__).parent.parent / "src" / "{{ cookiecutter.package_name }}" / "data" / "samples"
    samples_dir.mkdir(parents=True, exist_ok=True)

    prompts = [
        {"text": "What is the capital of France?"},
        {"text": "Summarize the following article..."}
    ]
    responses = [
        {"result": "Paris"},
        {"result": "This article discusses..."}
    ]

    (samples_dir / "prompts.json").write_text(json.dumps(prompts, indent=2))
    (samples_dir / "responses.json").write_text(json.dumps(responses, indent=2))
    logging.info(f"Seeded demo data in {samples_dir}")

if __name__ == "__main__":
    seed_demo_data()
