"""Simple example to call OpenAI Chat Completions API.

Usage:
  - Put your key in `.env` as `OPENAI_API_KEY=...`
  - Install dependencies: `pip install -r requirements.txt`
  - Run: `python call_openai.py`
"""
import os
import sys
import json
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")


def call_chat(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    if not API_KEY:
        raise RuntimeError("OPENAI_API_KEY not set in environment or .env")

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 300,
        "temperature": 0.2,
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    try:
        return data["choices"][0]["message"]["content"].strip()
    except Exception:
        return json.dumps(data, indent=2)


def main() -> None:
    if not API_KEY:
        print("OPENAI_API_KEY not found. Please add it to .env or export it.")
        sys.exit(1)

    prompt = input("Enter prompt for the LLM: ")
    try:
        completion = call_chat(prompt)
        print("\n--- Response ---")
        print(completion)
    except Exception as e:
        print("Request failed:", e)


if __name__ == "__main__":
    main()
