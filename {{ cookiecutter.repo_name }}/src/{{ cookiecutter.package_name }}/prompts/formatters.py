# formatters.py

def format_prompt(template: str, **kwargs) -> str:
    """
    Format a prompt template with the given keyword arguments.
    Useful for dynamically constructing prompts for GenAI workflows.
    """
    return template.format(**kwargs) 