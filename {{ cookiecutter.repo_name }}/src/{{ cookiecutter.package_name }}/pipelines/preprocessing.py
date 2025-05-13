# preprocessing.py

def preprocess(data: list[dict]) -> list[dict]:
    """
    Dummy preprocessing.
    """
    for item in data:
        item["text"] = item["text"].lower()
    return data