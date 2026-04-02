import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def get_vader() -> SentimentIntensityAnalyzer:
    try:
        nltk.data.find('sentiment/vader_lexicon')
    except LookupError:
        nltk.download('vader_lexicon', quiet=True)

    return SentimentIntensityAnalyzer()


def score_text(text: str, sia: SentimentIntensityAnalyzer) -> dict:
    text = (text or "").strip()
    return sia.polarity_scores(text)

