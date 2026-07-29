"""Entry point for the LLM API Playground"""

from llm_playground.client import LLMClient
from llm_playground.settings import load_settings


def main() -> None:
    """Send one prompt to the configured LLM"""

    settings = load_settings()
    client = LLMClient(settings)

    prompt = "Explain what an API is in one beginner-friendly sentence"

    print(f"Model: {settings.model}")
    print(f"Prompt: {prompt}")
    print("\nAssistant:")

    answer = client.generate(prompt)

    print(answer)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print ('Application error: {error}')
        raise SystemExit(1)