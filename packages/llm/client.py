class LLMClient:
    def __init__(self, provider: str):
        self.provider = provider

    async def generate(self, prompt: str) -> str:
        raise NotImplementedError("LLM provider not implemented yet")
