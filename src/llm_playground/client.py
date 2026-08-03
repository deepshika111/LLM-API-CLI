""" Client is responsible for communicating with API """

from openai import OpenAI
from llm_playground.settings import Settings
from openai.types.responses import Response
from dataclasses import dataclass
from llm_playground.messages import build_messages


@dataclass(frozen=True)
class GenerationResult:
    """Important information extracted from one model response."""

    response_id: str
    model_used:str
    status:str
    text:str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    finish_reason: str 
    max_output_tokens: int | None = None
    



class LLMClient:
    """ Small wrapper class around the client """

    def __init__ (self, settings:Settings) -> None:
        self._settings = settings

        self._client = OpenAI (
            api_key=settings.api_key,
            base_url="https://openrouter.ai/api/v1",
            timeout=settings.request_timeout_seconds,
        )


    def generate(
        self,
        developer_instruction: str,
        user_prompt: str,
        max_output_tokens: int | None = None,
    ) -> GenerationResult:
        """Send structured messages and return the generated result."""

        if max_output_tokens is not None and max_output_tokens <= 0:
            raise ValueError(
                "max_output_tokens must be greater than zero."
            )

        messages = build_messages(
            developer_instruction=developer_instruction,
            user_prompt=user_prompt,
        )

        if max_output_tokens is None:
            response = self._client.responses.create(
                model=self._settings.model,
                input=messages,
            )
        else:
            response = self._client.responses.create(
                model=self._settings.model,
                input=messages,
                max_output_tokens=max_output_tokens,
            )

        finish_reason = None

        if response.incomplete_details is not None:
            finish_reason = response.incomplete_details.reason

        if response.status not in {"completed", "incomplete"}:
            raise RuntimeError(
                "The model response ended with an unexpected status. "
                f"Status: {response.status}"
            )

        text = response.output_text

        if not text:
            if finish_reason == "max_output_tokens":
                raise RuntimeError(
                    "The model reached the output-token limit before "
                    "producing visible text. Try increasing "
                    "--max-output-tokens."
                )

            raise RuntimeError(
                "The response contained no text output."
            )

        if response.usage is None:
            raise RuntimeError(
                "The response did not contain token usage information."
            )

        return GenerationResult(
            response_id=response.id,
            model=response.model,
            status=response.status,
            finish_reason=finish_reason,
            text=text,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            total_tokens=response.usage.total_tokens,
        )