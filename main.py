from fastapi import FastAPI
import json

from Market_Pulse.news_fetcher import fetch_news
from Market_Pulse.sentiment_agent import analyze_sentiment

app = FastAPI(title="Market Pulse API")


# ✅ Health check
@app.get("/")
def root():
    return {
        "message": "Market Pulse backend running",
        "usage": "/analyze?ticker=AAPL"
    }


# ✅ Actual API
@app.get("/analyze")
def analyze_market(ticker: str):
    news = fetch_news(ticker)

    sentiments = analyze_sentiment(ticker, news)

    scores = []
    for s in sentiments:
        try:
            data = json.loads(s)
            scores.append(float(data.get("score", 0)))
        except Exception:
            scores.append(0)

    avg_score = sum(scores) / len(scores) if scores else 0
    
    sentiment_label = (
        "positive" if avg_score > 0.35 else
        "negative" if avg_score < -0.35 else
        "neutral"
    )

    return {
        ticker.upper(): {
            "sentiment": sentiment_label,
            "score": round(avg_score, 2),
            "articles_analyzed": len(news)
        }
    }






# from fastapi import FastAPI
# import json

# from Market_Pulse.news_fetcher import fetch_news
# from Market_Pulse.sentiment_agent import analyze_sentiment

# app = FastAPI(title="Market Pulse API")

# @app.get("/")
# def root():
#     return {"message": "Market Pulse backend running"}

# @app.get("/analyze")
# def analyze_market(ticker: str):
#     ticker = ticker.strip().upper()

#     news = fetch_news(ticker)
#     sentiments = analyze_sentiment(ticker, news)

#     data = json.loads(sentiments[0])

#     return {
#         ticker: {
#             "sentiment": data["sentiment"],
#             "score": round(float(data["score"]), 2),
#             "articles_analyzed": data.get("articles_analyzed", 0),
#             "summary": data.get("summary", "")
#         }
#     }
