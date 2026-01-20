import google.generativeai as genai
import os
from google.generativeai import types

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_INSTRUCTION = (
    "You are a professional financial analyst. "
    "MANDATORY: You must use Google Search to find TODAY'S stock news and price action. "
    "If there is any directional trend in the last 24 hours, you MUST choose positive or negative. "
    "Do not return 0.0 unless there is absolutely no news for the ticker."
)

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash", 
    system_instruction=SYSTEM_INSTRUCTION,
    tools=[{"google_search": {}}] 
)

generation_config = {
    "temperature": 1.0, 
    "response_mime_type": "application/json"
}

def get_sentiment(ticker):
    prompt = f"Analyze the real-time sentiment for ticker: {ticker}. Use current market data."
    
    response = model.generate_content(
        prompt,
        generation_config=generation_config
    )
    
    return response.text
