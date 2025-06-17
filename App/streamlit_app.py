import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Sentiment-Driven Portfolio", layout="wide")
st.title("Sentiment-Driven Portfolio Rotation Strategy")

st.markdown("""
Upload your sentiment-based ETF signals to generate a portfolio, evaluate its performance, and visualize key metrics.
""")

uploaded_file = st.file_uploader("Upload `weekly_signals.csv`", type="csv")

if uploaded_file:
    signals_df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Sentiment Signals")
    st.dataframe(signals_df)

    top_n = st.slider("Select number of top sectors to include", min_value=1, max_value=len(signals_df), value=3)
    top_etfs = signals_df.sort_values("finbert_score", ascending=False).head(top_n)
    etf_list = top_etfs["etf_ticker"].tolist()

    st.write("Selected ETFs:", etf_list)

    price_data = yf.download(etf_list, period="6mo", interval="1wk", auto_adjust=True)["Close"].dropna()
    returns = price_data.pct_change().dropna()
    weights = {etf: 1 / len(etf_list) for etf in etf_list}
    portfolio_returns = returns[etf_list].dot(pd.Series(weights))
    portfolio_returns.name = "Strategy"

    spy = yf.download("SPY", period="6mo", interval="1wk", auto_adjust=True)["Close"]
    spy_returns = spy.pct_change().dropna()
    spy_returns.name = "SPY"

    combined_returns = pd.concat([portfolio_returns, spy_returns], axis=1).dropna()
    cumulative_returns = (1 + combined_returns).cumprod()

    st.subheader("Portfolio vs SPY")
    st.line_chart(cumulative_returns)

    def compute_metrics(r):
        r = r.dropna()
        cumulative = (1 + r).prod()
        ann_return = float(cumulative**(52 / len(r)) - 1)
        ann_vol = float(r.std() * np.sqrt(52))
        sharpe = ann_return / ann_vol if ann_vol != 0 else np.nan
        return ann_return, ann_vol, sharpe

    strategy_metrics = compute_metrics(portfolio_returns)
    spy_metrics = compute_metrics(spy_returns)

    st.subheader("Performance Metrics")

    st.write("**Strategy**")
    st.metric("Annual Return", f"{strategy_metrics[0]:.2%}")
    st.metric("Annual Volatility", f"{strategy_metrics[1]:.2%}")
    st.metric("Sharpe Ratio", f"{strategy_metrics[2]:.2f}")

    st.write("**SPY**")
    st.metric("Annual Return", f"{spy_metrics[0]:.2%}")
    st.metric("Annual Volatility", f"{spy_metrics[1]:.2%}")
    st.metric("Sharpe Ratio", f"{spy_metrics[2]:.2f}")
