# Chatbot with Conversation History

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![Google Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-4285F4)
![Generative AI](https://img.shields.io/badge/Domain-Generative%20AI-purple)

A Python-based command-line chatbot powered by Google Gemini and LangChain that maintains conversation history across multiple turns. The project demonstrates how conversational memory, streaming responses, and model fallback logic can improve the interaction between users and large language models.

## 📌 Project Overview

Most basic chatbots process each prompt independently. This project takes a different approach by maintaining a conversation history and passing previous messages to the model when generating a response.

The chatbot runs directly in the terminal and supports interactive conversations, viewing previous messages, streaming generated responses, and exiting the session.

## ✨ Key Features

### 1. Conversation History
- Maintains a list of messages throughout the current session.
- Uses LangChain's `HumanMessage` and `AIMessage` objects to distinguish user inputs from AI responses.
- Provides conversation context to the model for more coherent multi-turn interactions.

### 2. Interactive Command-Line Interface
- Accepts user prompts through a continuous input loop.
- Supports the `history` command to display previous messages.
- Supports the `exit` command to end the conversation.

### 3. Streaming AI Responses
- Displays generated text incrementally instead of waiting for the entire response.
- Accumulates streamed content before adding the completed AI response to the conversation history.

### 4. Gemini Model Fallback
- Configures a primary Gemini model and a backup model.
- Attempts to switch models when certain service-busy (`503`) or rate-limit (`429`) errors occur.
- Helps demonstrate basic error-handling strategies for LLM applications.

### 5. Environment Configuration
- Loads environment variables using `python-dotenv`.
- Keeps API credentials outside the main Python source code.

## 🧰 Tech Stack

- **Language:** Python
- **LLM Provider:** Google Gemini
- **LLM Integration:** `langchain-google-genai`
- **Conversation Messages:** `langchain-core`
- **Environment Variables:** `python-dotenv`

## ⚙️ How It Works

1. The application loads environment variables.
2. It initializes an empty conversation-history list.
3. The user enters a prompt in the terminal.
4. The prompt is stored as a `HumanMessage`.
5. The chatbot sends the conversation history to Gemini.
6. The model generates a streamed response.
7. The completed response is stored as an `AIMessage`.
8. The user can continue chatting, view the history, or exit.

## 🚀 Getting Started

### Prerequisites

- Python installed on your system.
- A Google Gemini API key with access to a supported model.
- Internet connectivity.

### 1. Clone the Repository

```bash
git clone https://github.com/mani787060/chatbot_with_history.git
cd chatbot_with_history
```

### 2. Install Dependencies

```bash
pip install langchain-google-genai langchain-core python-dotenv
```

### 3. Configure the API Key

Create a `.env` file in the project directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Ensure that `.env` is included in `.gitignore` so that your credentials are not uploaded to GitHub.

### 4. Run the Chatbot

```bash
python 4_chatbot_with_history.py
```

Use the following commands during a session:

| Command | Purpose |
|---|---|
| `history` | Displays previous conversation messages |
| `exit` | Ends the chatbot session |

## 🧠 Concepts Demonstrated

- Multi-turn conversations with LLMs
- Conversation state and message history
- LangChain message objects
- Streaming text generation
- Gemini model integration
- Basic API error handling and model fallback
- Secure API-key configuration

## 🔮 Future Improvements

- Add conversation-history limits or summarization to control token usage.
- Implement retries with exponential backoff for temporary API failures.
- Add a graphical interface using Streamlit.
- Support saving and restoring conversations between sessions.
- Add configurable system instructions and conversation settings.
- Add automated tests for history management and error handling.

## 🎯 Learning Outcomes

This project provides practical experience with conversational LLM applications and demonstrates how message history can be used to maintain context across multiple interactions. It also introduces streaming output, environment-based configuration, and a basic fallback strategy for handling selected API errors.
