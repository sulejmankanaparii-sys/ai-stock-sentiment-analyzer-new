import os
import requests
import pandas as pd
from dotenv import load_dotenv

BASE_URL = "https://finnhub.io/api/v1/company-news"


def fetch_company_news(symbol: str, from_date: str, to_date: str) -> pd.DataFrame:
    load_dotenv()
    api_key = os.getenv("FINNHUB_API_KEY")
    if not api_key:
        raise ValueError("FINNHUB_API_KEY was not found in environment variables.")

    params = {
        "symbol": symbol.upper().strip(),
        "from": from_date,
        "to": to_date,
        "token": api_key
    }

    response = requests.get(BASE_URL, params=params, timeout=20)
    response.raise_for_status()

    data = response.json()

    if not data:
        return pd.DataFrame(colums=["date", "ticker", "source", "text"])

    rows = []

    for item in data:
        rows.append({
            'date': pd.to_datetime(item.get("datetime"), unit="s").date(),
            "ticker": symbol.upper().strip(),
            "source": item.get("source", "Unknown"),
            "text": item.get("headline", "")
        })

    return pd.DataFrame(rows)

