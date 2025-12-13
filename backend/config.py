import os
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyDMLBjsOhmazET9Y_z4vxD2FBV86nda2HY"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
