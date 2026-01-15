import google.generativeai as genai
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  

genai.configure(api_key=GEMINI_API_KEY)

tools_config = [
    {"google_search_retrieval": {}} 
]
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    tools=tools_config,
    generation_config={
        "temperature": 1.0,
        "response_mime_type": "application/json"  
    },
    system_instruction="You are a decisive financial analyst. Evaluate real-time data. You MUST choose positive or negative if there is ANY directional signal. Use neutral ONLY if completely balanced. Scores must NOT be zero unless truly neutral."
)
