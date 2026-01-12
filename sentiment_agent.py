import json
import re
from config import model
from utils import clean_text


def analyze_sentiment(ticker, headlines):
    results = []

    for news in headlines:
        cleaned = clean_text(news)

        prompt = f"""
You are a financial market sentiment analysis agent.

Analyze the following market-related news headline:

"{cleaned}"

Tasks:
1. Determine sentiment: Positive, Negative, or Neutral
2. Give a sentiment score between -1 and +1
3. Extract 2-3 finance-related keywords
4. Give one-line explanation

Respond ONLY in valid JSON:
{{
  "sentiment": "Positive | Negative | Neutral",
  "score": number,
  "keywords": [],
  "summary": ""
}}"""



        try:
            response = model.generate_content(prompt)
            text = response.text
        except Exception:
            results.append({
                "sentiment": "Neutral",
                "score": 0.0,
                "keywords": [],
                "summary": "Gemini API failed"
            })
            continue

        match = re.search(r"\{.*\}", text, re.DOTALL)

        if not match:
            results.append({
                "sentiment": "Neutral",
                "score": 0.0,
                "keywords": [],
                "summary": "Invalid Gemini response"
            })
            continue

        try:
            parsed = json.loads(match.group())

            # Normalize sentiment
            sentiment = parsed.get("sentiment", "Neutral").capitalize()
            if sentiment not in ["Positive", "Negative", "Neutral"]:
                sentiment = "Neutral"

            # Normalize score
            score = float(parsed.get("score", 0.0))
            score = max(-1.0, min(1.0, score))

            results.append({
                "sentiment": sentiment,
                "score": score,
                "keywords": parsed.get("keywords", []),
                "summary": parsed.get("summary", "")
            })

        except Exception:
            results.append({
                "sentiment": "Neutral",
                "score": 0.0,
                "keywords": [],
                "summary": "JSON parse error"
            })

    return results
