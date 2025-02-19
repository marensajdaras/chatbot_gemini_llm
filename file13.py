import os
import google.generativeai as genai
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain


api_key = os.getenv("GEMINI_API_KEY")

# configuring the API key globally
genai.configure(api_key = api_key)

# variable for the model
model = genai.GenerativeModel("gemini-pro")

# initialize the memory
memory = ConversationBufferMemory() 


# using langchain class for creating a chain of interactions
conversation = ConversationChain(
    llm = model,
    verbose = True, # during the testing phase we need additionsal info 
    memory = memory 
)
# adding a loop to make a conversation with many prompts
while True:

    user_input = input("Human (type 'exit' to end conversation):")

    # we need  a break to exit the loop
    if user_input.lower() == "exit":

        break

    response = model.generate_content(user_input)

    print(response.text)
