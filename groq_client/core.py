import requests
import os

def ask_groq(query, model="llama-3.3-70b-versatile"):
    """
    Sends a prompt to the Groq API and returns the response.

    Args:
        query (str): The user prompt.
        model (str): The model name to use. Default is "llama-3.3-70b-versatile".

    Returns:
        str: The model's response or an error message.
    """
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY environment variable is not set.")

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": query}]
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
    else:
        return f"Failed with status code {response.status_code}: {response.text}"
