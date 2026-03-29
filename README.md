# Gemini CLI Chat Orchestrator
[![Google AI](https://img.shields.io/badge/API-Google%20Gemini-4285F4)](https://ai.google.dev/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

## 💬 Project Overview
This repository contains a **Terminal-based AI Chatbot** powered by Google’s Gemini Pro. This implementation focuses on the core architecture of conversational AI: **State Management**. By manually orchestrating the chat history, this project demonstrates how to maintain a persistent dialogue where the model remembers and references previous user inputs throughout the session.

---

## 🛠️ Key Technical Implementations

### 1. Manual History Orchestration
* **Stateful Dialogue:** Implementing a list-based history buffer that stores every exchange, ensuring the LLM has the full context for every new response.
* **Role-Based Mapping:** Properly structuring messages with `user` and `model` roles to comply with the Google Generative AI API requirements.

### 2. Lightweight CLI Interface
* **Interactive Loop:** A robust `while True` loop that handles real-time user prompts and generates immediate AI feedback.
* **Session Controls:** Built-in commands to exit the program gracefully, ensuring a smooth developer experience.

### 3. Performance & Security
* **Efficient Payload Handling:** Sending only necessary conversation turns to manage token usage effectively.
* **Environment Security:** Protecting the `GOOGLE_API_KEY` using `.env` files and `python-dotenv` to avoid accidental credential leakage.

---

## 💻 Tech Stack
* **Language:** Python 3.9+
* **AI Model:** Google Gemini Pro
* **Library:** `google-generativeai`
* **Environment:** `python-dotenv`

