
import os
from dotenv import load_dotenv
from groq import Groq
import datetime

# Dictionary to store chat history for each user
chat_histories = {}

def aigeneration(userinput, user_id=None):
    load_dotenv()

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    # If no user_id provided, use a default
    if user_id is None:
        user_id = "default_user"
    
    # Initialize chat history for new users
    if user_id not in chat_histories:
        chat_histories[user_id] = [
            {
                "role": "system",
                "content": """You are a discord bot called XIV Bot, a test bot made by Armaans_YT 
                and are an AI utility bot to serve the community.You were founded on the 14th of December 2024, 
                Powered by Groq. Be inquisitive and cool bot. refer to the user by their username. Do not have long answers, have short answers where applicable, and long answers when the content is deep."""
            }
        ]
    
    # Add the new user message to the conversation history
    chat_histories[user_id].append({
        "role": "user",
        "content": f"{userinput} messaged by user at {datetime.datetime.now()} UTC time."
    })

    try:
        chat_completion = client.chat.completions.create(
            messages=chat_histories[user_id],
            model="llama3-8b-8192",
            temperature=0.8,
            max_tokens=8192,
            timeout=30,  # Add timeout to prevent hanging
        )
    except Exception as e:
        print(f"Groq API error: {e}")
        return "I'm experiencing technical difficulties. Please try again later."

    response_content = chat_completion.choices[0].message.content
    
    # Add the assistant's response to the conversation history
    chat_histories[user_id].append({
        "role": "assistant",
        "content": response_content,
    })

    return response_content

def clear_user_history(user_id):
    """Clear chat history for a specific user"""
    if user_id in chat_histories:
        del chat_histories[user_id]

def clear_all_histories():
    """Clear all chat histories"""
    global chat_histories
    chat_histories = {}
