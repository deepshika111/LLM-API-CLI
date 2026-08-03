"""Command-line argument parsing for the LLM API Playground."""

import argparse
from dataclasses import dataclass
from typing import Sequence

@dataclass(frozen=True)
class CLIArguments:
    """Validated values supplied through the command line."""

    prompt: str
    show_metadata: bool
    max_output_tokens: int | None


def build_parser() -> argparse.ArgumentParser:
    """Create and configure the command-line argument parser."""

    parser = argparse.ArgumentParser(
        prog="llm-playground",
        description="Send a prompt to an LLM from the command line.",
    )

    parser.add_argument(
        "-p",
        "--prompt",
        required=True,
        help="The text prompt to send to the model.",
    )

    parser.add_argument(
        "--show-metadata",
        action="store_true",
        help="Display response ID, model, status, and token usage.",
    )

    parser.add_argument(
    "--max-output-tokens",
    type=int,
    default=None,
    help="Maximum number of output tokens the model may generate.",
)

    return parser


def parse_arguments(
    arguments: Sequence[str] | None = None,
) -> CLIArguments:
    """Parse and validate command-line arguments."""

    parser = build_parser()
    namespace = parser.parse_args(arguments)

    prompt = namespace.prompt.strip()

    max_output_tokens = namespace.max_output_tokens

    if max_output_tokens is not None and max_output_tokens <= 0:
        parser.error("--max-output-tokens must be greater than zero.")

    if not prompt:
        parser.error("--prompt cannot be empty.")

    return CLIArguments(
        prompt=prompt,
        show_metadata=namespace.show_metadata,
        max_output_tokens=max_output_tokens,
    )