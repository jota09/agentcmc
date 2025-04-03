import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
LLM_MODEL = os.environ.get("LLM_MODEL","YOUR_LLM_MODEL")
LLM_API_KEY = os.environ.get("LLM_API_KEY","YOUR_LLM_API_KEY")
LLM_ENDPOINT = os.environ.get("LLM_ENDPOINT","YOUR_LLM_URL")

# Template for structuring the question before sending it to the chat model
PROMPT_TEMPLATE = """
Answer the following question:
If I ask you, "{question}" and I ask you to tell me in one word the lowercase name of the cryptocurrency being referenced, what would you answer?
"""

def find_symbol(questionprompt: str):
    prompt = PROMPT_TEMPLATE.format(question=questionprompt)
    response = query_llm_chat(prompt)
    return response

def query_llm_chat(prompt: str):
    payload = json.dumps({
        "model": LLM_MODEL,
        "messages": [
            {
            "role": "user",
            "content": prompt
            }
        ],
        "temperature": 0,
        "stream": False,
        "max_tokens": 0
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer '+LLM_API_KEY
    }

    response = requests.request("POST", LLM_ENDPOINT, headers=headers, data=payload)
    data = response.json()

    try:
        symbol = data["choices"][0]["message"]["content"]
    except:
        symbol = f"Failed to retrieve object"

    return symbol
