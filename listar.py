import google.generativeai as genai

import api_key
import sys

genai.configure(api_key=api_key.API_KEY)  # Usa la API_KEY


for model in genai.list_models():
    print(model.name)
