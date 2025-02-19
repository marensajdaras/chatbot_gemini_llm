
import os

api_key = os.getenv("GEMINI_API_KEY")

import google.generativeai as genai

# set the API key globally
genai.configure(api_key = api_key)

model = genai.GenerativeModel("gemini-pro")


user_input = input("You: ")

response = model.generate_content(user_input)

print(response.text)

