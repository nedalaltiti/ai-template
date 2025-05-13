# llm_base.py

class LLMBase:
    """
    Base class for Large Language Models.
    """
    def generate(self, prompt: str) -> str:
        raise NotImplementedError

    def embed(self, text: str) -> list[float]:
        raise NotImplementedError

    def chat(self, messages: list[dict]) -> str:
        raise NotImplementedError