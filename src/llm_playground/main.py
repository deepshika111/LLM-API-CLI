"""Entry point for the LLM API Playground."""

from llm_playground.client import LLMClient
from llm_playground.settings import load_settings
from llm_playground.cli import parse_arguments



def main() -> None:
    """Send one prompt to the configured LLM."""
    """Parse input, call the LLM, and display the result."""


    settings = load_settings()
    client = LLMClient(settings)
    arguments = parse_arguments()

    developer_instruction = (
    "You are a patient programming teacher. "
    "Explain concepts in clear, beginner-friendly language. "
    "Use a small example when it improves understanding."
)

    result = client.generate(
    developer_instruction=developer_instruction,
    user_prompt=arguments.prompt,
    max_output_tokens=arguments.max_output_tokens,
)
    print(result.text)

    print(f"Model: {settings.model}")
    print(f"Prompt: {arguments.prompt}")
    print("\nAssistant:")

    if arguments.show_metadata:
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