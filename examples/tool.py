import openai
import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

def get_openai_key():
    _ = load_dotenv(find_dotenv())
    return os.environ['OPENAI_API_KEY']

api_key = get_openai_key()
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

def get_completion(prompt, model="deepseek-chat"):
    messages = [
                   {"role": "user", "content": prompt}
               ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=4096,
        temperature=0,
        stream=False
    )
    return response.choices[0].message.content

def get_completion_from_messages(messages, model="deepseek-chat", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=4096,
        temperature=temperature,
        stream=False
    )
    return response.choices[0].message.content

