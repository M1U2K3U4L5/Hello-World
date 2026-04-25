from fastapi import APIRouter

from app.schemas import NewsArticle
from app.services.sentiment import classify_sentiment

router = APIRouter(prefix="/news", tags=["news"])


@router.get("/latest", response_model=list[NewsArticle])
def latest_news():
    feed = [
        {
            "title": "Nifty rally continues as banking stocks beat estimates",
            "source": "MarketWire",
            "url": "https://example.com/news1",
        },
        {
            "title": "IT shares fall after cautious global tech outlook",
            "source": "FinDesk",
            "url": "https://example.com/news2",
        },
        {
            "title": "Auto sector sees steady growth in monthly dispatch data",
            "source": "CapitalNow",
            "url": "https://example.com/news3",
        },
    ]

    return [
        NewsArticle(
            title=item["title"],
            source=item["source"],
            url=item["url"],
            sentiment=classify_sentiment(item["title"]),
        )
        for item in feed
    ]
