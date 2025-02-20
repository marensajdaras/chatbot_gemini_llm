from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from langchain.chains import LLMChain, ConversationChain

from langchain_google_genai import ChatGoogleGenerativeAI

import os

api_key = os.getenv("GEMINI_API_KEY")

chat = ChatGoogleGenerativeAI(model = "gemini-1.5-pro", google_api_key = api_key) # "gemini-pro"

# user_input = input("Human (type 'exit' to end conversation): ")



# Instead of __call__, use invoke to generate the response
# response = chat.invoke(user_input)

# print(response.content)


messages = [

    ("system", "You are a helpful assistant that translates English to French. Translate the user sentence."),
    ("human", "I love programming."),


    ]

# ai_msg = chat.invoke(messages)

# print(ai_msg.content)

from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm = chat,
    verbose = True,
    memory = memory,
)

# a = conversation.run("Hi there Gemini how are you?")

# print(a)


while True:

    query = input('you:  ')

    if query == 'exit':
        break

    output = conversation({'input': query})

    print('AI Agent: ', output['response'])


    

    



