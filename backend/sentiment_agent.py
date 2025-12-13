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

        response = model.generate_content(prompt)
        results.append(response.text)

    return results
