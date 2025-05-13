# azure_openai.py

class AzureOpenAIProvider:
    def generate(self, prompt: str) -> str:
        return f"AzureOpenAI: {prompt}"