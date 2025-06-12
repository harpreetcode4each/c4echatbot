import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()

def create_chatbot():
    # Initialize the ChatOpenAI model
    llm = ChatOpenAI(
        temperature=0.7,  # Controls randomness: 0 is deterministic, 1 is creative
        model="gpt-3.5-turbo"  # You can also use "gpt-4" if you have access
    )
    
    # Create a conversation chain with memory
    conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory(),
        verbose=True
    )
    
    return conversation

def main():
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set your OPENAI_API_KEY in the .env file")
        return
    
    # Create chatbot
    chatbot = create_chatbot()
    
    print("Welcome to the Code4each Chatbot! Type 'quit' to exit.")
    print("-------------------------------------------")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Get response from the chatbot
        response = chatbot.predict(input=user_input)
        print("\nAI:", response)

if __name__ == "__main__":
    main() 