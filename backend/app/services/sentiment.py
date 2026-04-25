from typing import Iterable


POSITIVE_WORDS = {"rally", "growth", "beat", "upgrade", "surge", "profit", "buy"}
NEGATIVE_WORDS = {"fall", "downgrade", "loss", "weak", "sell", "drop", "risk"}


def classify_sentiment(text: str) -> str:
    lower = text.lower()
    pos = sum(word in lower for word in POSITIVE_WORDS)
    neg = sum(word in lower for word in NEGATIVE_WORDS)
    if pos > neg:
        return "positive"
    if neg > pos:
        return "negative"
    return "neutral"


def aggregate_market_sentiment(labels: Iterable[str]) -> str:
    labels = list(labels)
    score = labels.count("positive") - labels.count("negative")
    if score >= 2:
        return "Bullish"
    if score <= -2:
        return "Bearish"
    return "Neutral"
