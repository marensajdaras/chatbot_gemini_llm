import os
import google.generativeai as genai

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=api_key)

# Choose the model (e.g., Gemini Pro)
model = genai.GenerativeModel("gemini-pro")

def chat():
    print("🤖 Gemini Chatbot: Type 'exit' to stop chatting.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("🤖 Goodbye!")
            break
        
        # Send input to Gemini and get response
        response = model.generate_content(user_input)
        print("🤖 Gemini:", response.text, "\n")

# Start chatbot
chat()
