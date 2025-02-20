from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from langchain.chains import LLMChain, ConversationChain

from langchain_google_genai import ChatGoogleGenerativeAI

import os

api_key = os.getenv("GEMINI_API_KEY")

chat = ChatGoogleGenerativeAI(model = "gemini-pro", google_api_key = api_key)

user_input = input("Human (type 'exit' to end conversation): ")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "I'm going to Rome for 2 days, what can I visit?"}
]

# Instead of __call__, use invoke to generate the response
response = chat.invoke(user_input)

print(response.content)



