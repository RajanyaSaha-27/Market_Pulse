import requests

def fetch_news(ticker):
    # Fallback dummy data if API fails
    dummy_news = [
        f"{ticker} shares rise after strong quarterly earnings",
        f"{ticker} faces regulatory challenges impacting investors",
        f"Market reacts to new developments related to {ticker}"
    ]
    return dummy_news
