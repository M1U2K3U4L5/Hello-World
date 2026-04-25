from fastapi import APIRouter

from app.schemas import MarketOverview
from app.services.market_data import NSE_UNIVERSE, fetch_quotes
from app.services.sentiment import aggregate_market_sentiment

router = APIRouter(prefix="/market", tags=["market"])


@router.get("/overview", response_model=MarketOverview)
def get_market_overview() -> MarketOverview:
    symbols = list(NSE_UNIVERSE.keys())[:8]
    quotes = fetch_quotes(symbols)

    ranked = sorted(quotes, key=lambda x: x.change_pct, reverse=True)
    gainers = ranked[:5]
    losers = sorted(quotes, key=lambda x: x.change_pct)[:5]
    trending = sorted(quotes, key=lambda x: abs(x.change_pct), reverse=True)[:5]

    sentiment = aggregate_market_sentiment(
        [
            "positive" if q.change_pct > 0.7 else "negative" if q.change_pct < -0.7 else "neutral"
            for q in quotes
        ]
    )

    return MarketOverview(
        trending=trending,
        gainers=gainers,
        losers=losers,
        market_sentiment=sentiment,
    )
