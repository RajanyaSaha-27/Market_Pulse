<h1 align="center">📊 Market_Pulse</h1>
<h3 align="center">AI-Powered Market Sentiment Analysis using Google Gemini</h3>

<p align="center">
  <b>TechSprint Hackathon Project</b><br/>
  Real-time sentiment analysis for market-related news (stocks, crypto, indices)
</p>

<hr/>

<h2>🚀 Problem Statement</h2>
<p>
Financial markets are heavily influenced by news such as earnings reports,
regulatory updates, and macroeconomic events. Investors and analysts often
struggle to process large volumes of market news in real time.
</p>

<p>
<b>MarketPulse</b> solves this problem by using an AI agent powered by
<b>Google Gemini</b> to analyze market-related news and generate an
aggregated sentiment score instantly.
</p>

<hr/>

<h2>💡 Solution Overview</h2>
<ul>
  <li>User enters a market ticker or keyword (e.g., AAPL, TSLA, BTC)</li>
  <li>System collects multiple related market news headlines</li>
  <li>Each headline is analyzed by <b>Google Gemini</b></li>
  <li>Sentiment scores are aggregated into a final market sentiment</li>
  <li>Results are displayed on an interactive dashboard</li>
</ul>

<hr/>

<h2>🧠 Google Technology Used</h2>
<p>
<b>Google Gemini API</b> is used as the core AI engine for:
</p>
<ul>
  <li>Understanding financial context in news headlines</li>
  <li>Classifying sentiment as Positive, Negative, or Neutral</li>
  <li>Generating sentiment scores and summaries</li>
</ul>

<p>
Gemini enables accurate sentiment analysis without training custom ML models,
making the system scalable and domain-aware.
</p>

<hr/>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li><b>AI:</b> Google Gemini API</li>
  <li><b>Backend:</b> FastAPI (Python)</li>
  <li><b>Frontend:</b> Streamlit</li>
  <li><b>Data Processing:</b> Prompt-based NLP</li>
  <li><b>Deployment:</b> Streamlit Cloud</li>
</ul>

<hr/>

<h2>🏗️ Project Architecture</h2>
<pre>
User Interface (Streamlit)
        ↓
FastAPI Backend
        ↓
Market News Collector
        ↓
Google Gemini Sentiment Agent
        ↓
Sentiment Aggregator
        ↓
Final Market Sentiment Output
</pre>

<hr/>

<h2>📁 Project Structure</h2>
<pre>
MarketPulse/
│
├── backend/
│   ├── main.py
│   ├── sentiment_agent.py
│   ├── news_fetcher.py
│   ├── utils.py
│   └── config.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
└── README.md
</pre>

<hr/>

<h2>⚙️ How to Run Locally</h2>

<h3>1️⃣ Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>2️⃣ Start Backend Server</h3>
<pre>
uvicorn backend.main:app --reload
</pre>

<h3>3️⃣ Run Frontend</h3>
<pre>
streamlit run frontend/app.py
</pre>

<hr/>

<h2>🌐 MVP Demo Link</h2>
<p>
<b>Live Demo:</b><br/>
<a href="[#](https://marketpulse-by-codecrafters.streamlit.app/)" target="_blank">[https://marketpulse-techsprint.streamlit.app](https://marketpulse-by-codecrafters.streamlit.app/)</a>
</p>

<p><i>(Replace with your actual deployed Streamlit link)</i></p>

<hr/>

<h2>👥 Team Information</h2>
<ul>
  <li>Team Size: 4 Members</li>
  <li>Hackathon: TechSprint</li>
  <li>Domain: FinTech / AI</li>
</ul>

<hr/>

<h2>🔮 Future Enhancements</h2>
<ul>
  <li>Multi-agent system (Risk Analysis + Sentiment Agent)</li>
  <li>Sentiment trend visualization over time</li>
  <li>Live news API integration</li>
  <li>Portfolio-level market insights</li>
</ul>

<hr/>

<h2>🏆 Conclusion</h2>
<p>
MarketPulse demonstrates how <b>Google Gemini</b> can be effectively used
to understand complex financial language and deliver actionable insights
from market news. The project is scalable, domain-independent, and
well-suited for real-world financial applications.
</p>

<p align="center">
  <b>Built with ❤️ by CodeCrafters</b>
</p>
