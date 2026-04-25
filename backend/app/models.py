from sqlalchemy import Column, DateTime, Float, Integer, String, Text, func

from app.database import Base


class NewsItem(Base):
    __tablename__ = "news_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    source = Column(String(100), nullable=False)
    url = Column(Text, nullable=False)
    sentiment = Column(String(20), nullable=False, default="neutral")
    published_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class PortfolioSnapshot(Base):
    __tablename__ = "portfolio_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    capital = Column(Float, nullable=False)
    risk_profile = Column(String(20), nullable=False, default="moderate")
    allocation_json = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
