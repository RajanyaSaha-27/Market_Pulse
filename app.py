import streamlit as st
import requests
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd
import random

st.set_page_config(
    page_title="MarketPulse | AI Sentiment",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Gradient Background */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(15, 23, 42) 0%, rgb(0, 0, 0) 90%);
    }

    /* Glassmorphism Card */
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        text-align: center;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: rgba(56, 189, 248, 0.5);
    }

    /* Typography */
    .big-stat {
        font-size: 36px;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #22c55e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .label-stat {
        font-size: 14px;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Input & Button Styling */
    div[data-testid="stTextInput"] input {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
        border-radius: 8px;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #0ea5e9, #22c55e);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        width: 100%;
    }
    div.stButton > button:hover {
        box-shadow: 0 0 15px rgba(34, 197, 94, 0.4);
    }
    
    /* Footer */
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: rgba(15, 23, 42, 0.9); color: #64748b;
        text-align: center; padding: 10px; font-size: 12px;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
    }
</style>
""", unsafe_allow_html=True)

BACKEND_URL = "http://127.0.0.1:8000/analyze"

if "history" not in st.session_state:
    st.session_state.history = []

def get_color(score):
    if score > 0.3: return "#22c55e" # Green
    if score < -0.3: return "#ef4444" # Red
    return "#eab308" # Yellow

def render_metric_card(label, value, prefix="", suffix=""):
    st.markdown(f"""
    <div class="metric-card">
        <div class="label-stat">{label}</div>
        <div class="big-stat">{prefix}{value}{suffix}</div>
    </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ⚡ MarketPulse")
    st.caption("AI-Powered Financial Intelligence")
    st.markdown("---")
    
    MOCK_MODE = st.checkbox("🔮 Demo Mode (Mock Data)", value=True)
    
    st.markdown("---")
    if st.session_state.history:
        st.subheader("🕒 Recent Scans")
        hist_df = pd.DataFrame(st.session_state.history)
        st.dataframe(
            hist_df[["ticker", "score"]].tail(5).iloc[::-1], 
            hide_index=True,
            column_config={"score": st.column_config.ProgressColumn("Sentiment", min_value=-1, max_value=1, format="%.2f")}
        )
        if st.button("Clear History"):
            st.session_state.history = []
            st.rerun()

    st.markdown("---")
    st.markdown("*Powered by Gemini*")

st.markdown("<h1 style='text-align: center;'>Market<span style='color:#38bdf8'>Pulse</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; margin-bottom: 40px;'>Real-time AI Market Sentiment Analysis</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    search_col_a, search_col_b = st.columns([3, 1])
    with search_col_a:
        ticker = st.text_input("Asset Ticker", placeholder="e.g. AAPL, BTC", label_visibility="collapsed")
    with search_col_b:
        analyze_btn = st.button("Analyze 🚀")

if analyze_btn and ticker:
    with st.status(f"🤖 Analyzing {ticker.upper()}...", expanded=True) as status:
        try:
            st.write("📡 Connecting to Market Data Stream...")
            
            # MOCK MODE
            if MOCK_MODE:
                import time
                time.sleep(1.0) 
                score = round(random.uniform(-0.8, 0.9), 2)
                articles = random.randint(5, 50)
                sentiment = "Positive" if score > 0.3 else "Negative" if score < -0.3 else "Neutral"
                news_headlines = [
                    f"Market rally continues as {ticker.upper()} beats expectations.",
                    f"Analysts update price target for {ticker.upper()}.",
                    f"Regulatory concerns loom over {ticker.upper()} sector."
                ]
            
            # REAL MODE
            else:
                response = requests.get(BACKEND_URL, params={"ticker": ticker}, timeout=10)
                response.raise_for_status()
                data = response.json().get(ticker, {})
                
                # Robust extraction with defaults
                sentiment = data.get("sentiment", "Unknown")
                score = float(data.get("score", 0.0))
                articles = data.get("articles_analyzed", 0)
                news_headlines = data.get("headlines", ["No news found."])

            st.write("🧠 Gemini AI processing semantics...")
            status.update(label="Analysis Complete!", state="complete", expanded=False)
            
            # Save to history
            st.session_state.history.append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "ticker": ticker.upper(),
                "score": score
            })

            st.divider()
            
            # Metrics
            m1, m2, m3 = st.columns(3)
            with m1: render_metric_card("Confidence", score)
            with m2: render_metric_card("Sentiment", sentiment.capitalize())
            with m3: render_metric_card("Articles", articles)

            st.write("") 

            # Charts
            c1, c2 = st.columns([1, 1])

            # Gauge Chart
            with c1:
                st.markdown("### 🧭 Sentiment Gauge")
                gauge_fig = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=score,
                    delta={'reference': 0},
                    gauge={
                        'axis': {'range': [-1, 1], 'tickcolor': "white"},
                        'bar': {'color': "rgba(0,0,0,0)"},
                        'bgcolor': "rgba(0,0,0,0)",
                        'borderwidth': 2,
                        'bordercolor': "#333",
                        'steps': [
                            {'range': [-1, -0.3], 'color': 'rgba(239, 68, 68, 0.3)'},
                            {'range': [-0.3, 0.3], 'color': 'rgba(234, 179, 8, 0.3)'},
                            {'range': [0.3, 1], 'color': 'rgba(34, 197, 94, 0.3)'}
                        ],
                        'threshold': {'line': {'color': "white", 'width': 4}, 'thickness': 0.75, 'value': score}
                    }
                ))
                gauge_fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"}, height=300, margin=dict(l=20, r=20, t=20, b=20))
                st.plotly_chart(gauge_fig, use_container_width=True)

            # Trend Chart
            with c2:
                st.markdown("### 📈 Sentiment Trend")
                if len(st.session_state.history) > 0:
                    hist_df = pd.DataFrame(st.session_state.history)
                    line_fig = go.Figure()
                    
                    line_fig.add_trace(go.Scatter(
                        x=hist_df["time"], # UPDATED: Uses Time on X-Axis
                        y=hist_df["score"],
                        mode='lines+markers',
                        line=dict(color='#38bdf8', width=3),
                        marker=dict(size=8, color='#22c55e'),
                        fill='tozeroy',
                        fillcolor='rgba(56, 189, 248, 0.1)'
                    ))
                    
                    line_fig.update_layout(
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        font={'color': "#cbd5e1"},
                        height=300,
                        margin=dict(l=0, r=0, t=20, b=0),
                        xaxis=dict(showgrid=False, title="Time"),
                        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', range=[-1.1, 1.1])
                    )
                    st.plotly_chart(line_fig, use_container_width=True)

            # News Feed
            st.markdown("### 📰 Key Insights")
            for headline in news_headlines:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.02); border-left: 3px solid {get_color(score)}; padding: 10px 15px; border-radius: 0 8px 8px 0; margin-bottom: 10px;">
                    {headline}
                </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Analysis Failed: {str(e)}")
            if not MOCK_MODE:
                st.info("Ensure your Backend API is running on Port 8000.")

st.markdown("""<div class="footer">Built for TechSprint 2025</div>""", unsafe_allow_html=True)
