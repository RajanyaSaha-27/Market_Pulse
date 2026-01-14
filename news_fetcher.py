import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(ticker):
    if not NEWS_API_KEY:
        return []

    query = f"{ticker} stock market OR {ticker} shares OR {ticker} index"

    url = (
        "https://newsapi.org/v2/everything?"
        f"q={query}&"
        "language=en&"
        "sortBy=publishedAt&"
        "pageSize=5&"
        f"apiKey={NEWS_API_KEY}"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        articles = data.get("articles", [])

        headlines = []
        for a in articles:
            title = a.get("title", "")
            desc = a.get("description", "")

            text = f"{title}. {desc}".strip()
            if len(text) > 40:
                headlines.append(text)

        return headlines

    except Exception:
        return []
