import requests
import xml.etree.ElementTree as ET
import urllib.parse

def fetch_news(ticker):
    try:
        query = urllib.parse.quote(f"{ticker} stock")
        url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

        response = requests.get(url, timeout=5)
        root = ET.fromstring(response.content)

        headlines = []

        for item in root.findall(".//item"):
            title = item.find("title").text
            
            if title:
                headlines.append(title)

            if len(headlines) == 5:
                break

        # print("Fetched headlines:", headlines)  # debug

        return headlines

    except Exception as e:
        print("❌ Error:", e)
        return [
            f"{ticker} market shows mixed signals",
            f"Investors cautious about {ticker}",
            f"{ticker} performance uncertain"
        ]

# import feedparser

# def fetch_news(ticker):
#     dummy_news = [
#         f"{ticker} shares rise after strong quarterly earnings",
#         f"{ticker} faces regulatory challenges impacting investors",
#         f"Market reacts to new developments related to {ticker}"
#     ]

#     try:
#         query = f"{ticker}+stock"
#         url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

#         print("URL:", url)

#         feed = feedparser.parse(url)

#         print("Feed entries length:", len(feed.entries))  # 👈 VERY IMPORTANT

#         headlines = [entry.title for entry in feed.entries[:5]]

#         if not headlines:
#             print("⚠️ No headlines extracted")
#             return dummy_news

#         return headlines

#     except Exception as e:
#         print("❌ Error:", e)
#         return dummy_news

# def fetch_news(ticker):
#     # Fallback dummy data if API fails
#     dummy_news = [
#         f"{ticker} shares rise after strong quarterly earnings",
#         f"{ticker} faces regulatory challenges impacting investors",
#         f"Market reacts to new developments related to {ticker}"
#     ]
#     return dummy_news


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
