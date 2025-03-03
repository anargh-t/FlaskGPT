import requests
from config import Config

def get_ai_response(model, prompt):
    if model == "chatgpt":
        return call_openai(prompt)
    elif model == "deepseek":
        return call_deepseek(prompt)
    elif model == "gemini":
        return call_gemini(prompt)
    else:
        return "Invalid model selection."

def call_openai(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {Config.OPENAI_API_KEY}"}
    data = {"model": "gpt-4", "messages": [{"role": "user", "content": prompt}]}
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response.")

def call_deepseek(prompt):
    url = "https://api.deepseek.com/chat"
    headers = {"Authorization": f"Bearer {Config.DEEPSEEK_API_KEY}"}
    data = {"prompt": prompt}
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("response", "No response.")

def call_gemini(prompt):
    url = "https://api.gemini.com/v1/chat"
    headers = {"Authorization": f"Bearer {Config.GEMINI_API_KEY}"}
    data = {"input": prompt}
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("content", "No response.")
