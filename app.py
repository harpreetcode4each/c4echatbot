import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(page_title="Code4each Chatbot", page_icon="🤖", layout="wide")

# Custom CSS for better UI
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .chat-message.user {
        background-color: #2b313e;
        color: #ffffff;
    }
    .chat-message.bot {
        background-color: #475063;
        color: #ffffff;
    }
    .chat-message .avatar {
        width: 20%;
    }
    .chat-message .content {
        width: 80%;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize the chatbot
@st.cache_resource
def get_chatbot():
    llm = ChatOpenAI(
        temperature=0.7,
        model="gpt-3.5-turbo"
    )
    conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory(),
        verbose=True
    )
    return conversation

# Check for API key
if not os.getenv("OPENAI_API_KEY"):
    st.error("Please set your OPENAI_API_KEY in the .env file")
    st.stop()

# Title and description
st.title("🤖 Code4each Chatbot")
st.markdown("""
This is an advanced Code4each Chatbot powered by OpenAI's GPT model. 
You can have a natural conversation with it, and it will remember the context of your chat.
""")

# Sidebar
with st.sidebar:
    st.title("About")
    st.markdown("""
    This chatbot uses:
    - OpenAI's GPT-3.5-turbo model
    - LangChain for conversation management
    - Streamlit for the web interface
    """)
    
    st.title("Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1,
                          help="Higher values make the output more creative, lower values make it more deterministic")

# Chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's on your mind?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get chatbot response
    chatbot = get_chatbot()
    response = chatbot.predict(input=prompt)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using code4each Chatbot")
