# chatbot_gemini_llm
Creating a chatbot with google open source llm
# First you have to get an google api key with which you are going to access the models 
# You can create one in Google AI Studio
-> file11.py is one loop conversation with the gemini model, a simple way to connect with the model with an api key

-> file12.py is with many loops, so you can create a full conversation with the ai agent (gemini model) and can exit the loop with keyword 'exit'

-> file13.py is an updated version of file12.py, but with added memory and with a new conversation chain to create an chain of interactions with ai agent (it has an error with the runnable instance of the model)

-> file17.py is a simple version using the ChatGoogleGenerativeAI that is operative without error, this will help me to build an ai agent that has also memory. The previous ai agents build on generativeai module are operative without any error but is very difficult to build the memory part. 

-> file17.py is fully updated with usage of ConversationBufferMemory for memory of AI Agent, now you can make a normal conversation because the AI Agent has memory of previous prompts and the conversation makes sense.

-> file_interface.py is the most complete version till now with interface using streamlit

-> PNG files show that the ai agent function and that the ai agent has memory to give better convenient answers 
