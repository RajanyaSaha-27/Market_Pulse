<div align="center">

# 📈 Market Pulse

### *AI-Powered Multi-Agent Financial Sentiment Analysis Platform*

**Analyze. Interpret. Predict. — Before the market reacts.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

<br/>

> *"Markets move on sentiment before they move on numbers. Market Pulse captures that sentiment — in real time."*

<br/>

</div>

---

## 🧠 What is Market Pulse?

Market Pulse is a **production-ready AI-powered stock sentiment analysis platform** that analyzes market mood for stocks, indices, and assets like:

```bash
AAPL
TSLA
RELIANCE
NIFTY
BTC
````

The system uses a **3-Agent AI workflow** to fetch financial headlines, extract meaningful keywords, understand sentiment trends, and calculate a normalized market sentiment score ranging from **-1 to +1**.

Think of it as an **AI market analyst that reads financial news before you do.**

| Traditional Research      | With Market Pulse                     |
| ------------------------- | ------------------------------------- |
| Manual news reading       | AI-curated financial headlines        |
| Subjective interpretation | Quantified sentiment score            |
| Time-consuming analysis   | Real-time market mood detection       |
| Scattered information     | Centralized dashboard                 |
| No visualization          | Interactive sentiment charts & gauges |

---

## 🤖 AI Architecture

Market Pulse operates using **3 autonomous AI agents** working sequentially to analyze financial sentiment.

```text
┌──────────────────────────────────────────────────────────────┐
│                    AI AGENT PIPELINE                         │
│                                                              │
│  📥 User Input                                               │
│  (Ticker Symbol: AAPL / NIFTY / RELIANCE etc.)               │
│           │                                                  │
│           ▼                                                  │
│  ┌─────────────────┐                                         │
│  │  Agent 1        │  News Fetching Agent                    │
│  │  📰 Fetch       │  Retrieves top financial headlines     │
│  └────────┬────────┘                                         │
│            ▼                                                 │
│  ┌─────────────────┐                                         │
│  │  Agent 2        │  Keyword & Sentiment Agent              │
│  │  🔍 Analyze     │  Extracts keywords + sentiment context  │
│  └────────┬────────┘                                         │
│            ▼                                                 │
│  ┌─────────────────┐                                         │
│  │  Agent 3        │  Sentiment Scoring Agent                │
│  │  📊 Score       │  Generates normalized score (-1 to +1)  │
│  └────────┬────────┘                                         │
│            ▼                                                 │
│  ┌──────────────────────────────────────────────┐             │
│  │ Visualization Dashboard                      │             │
│  │ 📈 Trend Charts                             │             │
│  │ 🎯 Sentiment Gauge                          │             │
│  │ 📰 News Display                             │             │
│  └──────────────────────────────────────────────┘            │
└──────────────────────────────────────────────────────────────┘
```

---

## 📊 Sentiment Scoring System

The platform generates a sentiment score between:

* **+1 → Strong Positive**
* **0 → Neutral**
* **-1 → Strong Negative**

### Market Mood Categories

| Score Range   | Sentiment   |
| ------------- | ----------- |
| `0.15 → 1.0`   | 🟢 Positive |
| `-0.15 → 0.15`  | ⚪ Neutral   |
| `-1.0 → -0.15` | 🔴 Negative |

---

## ⚡ Features

* 📰 **Real-Time Financial News Fetching**
* 🤖 **Multi-Agent AI Workflow**
* 🔍 **Keyword Extraction from Headlines**
* 📈 **Interactive Trend Visualization**
* 🎯 **Dynamic Sentiment Gauge**
* 📊 **Normalized Sentiment Scoring**
* 🕘 **Search History Tracking**
* 🖨️ **Printable Analysis Reports**
* 🎥 **Built-in Screen Recording Support**
* 🎨 **Theme Switching Support**
* 🛡️ **Demo Mode Fallback if APIs Fail**
* ⚡ **FastAPI Backend + Streamlit Frontend**
* ☁️ **Render Cloud Deployment**

---

## 🧩 How the System Works

```text
User Enters Ticker
        │
        ▼
📥 Input Example:
AAPL / TSLA / NIFTY / RELIANCE
        │
        ▼
📰 Agent 1 → Fetches Top Financial News
        │
        ▼
