import matplotlib.pyplot as plt
import pandas as pd


def plot_sentiment_trend(df_report: pd.DataFrame, ticker: str, outpath):

    df = df_report[df_report['ticker'] == ticker].copy()

    if df.empty:
        raise ValueError(f"No data found for ticker {ticker}")

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    plt.figure()
    plt.plot(df["date"], df["daily_sentiment_score"])
    plt.title(f"Daily Sentiment Trend - {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Sentiment Score")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(outpath)
    plt.close()
