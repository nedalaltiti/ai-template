# feature_store.py

class FeatureStore:
    """
    Simple in-memory feature store for demonstration.
    Replace with a real backend (e.g., Redis, Feast) for production.
    """
    def __init__(self):
        self._store = {}

    def put(self, key: str, features: dict):
        self._store[key] = features

    def get(self, key: str) -> dict:
        return self._store.get(key, {})
