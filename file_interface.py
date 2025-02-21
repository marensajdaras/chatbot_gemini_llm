import streamlit as st

import os 

from langchain.chains import LLMChain, ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory

st.set_page_config(page_title = "AIAgent", page_icon="@")
st.header('@ Welcome to AI Assistant, you can ask everything that can help you.')

api_key = os.getenv("GEMINI_API_KEY")


chat = ChatGoogleGenerativeAI(model = "gemini-1.5-pro",
                              google_api_key = api_key)

# memory = ConversationBufferMemory()

if "memory" not in st.session_state:

    st.session_state.memory = ConversationBufferMemory()

conversation = ConversationChain(

    llm = chat,
    verbose = True,
    # memory = memory,
    memory = st.session_state.memory

    )

# Store chat history in Streamlit session state if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.text_input("You:", key=f"user_input_{len(st.session_state.messages)}", placeholder="Type your message here...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get AI response
    response = conversation.run(user_input)
    
    # Store AI response
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Clear input field
    st.text_input("You:", "", key="user_input", placeholder="Type your message here...")


    
