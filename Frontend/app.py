import streamlit as st
import requests

st.set_page_config(page_title="MarketPulse", layout="centered")

st.title("📊 MarketPulse – AI Market Sentiment")

ticker = st.text_input("Enter Market Ticker (AAPL, TSLA, BTC, NIFTY)")

if st.button("Analyze Sentiment"):
    response = requests.get(
        f"http://127.0.0.1:8000/analyze?ticker={ticker}"
    )
    data = response.json()[ticker]

    st.subheader(f"Sentiment for {ticker}")

    color = (
        "🟢" if data["sentiment"] == "positive" else
        "🔴" if data["sentiment"] == "negative" else
        "🟡"
    )

    st.markdown(f"### {color} {data['sentiment'].upper()}")
    st.metric("Sentiment Score", data["score"])
    st.text(f"Articles Analyzed: {data['articles_analyzed']}")

