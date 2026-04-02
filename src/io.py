import pandas as pd

REQUIRED_COLS = {"date", "ticker", "text"}

def load_headlines_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Check if csv has the minimum required columns
    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    # Normalize date
    df["date"] = pd.to_datetime(df["date"]).dt.date

    # Normalize ticker
    df["ticker"] = df["ticker"].astype(str).str.upper().str.strip()

    # Make sure text is string
    df["text"] = df["text"].astype(str)

    return df