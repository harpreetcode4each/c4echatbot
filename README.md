# Code4each Chatbot with LangChain and OpenAI

This is a simple chatbot application that uses OpenAI's GPT model through the LangChain framework. The chatbot maintains conversation memory and can engage in natural language interactions.

## Features

- Uses OpenAI's GPT-3.5-turbo model
- Maintains conversation context using LangChain's memory
- Simple command-line interface
- Configurable temperature for response creativity

## Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up OpenAI API Key**
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - You can get an API key from [OpenAI's website](https://platform.openai.com/api-keys)

3. **Run the Chatbot**
   ```bash
   python chatbot.py
   ```

## How to Use

1. Start the application using the command above
2. Type your message and press Enter
3. The AI will respond to your message
4. Type 'quit' to exit the conversation

## Code Structure

- `chatbot.py`: Main application file containing the chatbot logic
- `requirements.txt`: List of required Python packages
- `.env`: Configuration file for API keys (create this file yourself)

## Dependencies

- openai: For interacting with OpenAI's API
- langchain: Framework for building LLM applications
- python-dotenv: For loading environment variables
- langchain-openai: OpenAI integration for LangChain 