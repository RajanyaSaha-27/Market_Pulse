from fastapi import FastAPI
import json
from news_fetcher import fetch_news
from sentiment_agent import analyze_sentiment

app = FastAPI()

@app.get("/analyze")
def analyze_market(ticker: str):
    news = fetch_news(ticker)
    sentiments = analyze_sentiment(ticker, news)

    scores = []
    final_output = {}

    for s in sentiments:
        data = json.loads(s)
        scores.append(data["score"])

    avg_score = sum(scores) / len(scores)

    sentiment_label = (
        "positive" if avg_score > 0.35 else
        "negative" if avg_score < -0.35 else
        "neutral"
    )

    final_output[ticker] = {
        "sentiment": sentiment_label,
        "score": round(avg_score, 2),
        "articles_analyzed": len(news)
    }

    return final_output
