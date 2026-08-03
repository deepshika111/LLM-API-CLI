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

Phase 4: Command-line argument parsing for the LLM API Playground
## Usage

Added cli.py 

Send a prompt:

PYTHONPATH=src python -m llm_playground.main \
  --prompt "Explain machine learning in simple terms."

Response:

Machine learning is a way for computers to become smart at certain tasks by learning from examples, rather than being given strict instructions. Think of it like teaching a child to identify animals: instead of listing every possible rule about their features, you show them many pictures of dogs and cats with labels. The computer (or the child) then looks for patterns that help distinguish one from the other. 

Here’s a simple breakdown:  
1. **Data is King**: Computers need lots of examples (data) to learn. It could be pictures, books, numbers, or even your Netflix watching history.  
2. **Learn, Don’t Program**: Instead of writing detailed rules, we let the computer explore the data, figure out hidden patterns, and use those to make sense of new information.  
3. **Types of Learning**:  
   - **Supervised Learning**: Like a teacher grading homework. The computer learns with labeled examples (e.g., "This is a rainy day," "That is sunny day").  
   - **Unsupervised Learning**: Letting the computer group or sort data on its own (e.g., "Sort these movies into genres" without telling it what the genres are).  
   - **Reinforcement Learning**: Like training a puppy. The computer tries actions, gets feedback (e.g., points in a video game), and improves over time.  

4. **Predict & Decide**: Once trained, the computer can guess the answer to a new question (e.g., "Is this picture a cat or a dog?") or decide the best action in a given situation (e.g., steering a self-driving car).  

**Real-World Uses**:  
- Recommending songs you'll like on Spotify.  
- Recognizing your face on a smartphone.  
- Helping doctors detect diseases in scans.  
- Playing chess or Go by strategizing smarter each move.  

**Important Note**: It’s not magic! It’s powered by math and statistics, and it needs high-quality data. The more examples you give, the better it gets, but it can also make mistakes if the data is messy or if it overfits (learns the examples too well to handle new situations).  

In short, machine learning is like giving a computer a super-sized brain workout with data so it can think and act smart in its task. 
Model: qwen/qwen3-32b
Prompt: Explain machine learning in simple terms.


## With Metadata

**Machine Learning Explained Simply:**

Imagine teaching your pet a new trick. You show them how to sit, reward them when they succeed, and guide them until they get it right. Machine learning works in a similar way, but with computers!

**How It Works:**
1. **Learning from Examples:** Instead of programming step-by-step rules, you feed the computer a bunch of examples (data). For instance, thousands of labeled pictures of cats and dogs, or past emails marked as "spam" or "not spam."
2. **Finding Patterns:** The computer filters through all this data to find patterns—like how certain words in an email might be a red flag for spam.
3. **Getting Better Over Time:** The system keeps adjusting its guesses based on feedback (e.g., "Right, this is spam!" or "Oops, missed that one!"). The more examples it gets, the better it becomes at making decisions.

**Why It’s Useful:**
Think of apps that guess movies you’d like, self-driving cars avoiding potholes, or smart assistants who understand your voice. These systems aren’t following pre-set instructions—they’re using learned patterns to adapt and help you!

**In Short:**  
Machine learning is like teaching a robot with examples instead of rules. It learns by practice, improves with experience, and helps handle tasks too complex for basic programming.
Model: qwen/qwen3-32b
Prompt: Explain machine learning in simple terms.

Assistant:

--- Response information ---
Response ID: gen-1785432849-jY7H9AB17tvNST2agd7V
Status: completed
Returned model: qwen/qwen3-32b
Input tokens: 17
Output tokens: 904
Total tokens: 921

## Structured messages

Requests are sent using role-based messages:

- `developer` defines application behavior.
- `user` contains the command-line prompt.
- `assistant` will represent previous model responses when conversation
  history is introduced.

Current request structure:

```python
[
    {
        "role": "developer",
        "content": "Explain programming concepts clearly.",
    },
    {
        "role": "user",
        "content": "What is recursion?",
    },
]

