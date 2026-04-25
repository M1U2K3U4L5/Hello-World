from fastapi import APIRouter, Query

from app.schemas import StockDetail
from app.services.market_data import calculate_indicators, search_stocks

router = APIRouter(prefix="/stocks", tags=["stocks"])


@router.get("/search")
def stock_search(q: str = Query(..., min_length=1)):
    return {"results": search_stocks(q)}


@router.get("/{symbol}", response_model=StockDetail)
def stock_detail(symbol: str) -> StockDetail:
    current, indicators, zones = calculate_indicators(symbol.upper())
    return StockDetail(
        symbol=symbol.upper(),
        company_name=symbol.upper(),
        current_price=current,
        indicators=indicators,
        zones=zones,
    )
