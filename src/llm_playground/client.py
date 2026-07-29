""" Client is responsible for communicating with API """

from openai import OpenAI
from llm_playground.settings import Settings

class LLMClient:
    """ Small wrapper class around the client """

    def __init__ (self, settings:Settings) -> None:
        self._settings = settings

        self._client = OpenAI (
            api_key=settings.api_key,
            timeout=settings.request_timeout_seconds,
        )


    def generate (self, prompt:str) -> str:
        """ Send a prompt and return generated text """

        if not prompt.strip():
            raise ValueError("The prompt cannot be empty.")

        response = self._client.responses.create (
            model=self._settings.model,
            input=prompt,
        )

        return response.output_text
