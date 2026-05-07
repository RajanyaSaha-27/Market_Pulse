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
