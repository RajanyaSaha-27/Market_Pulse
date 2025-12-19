import json
from Market_Pulse.config import model
from Market_Pulse.utils import clean_text

def analyze_sentiment(ticker, headlines):
    results = []
    for news in headlines:
        cleaned = clean_text(news)

        prompt = f"""
        You are a financial market sentiment analysis agent.

        Analyze the following market-related news headline:

        "{cleaned}"

        Tasks:
        1. Determine sentiment: positive, negative, or neutral
        2. Give a sentiment score between -1 and +1
        3. Extract 2-3 finance-related keywords
        4. Give one-line explanation

        Respond ONLY in JSON:
        {{
          "sentiment": "",
          "score": 0.0,
          "keywords": [],
          "summary": ""
        }}
        """

        # response = model.generate_content(prompt)
        # results.append(response.text)
        try:
            response = model.generate_content(prompt)
            text = response.text
        except Exception as e:
            # Gemini failed → fallback
            results.append(json.dumps({
                "sentiment": "neutral",
                "score": 0.0,
                "keywords": [],
                "summary": "Gemini API failed"
            }))
            continue

        import re
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            results.append(match.group())
        else:
            results.append(json.dumps({
                "sentiment": "neutral",
                "score": 0.0,
                "keywords": [],
                "summary": "Invalid Gemini response"
            }))
    return results
