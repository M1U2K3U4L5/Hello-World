from fastapi import APIRouter

from app.schemas import PortfolioRecommendation, PortfolioRequest
from app.services.portfolio import recommend_allocation

router = APIRouter(prefix="/portfolio", tags=["portfolio"])


@router.post("/recommend", response_model=PortfolioRecommendation)
def recommend(payload: PortfolioRequest):
    return recommend_allocation(payload.capital, payload.risk_profile)
