import pandas as pd


def label_from_compound(compound: float) -> str:

    if compound >= 0.05:
        return "positive"

    if compound <= -0.05:
        return "negative"

    return "neutral"

def daily_sentiment(df: pd.DataFrame) -> pd.DataFrame:

    result = (
        df.groupby(["date", "ticker"])
        .agg(
            daily_sentiment_score=("compound", "mean"),
            news_count=("compound", "count")
        )
        .reset_index()
    )
    return  result

def signal_from_score(score: float, bullish: float = 0.10, bearish: float = -0.10) -> str:

    if score >= bullish:
        return "bullish"

    if score <= bearish:
        return "bearish"

    return "neutral"
