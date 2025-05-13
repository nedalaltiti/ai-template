# embeddings.py

def embed_text(text: str) -> list[float]:
    """
    Dummy embedding function.
    Replace with actual embedding model.
    """
    return [float(ord(c)) for c in text[:10]]