import requests

def fetch_news(ticker):
    # Fallback dummy data if API fails
    dummy_news = [
        f"{ticker} shares rise after strong quarterly earnings",
        f"{ticker} faces regulatory challenges impacting investors",
        f"Market reacts to new developments related to {ticker}"
    ]
    return dummy_news

# import feedparser

# def fetch_news(ticker):
#     feed = feedparser.parse(
#         f"https://news.google.com/rss/search?q={ticker}+market"
#     )

#     headlines = []
#     for entry in feed.entries[:5]:
#         headlines.append(entry.title)

#     return headlines if headlines else [
#         f"{ticker} market news unavailable"
#     ]
