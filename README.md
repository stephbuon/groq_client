# groq_client

A lightweight Python package to send queries to the Groq API using LLMs.

## Installation

```bash
pip install git+https://github.com/yourusername/groq_client.git
```

## Usage

```python
from groq_client import ask_groq

response = ask_groq("Translate this Russian sentence into English.")
print(response)
```

## Requirements

- Set your Groq API key as an environment variable:
```bash
export GROQ_API_KEY=your_api_key_here
```
