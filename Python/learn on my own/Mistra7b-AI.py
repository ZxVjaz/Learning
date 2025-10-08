import requests
import json
from datetime import datetime
import os
import random

# Variable API Ollama local
Ollama_API_URL = "http://localhost:11434/api/chat"

def chat():
    user_input = input("You: ")
    if not user_input:
        return

    # Prepare the conversation history
    messages = [{"role": "user", "content": user_input}]

    payload = {
        "model": "mistral:7b",
        "messages": messages,
        "stream": False
    }

    response = requests.post(Ollama_API_URL, json=payload, timeout=60)

    if response.status_code == 200:
        data = response.json()
        response_content = data["message"]["content"]
        print("Assistant:", response_content)
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    while True:
        chat()
