# Gemini-Powered AI Coding Agent

This is a simple yet powerful AI agent powered by Google's Gemini model. It's designed to understand natural language commands, interact with your local file system, and execute code to perform a variety of development tasks.

## Features

- **Natural Language Understanding**: Leverages the Gemini API to interpret complex requests.
- **File System Tools**: Can list directory contents, read files, and write/overwrite files.
- **Code Execution**: Capable of running Python scripts to test changes or perform tasks.
- **Iterative Problem-Solving**: Works in a loop, using tools and refining its approach until the task is complete.
- **Simple Command-Line Interface**: Easy to run from your terminal.

## How It Works

The agent operates on a simple loop:
1.  You provide a prompt (a task) to the agent.
2.  The Gemini model determines which tool to use based on the prompt (e.g., `read_file`, `execute_python`).
3.  The agent executes the tool and sends the result back to the model.
4.  The model analyzes the result and decides on the next step.
5.  This process repeats until the model determines the task is complete, at which point it gives a final answer.

## Prerequisites

- Python 3.10+
- uv (a fast Python package installer and runner)

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ty-strong/ai-agent.git
    cd ai-agent
    ```

2.  **Set up your environment:**
    Create a file named `.env` in the root of the project and add your Gemini API key. You can get a key from Google AI Studio.

    ```env
    # .env
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

## Usage

To run the agent, use `uv run` from your terminal. Pass your request as a string argument. `uv` will automatically create a virtual environment and install the dependencies listed in `pyproject.toml`.

```bash
uv run main.py "Your task for the agent here"
```

For more detailed output on the agent's thought process and tool usage, add the `--verbose` flag:

```bash
uv run main.py "Your task for the agent here" --verbose
```

### Example

Imagine you have a `calculator.py` with a bug where it doesn't respect operator precedence (e.g., `3 + 7 * 2` incorrectly returns `20`). You can ask the agent to fix it:

```bash
uv run main.py "In calculator.py, fix the bug where 3 + 7 * 2 returns 20 instead of 17"
```