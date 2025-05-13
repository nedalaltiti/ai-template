# base.py
from abc import ABC, abstractmethod

class LLMProviderBase(ABC):
    """
    Abstract base class for all LLM providers.
    Ensures a consistent interface for text generation and other LLM tasks.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate text from a prompt using the LLM provider.
        """
        pass
