from fastapi import FastAPI
from news_fetcher import fetch_news
from sentiment_agent import analyze_sentiment

app = FastAPI(title="Market Pulse API")


@app.get("/")
def root():
    return {
        "message": "Market Pulse backend running",
        "usage": "/analyze?ticker=AAPL"
    }


@app.get("/analyze")
def analyze_market(ticker: str):
    news = fetch_news(ticker)
    results = analyze_sentiment(ticker, news)

    scores = [r["score"] for r in results if isinstance(r.get("score"), (int, float))]

    if not scores:
        avg_score = 0.0
    else:
        avg_score = round(sum(scores) / len(scores), 2)

    if avg_score > 0.15:
        sentiment_label = "positive"
    elif avg_score < -0.15:
        sentiment_label = "negative"
    else:
        sentiment_label = "neutral"

    return {
        ticker.upper(): {
            "sentiment": sentiment_label,
            "score": avg_score,
            "articles_analyzed": len(news)
        }
    }