🔍 Agent 2 → Extracts Keywords + Detects Sentiment
        │
        ▼
📊 Agent 3 → Calculates Sentiment Score
        │
        ▼
📈 Dashboard Displays:
• Top Headlines
• Sentiment Gauge
• Trend Chart
• Market Mood
```

---

## 📷 Dashboard Preview
<img width="1732" height="544" alt="Screenshot 2025-12-27 183722" src="https://github.com/user-attachments/assets/44673872-5155-43d3-a2ba-5f178f706f31" />
--
<img width="1708" height="675" alt="Screenshot 2025-12-27 182745" src="https://github.com/user-attachments/assets/0bdc38be-661a-4efe-b1d7-c685300c90c9" />
--
<img width="297" height="901" alt="Screenshot 2025-12-27 183153" src="https://github.com/user-attachments/assets/f3e643a3-4449-4e85-a33f-09236fdebba9" />




---

## 🧱 Tech Stack

### Frontend

| Technology | Purpose                  |
| ---------- | ------------------------ |
| Streamlit  | Interactive dashboard UI |
| Plotly     | Charts & visualizations  |
| HTML/CSS   | UI styling               |

### Backend

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python 3.10+ | Core runtime                 |
| FastAPI      | High-performance backend API |
| Uvicorn      | ASGI server                  |

### AI / NLP

| Technology           | Purpose                 |
| -------------------- | ----------------------- |
| Transformers         | Sentiment analysis      |
| NLP Pipelines        | Keyword extraction      |
| Custom Scoring Logic | Sentiment normalization |

### Deployment

| Platform | Purpose          |
| -------- | ---------------- |
| Render   | Cloud deployment |

---

## 🌐 Live Link

<p>
<b>Live Demo:</b>
<a href="https://marketpulse-by-codecrafters.streamlit.app/">here</a>
</p>

---

## ⚙️ Run Locally

### Prerequisites

* Python 3.10+
* Internet connection
* API Key (optional for live news)

---

### 1. Clone Repository

```bash
git clone https://github.com/RajanyaSaha-27/Market_Pulse.git
cd Market_Pulse
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create `.env`

```env
API_KEY=your_api_key_here
```

---

### 5. Start Backend

```bash
uvicorn main:app --reload
```

---

### 6. Start Frontend

```bash
streamlit run app.py
```

---

## 💡 Why Market Pulse Stands Out

### 1. Multi-Agent AI Workflow

Instead of using a single sentiment model, Market Pulse separates tasks across autonomous agents for better modularity and explainability.

### 2. Quantified Financial Sentiment

The system converts subjective news sentiment into measurable market intelligence using normalized scoring.

### 3. Interactive Visualization

Rather than static outputs, users get dynamic gauges, trend charts, and visual insights.

### 4. Fallback Demo Mode

Even if APIs fail or rate limits are exceeded, the platform remains fully functional using demo data.

### 5. Designed for Real Traders & Researchers

The architecture can be extended into:

* algorithmic trading
* portfolio monitoring
* AI-driven research tools
* real-time financial dashboards

---

## 🚧 Limitations

* Sentiment is based primarily on headlines
* Financial predictions are not guaranteed
* API rate limits may affect live news fetching

---

## 🚀 Future Scope

| Phase   | Goal                               |
| ------- | ---------------------------------- |
| Phase 1 | Real-time market streaming         |
| Phase 2 | Portfolio-based sentiment tracking |
| Phase 3 | AI-powered stock forecasting       |

### Planned Features

* 📡 Real-time stock data integration
* 🧠 Advanced LLM-based financial summarization
* 📱 Mobile-responsive dashboard
* 🔔 Sentiment-based alerts
* 🌍 Multi-market support
* 📈 AI forecasting models

---

## 📁 Project Structure

```text
Market_Pulse/
├── app.py                 # Streamlit frontend
├── main.py                # FastAPI backend
├── news_fetcher.py        # News collection agent
├── sentiment_agent.py     # Sentiment analysis agent
├── config.py              # Configuration
├── requirements.txt
└── README.md
```

---

## 👤 Author

**Rajanya Saha**<br>
B.Tech CSE (AI & ML)

---

<div align="center">

**If Market Pulse impressed you, consider giving this repository a ⭐**

*"Financial markets speak through sentiment. Market Pulse listens."*

</div>
