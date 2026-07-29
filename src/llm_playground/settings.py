import os 
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()

@dataclass(frozen=True)
class Settings:
    """ Configurations for calling LLM API """

    api_key:str
    model:str
    request_timeout_seconds:float

def load_settings () -> Settings:
    """ Loading APP Settings """

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL")
    timeout_text = os.getenv("REQUEST_TIMEOUT_SECONDS", "30")


    if not api_key:
        raise ValueError (
            'API Key missing'
        )


    if not model:
        raise ValueError (
            'Model Missing'
        )


    try:
        request_timeout_seconds = float(timeout_text)
    except ValueError as error:
        raise ValueError(
            "REQUEST_TIMEOUT_SECONDS must be a number."
        ) from error

    if request_timeout_seconds <= 0:
        raise ValueError(
            "REQUEST_TIMEOUT_SECONDS must be greater than zero."
        )

    return Settings(
        api_key = api_key,
        model = model,
        request_timeout_seconds = request_timeout_seconds
    )
