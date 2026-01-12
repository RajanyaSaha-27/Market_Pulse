import json
import re
from config import model
from utils import clean_text


def analyze_sentiment(ticker, headlines):
    results = []

    for news in headlines:
        cleaned = clean_text(news)

        prompt = f"""
Analyze the financial news headline below.

Headline:
"{cleaned}"

Return ONLY valid JSON:
{{
  "sentiment": "positive | negative | neutral",
  "score": number between -1 and 1
}}
"""

        try:
            response = model.generate_content(prompt)
            text = response.text
        except Exception:
            results.append({"sentiment": "neutral", "score": 0.0})
            continue

        match = re.search(r"\{.*\}", text, re.DOTALL)

        if not match:
            results.append({"sentiment": "neutral", "score": 0.0})
            continue

        try:
            data = json.loads(match.group())
            score = float(data.get("score", 0.0))
            score = max(-1.0, min(1.0, score))

            sentiment = data.get("sentiment", "neutral").lower()
            if sentiment not in ["positive", "negative", "neutral"]:
                sentiment = "neutral"

            results.append({
                "sentiment": sentiment,
                "score": score
            })

        except Exception:
            results.append({"sentiment": "neutral", "score": 0.0})

    return results
