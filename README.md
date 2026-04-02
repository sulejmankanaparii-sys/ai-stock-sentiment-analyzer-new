# 📊 AI Stock Sentiment Analyzer (Web App)

A full-stack web application that analyzes financial news sentiment for stocks and generates trading signals using NLP techniques.

This project combines Natural Language Processing (VADER), data aggregation, and a Flask-based web interface to provide real-time sentiment insights for stock tickers.

---

## 🚀 Features

- 🔎 Fetch stock news via API (Finnhub) or CSV
- 🧠 Perform sentiment analysis using VADER (NLP)
- 📈 Aggregate daily sentiment scores
- 📊 Generate trading signals (Bullish / Bearish / Neutral)
- 📉 Visualize sentiment trends with charts
- 🌐 Interactive web interface (Flask + JavaScript)

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **NLP:** VADER Sentiment Analysis
- **Data Processing:** Pandas
- **Visualization:** Matplotlib
- **API:** Finnhub

---

## 📁 Project Structure
```commandline
ai-stock-sentiment-analyzer/
│
├── data/ # Raw and processed data
├── outputs/ # Reports and generated charts
├── src/ # Core NLP and processing logic
│ ├── api_client.py
│ ├── sentiment.py
│ ├── scoring.py
│ ├── report.py
│ └── plot.py
│
├── webapp/ # Web application layer
│ ├── app.py
│ ├── routes/
│ ├── services/
│ ├── templates/
│ └── static/
│
├── main.py # CLI pipeline entry point
├── .env
└── requirements.txt
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/ai-stock-sentiment-analyzer.git
cd ai-stock-sentiment-analyzer
```
2. Create virtual environment:
```
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

3. Install dependencies:
```
pip install -r requirements.txt
```

---

# 🧩 Environment Variables

```md
## 🔑 Environment Variables

Create a `.env` file in the root directory and add your Finnhub API key:

FINNHUB_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

Start the Flask web app:

```bash
python -m webapp.app
```

Open in browser: http://127.0.0.1:5000


---

# 🧩 — How It Works

```md
1. Fetch stock-related news (API or CSV)
2. Apply VADER sentiment analysis to each headline
3. Compute sentiment scores (compound)
4. Aggregate sentiment daily
5. Generate trading signal
6. Display results and chart in web UI
```

---

## 📊 Example Output

- **Signal:** Bullish / Bearish / Neutral  
- **Sentiment Score:** Numerical value (-1 to 1)  
- **Articles:** Number of news analyzed  
- **Chart:** Daily sentiment trend visualization  

---

## 🚧 Future Improvements

- Add real-time streaming data
- Improve UI/UX with modern frameworks (React)
- Deploy to cloud (Render / AWS)
- Add user authentication and saved analyses

---

## 👤 Author

Developed by Eris Kanapari

Aspiring AI/ML Engineer with focus on real-world applications of NLP and data-driven decision systems.
