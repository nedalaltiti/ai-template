# classification_service.py

def predict_class(text: str) -> str:
    """
    Dummy classification service function.
    Replace with actual model inference logic.
    """
    if "good" in text.lower():
        return "positive"
    elif "bad" in text.lower():
        return "negative"
    else:
        return "neutral"
