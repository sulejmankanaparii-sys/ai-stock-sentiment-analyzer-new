import pandas as pd
import os
import argparse

from src.io import load_headlines_csv
from src.sentiment import get_vader, score_text
from src.scoring import label_from_compound, daily_sentiment
from src.report import build_daily_report
from src.plot import plot_sentiment_trend
from src.api_client import fetch_company_news


def parse_arg():
    parser = argparse.ArgumentParser(description="AI Stock Sentiment Analyzer")

    parser.add_argument("--input", default="data/raw/sample_headline.csv", help="Path to input CSV")
    parser.add_argument("--ticker", default="AAPL", help="Ticker Symbol (e.g. AAPL, TSLA)")
    parser.add_argument("--plot", action="store_true", help="Generate sentiment trend chart")

    parser.add_argument("--use-api", action="store_true", help="Use Finnhub API instead of CSV input")
    parser.add_argument("--from-date", default="2026-03-01", help="Start date for API news in YYYY-MM-DD format")
    parser.add_argument("--to-date", default="2026-03-10", help="End date for API news in YYYY-MM-DD format")

    return parser.parse_args()


def load_input_data(args) -> pd.DataFrame:
    if args.use_api:
        print(f"Using Finnhub API: {args.ticker}...")
        df = fetch_company_news(
            symbol=args.ticker,
            from_date=args.from_date,
            to_date=args.to_date
        )
    else:
        print(f"Using CSV input: {args.input}")
        df = load_headlines_csv(args.input)

    return df


def main():
    args = parse_arg()

    # 1) Load input
    df = load_input_data(args)
    if df.empty:
        print("No data found for selected input.")
        return

    # 2) Score headlines with VADER
    sia = get_vader()
    scores = df["text"].apply(lambda t: score_text(t, sia))
    scores_df = pd.json_normalize(scores)
    df_scored = pd.concat([df, scores_df], axis=1)

    # 3) Add label per headline
    df_scored["sentiment"] = df_scored["compound"].apply(label_from_compound)

    # 4) Aggregate daily per ticker
    df_daily = daily_sentiment(df_scored)

    # 5) Build final report with signal
    df_report = build_daily_report(df_daily)

    # 6) Save outputs
    os.makedirs("data/processed", exist_ok=True)
    df_report.to_csv(
        "data/processed/daily_sentiment.csv",
        index=False
    )

    # 7) Save text report
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/report.txt", "w", encoding="utf-8") as f:
        f.write("AI Stock Sentiment Analyzer Report\n")
        f.write("---------------------------------\n\n")
        f.write(df_report.to_string())
        f.write("\n")

    # 8) Print final report
    print("\nFINAL REPORT (Daily Score + Signal)")
    print(df_report)

    # 9) Optional chart
    if args.plot:
        ticker = args.ticker.upper().strip()
        plot_path = f"outputs/{ticker}_sentiment.png"
        plot_sentiment_trend(df_report, ticker=ticker, outpath=plot_path)
        print(f"\nSaved plot: {plot_path}")


if __name__ == "__main__":
    main()
