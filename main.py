import os 
from constants import openai_key
from langchain.llms import OpenAI
from langchain import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
import streamlit as st

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'input' not in st.session_state:
    st.session_state['input'] = ""

if 'store_session' not in st.session_state:
    st.session_state['store_session'] = []

def get_text():
    input_text = st.text_input("You: ",st.session_state["input"],key="input",placeholder="Hello, how may i help you")
    return input_text

st.title("Chat Bot❇️❇️")

os.environ["OPENAI_API_KEY"] = openai_key

llm = OpenAI(temperature=0)

#Conversational Memory:

if 'entity_memory' not in st.session_state:
    st.session_state.entity_memory = ConversationEntityMemory(llm = llm)

# Conversation Chain
conversation = ConversationChain(
    llm = llm,
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    memory=st.session_state.entity_memory
    )

user_input = get_text()

if user_input:
    response = conversation({'input':user_input})
    st.write(response['response'])
