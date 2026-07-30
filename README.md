# LLM API Playground

A command-line application for learning and experimenting with the core LLM API primitive.

## Planned capabilities

- Send prompts to an LLM API
- Configure generation parameters
- Stream responses
- Track token usage
- Estimate request costs
- Maintain client-side conversation history
- Enforce context budgets
- Retry temporary failures
- Record structured operational logs


Phase 1: project environment and repository setup.

Phase 2: a validated, non-streaming request can be sent through the OpenAI Responses API.

## request flow

1. Load environment variables.
2. Validate the API key, model, and timeout.
3. Initialize the OpenAI SDK client.
4. Submit one text prompt.
5. Wait for the complete response.
6. Extract and print the generated text.

Phase 3: the application now extracts a structured result from each
non-streaming API response.

## Response information captured

- Response ID
- Completion status
- Returned model
- Generated text
- Input-token usage
- Output-token usage
- Total-token usage

The raw OpenAI response is converted into an application-level
`GenerationResult` object.

