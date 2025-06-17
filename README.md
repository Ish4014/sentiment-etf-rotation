# 📊 Sentiment-Driven ETF Portfolio Rotation Strategy

A sentiment-driven portfolio management system that uses FinBERT to analyze financial news, generate ETF signals, rotate holdings weekly, and compare performance against SPY. Built with Python, Streamlit, and financial APIs.


##  Overview

This project integrates NLP, finance, and portfolio analytics to simulate a real-world investment strategy:

- 🧠 Uses FinBERT for sentiment analysis on ETF-related news
- 📈 Rotates into top bullish sector ETFs weekly
- 📊 Backtests against SPY and calculates Sharpe, returns, volatility
- 🧪 Visualizes performance via an interactive Streamlit dashboard


## 🛠Tools & Libraries

- `Python`, `Pandas`, `NumPy`, `Matplotlib`
- `FinBERT`, `transformers`, `yfinance`
- `Streamlit` (for app deployment)
- `Finnhub API` (for financial news)

  
---

##  Sample Outputs

| Metric             | Strategy   | SPY        |
|--------------------|------------|------------|
| Annual Return      | ✅ XX.XX%  | YY.YY%     |
| Volatility         | ✅ XX.XX%  | YY.YY%     |
| Sharpe Ratio       | ✅ X.XX     | Y.YY       |



##  How to Run

1. Clone the repository:

git clone https://github.com/Ish4014/sentiment-etf-rotation.git
cd sentiment-etf-rotation

2: Install dependencies:
pip install -r requirements.txt

3. Launch Streamlit app:
   cd App
streamlit run streamlit_app.py

🛡 Disclaimer
This is an academic project. No financial advice is given.


Contact
Ishwar Nimse
LinkedIn: www.linkedin.com/in/ishwar-nimse
GitHub: https://github.com/Ish4014






