"""Message construction for LLM requests."""

from typing import Literal, TypedDict


MessageRole = Literal[
    "developer",
    "user",
    "assistant",
]


class Message(TypedDict):
    """A structured text message sent to the model."""

    role: MessageRole
    content: str


def build_messages(
    developer_instruction: str,
    user_prompt: str,
) -> list[Message]:
    """Build and validate messages for one model request."""

    cleaned_instruction = developer_instruction.strip()
    cleaned_prompt = user_prompt.strip()

    if not cleaned_instruction:
        raise ValueError("The developer instruction cannot be empty.")

    if not cleaned_prompt:
        raise ValueError("The user prompt cannot be empty.")

    return [
        {
            "role": "developer",
            "content": cleaned_instruction,
        },
        {
            "role": "user",
            "content": cleaned_prompt,
        },
    ]

    print("\n--- Request messages ---")

    for message in messages:
        print(f"Role: {message['role']}")
        print(f"Content: {message['content']}")
        print()