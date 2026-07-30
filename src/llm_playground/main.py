"""Entry point for the LLM API Playground."""

from llm_playground.client import LLMClient
from llm_playground.settings import load_settings


def main() -> None:
    """Send one prompt to the configured LLM."""

    settings = load_settings()
    client = LLMClient(settings)

    prompt = (
    "Explain what an API is to a complete beginner. "
    "Use one real-world analogy and one software example. "
    "Keep the explanation under 100 words."
    )

    print(f"Model: {settings.model}")
    print(f"Prompt: {prompt}")
    print("\nAssistant:")

    result = client.generate(prompt)
    print(result.text)

    print("\n--- Response information ---")
    print(f"Response ID: {result.response_id}")
    print(f"Status: {result.status}")
    print(f"Returned model: {result.model_used}")
    print(f"Input tokens: {result.input_tokens}")
    print(f"Output tokens: {result.output_tokens}")
    print(f"Total tokens: {result.total_tokens}")
    


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Application error: {error}")
        raise SystemExit(1)