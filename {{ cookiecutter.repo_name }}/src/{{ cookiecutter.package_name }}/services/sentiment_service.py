# sentiment_service.py

def predict_sentiment(text: str) -> str:
    """
    Dummy sentiment prediction.
    """
    return "positive" if "good" in text else "negative"