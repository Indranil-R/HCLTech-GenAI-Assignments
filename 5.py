# 5. create a simple python program to print the list of models in ChatGPT, Gemini and hugging face?

import os
from dotenv import load_dotenv

load_dotenv()

# ChatGPT models
from openai import OpenAI

client = OpenAI()
openai_models = client.models.list()

print("Chat GPT Models are:")
for model in openai_models:
    print(model)

# Gemini models

from google import genai

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
gemini_models = client.models.list()

print("\nGemini Models are:")
for model in gemini_models:
    print(model)

# Hugging Face models

from huggingface_hub import HfApi

api = HfApi()
huggingface_models = api.list_models()

print("\nHugging Face Models are:")
for model in huggingface_models:
    print(model)
