import os

api_key = os.getenv("GEMINI_API_KEY")

import google.generativeai as genai

# configuring the API key globally
genai.configure(api_key = api_key)


model = genai.GenerativeModel("gemini-pro")


# adding a loop to make a conversation with many prompts
while True:
    
    user_input = input("Human (type 'exit' to end conversation):")
    
    # we need  a break to exit the loop
    if user_input.lower() == "exit":
        break
    
    response = model.generate_content(user_input)
    
    print(response.text)
