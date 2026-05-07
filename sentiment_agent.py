import json

from config import model
from utils import clean_text

def analyze_sentiment(ticker, headlines):
    combined_news = "\n".join(headlines)

    prompt = f"""
You are a financial sentiment analysis AI.

Analyze the following news headlines for {ticker}:

{combined_news}

Return ONLY JSON:

{{
  "sentiment": "positive | negative | neutral",
  "score": number between -1 and 1,
  "keywords": [],
  "summary": "overall market sentiment"
}}
"""

    try:
        response = model.generate_content(prompt)
        text = response.text

        start = text.find("{")
        end = text.rfind("}") + 1
        clean_json = text[start:end]

        return [clean_json]

    except Exception as e:
        return [json.dumps({
            "sentiment": "neutral",
            "score": 0.0,
            "keywords": [],
            "summary": "Gemini failed"
        })]
    
# def analyze_sentiment(ticker, headlines):
#     results = []

#     for news in headlines:
#         cleaned = clean_text(news)

#         # prompt = f"""
#         # You are a financial market sentiment analysis agent.

#         # Analyze the following market-related news headline:

#         # "{cleaned}"

#         # Tasks:
#         # 1. Determine sentiment: positive, negative, or neutral
#         # 2. Give a sentiment score between -1 and +1
#         # 3. Extract 2-3 finance-related keywords
#         # 4. Give one-line explanation

#         # Respond ONLY in JSON:
#         # {{
#         #   "sentiment": "",
#         #   "score": 0.0,
#         #   "keywords": [],
#         #   "summary": ""
#         # }}
#         # """
#         prompt = f"""
# Analyze this financial news headline:

# "{cleaned}"

# Return ONLY valid JSON. No explanation, no extra text.

# Format:
# {{
#   "sentiment": "positive" or "negative" or "neutral",
#   "score": number between -1 and 1,
#   "keywords": ["word1", "word2"],
#   "summary": "short explanation"
# }}
# """
#         try:
#             response = model.generate_content(prompt)
#             text = response.text

#             print("Gemini raw:", text)
#         except Exception as e:
#             # Gemini failed → fallback
#             results.append(json.dumps({
#                 "sentiment": "neutral",
#                 "score": 0.0,
#                 "keywords": [],
#                 "summary": "Gemini API failed"
#             }))
#             continue

#         try:
#             start = text.find("{")
#             end = text.rfind("}") + 1

#             if start != -1 and end != -1:
#                 clean_json = text[start:end]
#                 parsed = json.loads(clean_json)

#                 parsed["score"] = float(parsed.get("score", 0.0))

#                 results.append(json.dumps(parsed))
#             else:
#                 raise ValueError("No JSON found")

#         except Exception as e:
#             print("❌ JSON parse failed:", text)

#     results.append(json.dumps({
#         "sentiment": "neutral",
#         "score": 0.0,
#         "keywords": [],
#         "summary": "Parsing failed"
#     }))

#     return results
