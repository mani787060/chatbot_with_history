
import os  
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage  # Added for chat history
from dotenv import load_dotenv

load_dotenv()

# Using the most stable 2026 model with fallback logic
MODELS = ["gemini-3.1-flash-lite-preview", "gemini-3-flash-preview"]

# Initialize an empty list for chat history
chat_history = []

print("--- Chatbot with Memory Started ---")
print("(Type 'history' to see previous messages or 'exit' to quit)")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'exit':
        break

    # --- NEW ADDITION: Print Chat History ---
    if user_input.lower() == 'history':
        print("\n---📜 Full Chat History ---")
        for msg in chat_history:
            role = "👤 You" if isinstance(msg, HumanMessage) else "🤖 AI"
            print(f"{role}: {msg.content}")
        print("--------------------------")
        continue # Skip the AI call and ask for input again
    # ----------------------------------------

    
    # 1. Add User message to history
    chat_history.append(HumanMessage(content=user_input))
    
    success = False
    for model_name in MODELS:
        if success: break
        
        try:
            model = ChatGoogleGenerativeAI(model=model_name)
            print(f"AI ({model_name}): ", end="", flush=True)
            
            full_response = ""
            # 2. Pass the entire chat_history list to the model
            for chunk in model.stream(chat_history):
                content = chunk.content
                # Handle potential list format from newer Gemini models
                if isinstance(content, list):
                    content = "".join([p.get('text', '') for p in content if isinstance(p, dict)])
                
                print(content, end="", flush=True)
                full_response += content
            
            # 3. Add AI response to history
            chat_history.append(AIMessage(content=full_response))
            print()
            success = True
            
        except Exception as e:
            if "503" in str(e) or "429" in str(e):
                print(f"\n[System Busy] Trying backup model...")
                continue # Try next model in the list
            else:
                print(f"\nAI Error: {e}")
                break

            

