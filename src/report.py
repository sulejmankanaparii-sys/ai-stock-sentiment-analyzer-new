import pandas as pd
from src.scoring import signal_from_score

def build_daily_report(df_daily: pd.DataFrame) -> pd.DataFrame:

    df = df_daily.copy()
    df['signal'] = df['daily_sentiment_score'].apply(signal_from_score)
    return df.sort_values(['date', 'ticker'])
