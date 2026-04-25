from pydantic import BaseModel
from typing import List


class StockSummary(BaseModel):
    symbol: str
    name: str
    price: float
    change_pct: float


class MarketOverview(BaseModel):
    trending: List[StockSummary]
    gainers: List[StockSummary]
    losers: List[StockSummary]
    market_sentiment: str


class IndicatorSet(BaseModel):
    sma20: float
    sma50: float
    rsi: float
    macd: float
    signal: float


class TradeZones(BaseModel):
    buy_zone: str
    sell_zone: str
    stop_loss: str


class StockDetail(BaseModel):
    symbol: str
    company_name: str
    current_price: float
    indicators: IndicatorSet
    zones: TradeZones


class NewsArticle(BaseModel):
    title: str
    source: str
    url: str
    sentiment: str


class PortfolioRequest(BaseModel):
    capital: float
    risk_profile: str = "moderate"


class AllocationItem(BaseModel):
    bucket: str
    percentage: float
    amount: float


class PortfolioRecommendation(BaseModel):
    capital: float
    risk_profile: str
    recommendations: List[AllocationItem]


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    disclaimer: str
