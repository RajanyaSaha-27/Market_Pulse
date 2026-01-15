import json
from config import model
from utils import clean_text


def analyze_sentiment(ticker, headlines):
    results = []

    for news in headlines:
        cleaned = clean_text(news)

        prompt = f"""
You are a financial analyst.

Based on input ticker , do followings on real time data.

Rules:
- You MUST choose positive or negative if there is ANY directional signal
- Use neutral ONLY if completely balanced
- Scores must NOT be zero unless truly neutral

Return JSON ONLY:
{{
  "sentiment": "positive | negative | neutral",
  "score": number between -1 and 1 (non-zero if not neutral)
}}
"""

        try:
            response = model.generate_content(prompt)
            data = json.loads(response.text)

            score = float(data.get("score", 0.0))
            score = max(-1.0, min(1.0, score))

            sentiment = data.get("sentiment", "neutral").lower()
            if sentiment not in ["positive", "negative", "neutral"]:
                sentiment = "neutral"

            results.append({
                "sentiment": sentiment,
                "score": score
            })
            print(result)

        except Exception:
            results.append({
                "sentiment": "neutral",
                "score": 0.0
            })

    return results
