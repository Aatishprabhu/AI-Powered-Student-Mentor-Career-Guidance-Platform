import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
GENIE_MODEL = 'gemini-2.5-flash'

def get_gemini_response(prompt, system_instruction="You are a helpful career mentor for students."):
    model = genai.GenerativeModel(
        model_name=GENIE_MODEL,
        system_instruction=system_instruction
    )
    response = model.generate_content(prompt)
    return response.text

def get_chat_response(conversation_history, new_message):
    model = genai.GenerativeModel(GENIE_MODEL)
    chat = model.start_chat(history=conversation_history)
    response = chat.send_message(new_message)
    return response.text