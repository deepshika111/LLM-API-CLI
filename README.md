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

## Current status

Phase 1: project environment and repository setup.

## Current status

Phase 2: a validated, non-streaming request can be sent through the OpenAI Responses API.

## Current request flow

1. Load environment variables.
2. Validate the API key, model, and timeout.
3. Initialize the OpenAI SDK client.
4. Submit one text prompt.
5. Wait for the complete response.
6. Extract and print the generated text.