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
    ticker = ticker.upper()

    news = fetch_news(ticker)

    if not news:
        return {
            ticker: {
                "sentiment": "neutral",
                "score": 0.0,
                "articles_analyzed": 0
            }
        }

    results = analyze_sentiment(ticker, news)

    scores = []
    for r in results:
        try:
            s = float(r.get("score", 0.0))
            scores.append(s)
        except Exception:
            continue

    if not scores:
        avg_score = 0.0
    else:
        avg_score = round(sum(scores) / len(scores), 3)

    if avg_score > 0.15:
        sentiment_label = "positive"
    elif avg_score < -0.15:
        sentiment_label = "negative"
    else:
        sentiment_label = "neutral"

    return {
        ticker: {
            "sentiment": sentiment_label,
            "score": avg_score,
            "articles_analyzed": len(news)
        }
    }
