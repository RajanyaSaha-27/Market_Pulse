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

Return ONLY valid JSON in this format:
{{
  "sentiment": "Positive | Negative | Neutral",
  "score": number between -1 and 1
}}
"""

        try:
            response = model.generate_content(prompt)
            text = response.text
        except Exception:
            results.append({"sentiment": "Neutral", "score": 0.0})
            continue

        match = re.search(r"\{.*\}", text, re.DOTALL)

        if not match:
            results.append({"sentiment": "Neutral", "score": 0.0})
            continue

        try:
            parsed = json.loads(match.group())

            sentiment = parsed.get("sentiment", "Neutral").capitalize()
            if sentiment not in ["Positive", "Negative", "Neutral"]:
                sentiment = "Neutral"

            score = float(parsed.get("score", 0.0))
            score = max(-1.0, min(1.0, score))

            results.append({
                "sentiment": sentiment,
                "score": score
            })

        except Exception:
            results.append({"sentiment": "Neutral", "score": 0.0})

    return results
