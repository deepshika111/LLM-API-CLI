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



class LLMClient:
    """ Small wrapper class around the client """

    def __init__ (self, settings:Settings) -> None:
        self._settings = settings

        self._client = OpenAI (
            api_key=settings.api_key,
            base_url="https://openrouter.ai/api/v1",
            timeout=settings.request_timeout_seconds,
        )


    def generate(self,developer_instruction: str,user_prompt: str,) -> GenerationResult:
        """ Send a prompt and return generated text """

        if not user_prompt.strip():
            raise ValueError("The prompt cannot be empty.")

        messages = build_messages(
            developer_instruction=developer_instruction,
            user_prompt=user_prompt,
        )

        response = self._client.responses.create (
            model=self._settings.model,
            input=messages,
        )

        if response.status != 'completed':
            raise RuntimeError(
                f'The model did not complete. Status:{response.status}'
            )


        if response.usage is None:
            raise RuntimeError(
                "The response did not contain token usage information."
            )

        text = response.output_text

        return GenerationResult(
            response_id=response.id,
            model_used=response.model,
            status=response.status,
            text=text,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            total_tokens=response.usage.total_tokens,
        )

         #return response.output_text

        # text_parts : list[str] = []

        # for output_item in response.output:               (why response.output_text is used)
        #     if output_item.type!= "message":
        #         continue 

        #     for content_item in output_item.content:
        #         if content_item.type == "output_text":
        #             text_parts.append(content_item.text)

        # return "".join(text_parts)



        # response_dictionary = response.model_dump()

        # print("\n--- Dictionary representation ---")     (dictionary response over why SDK is better)
        # pprint(response_dictionary)

        # return response.output_text



