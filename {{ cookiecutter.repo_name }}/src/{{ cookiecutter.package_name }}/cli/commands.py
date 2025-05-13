# commands.py
import typer
from ..services.summarization_service import summarize_text

app = typer.Typer()

@app.command()
def summarize(text: str):
    """
    Summarize the given text using the summarization service.
    """
    summary = summarize_text(text)
    typer.echo(f"Summary: {summary}")

# Add more CLI commands as needed for your workflows
