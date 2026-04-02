import pandas as pd
import os

from src.io import load_headlines_csv
from src.sentiment import get_vader, score_text
from src.scoring import label_from_compound, daily_sentiment
from src.report import build_daily_report
from src.plot import plot_sentiment_trend
from src.api_client import fetch_company_news
from datetime import datetime, timedelta


def run_pipeline(ticker, source, start_date=None, end_date=None):
    # 1) Load data

    if source == "api":

        if not start_date or not end_date:
            end = datetime.today()
            start = end - timedelta(days=7)

            start_date = start.strftime("%Y-%m-%d")
            end_date = end.strftime("%Y-%m-%d")

        df = fetch_company_news(
            symbol=ticker,
            from_date=start_date,
            to_date=end_date
        )
        print("TICKER:", ticker)
        print("DATES:", start_date, end_date)
        print("ROWS:", len(df))
        print(df.head())
    else:
        df = load_headlines_csv("data/raw/sample_headline.csv")  # adjust if needed

    if df.empty:
        return {
            "ticker": ticker,
            "signal": "No Data",
            "articles": 0,
            "sentiment_score": 0,
            "chart_path": None
        }

    # 2) VADER
    sia = get_vader()
    scores = df["text"].apply(lambda t: score_text(t, sia))
    scores_df = pd.json_normalize(scores)
    df_scored = pd.concat([df, scores_df], axis=1)

    # 3) Label
    df_scored["sentiment"] = df_scored["compound"].apply(label_from_compound)

    # 4) Daily aggregation
    df_daily = daily_sentiment(df_scored)

    # 5) Final report
    df_report = build_daily_report(df_daily)

    print("REPORT COLUMNS:", df_report.columns)

    print(df_report.tail())

    # 6) Extract latest signal

    sentiment_score = df_report["daily_sentiment_score"].mean()

    signal = df_report.iloc[-1]["signal"]

    articles = df_report["news_count"].sum()

    # 7) Chart
    chart_path = None
    try:
        os.makedirs("webapp/static/charts", exist_ok=True)
        filename = f"{ticker}_sentiment.png"
        full_path = f"webapp/static/charts/{filename}"

        plot_sentiment_trend(df_report, ticker=ticker, outpath=full_path)

        chart_path = f"/static/charts/{filename}"
    except:
        pass

    return {
        "ticker": ticker,
        "signal": signal,
        "articles": int(articles),
        "sentiment_score": round(float(sentiment_score), 3),
        "chart_path": chart_path
    }
