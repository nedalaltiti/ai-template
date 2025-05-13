# summarization_service.py

def summarize_text(text: str) -> str:
    """
    Dummy summarization service function.
    Replace with actual summarization model or API call.
    """
    if len(text) > 50:
        return text[:47] + "..."
    return text
