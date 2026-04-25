from app.schemas import AllocationItem, PortfolioRecommendation


RISK_MODELS = {
    "conservative": [
        ("Large-cap equities", 40),
        ("Debt / Liquid funds", 40),
        ("Gold ETF", 10),
        ("Cash reserve", 10),
    ],
    "moderate": [
        ("Large-cap equities", 45),
        ("Mid-cap equities", 20),
        ("Debt / Liquid funds", 20),
        ("Gold ETF", 10),
        ("Cash reserve", 5),
    ],
    "aggressive": [
        ("Large-cap equities", 35),
        ("Mid-cap equities", 30),
        ("Small-cap / thematic", 20),
        ("Debt / Liquid funds", 10),
        ("Cash reserve", 5),
    ],
}


def recommend_allocation(capital: float, risk_profile: str) -> PortfolioRecommendation:
    profile = risk_profile.lower().strip()
    model = RISK_MODELS.get(profile, RISK_MODELS["moderate"])

    allocation = [
        AllocationItem(bucket=bucket, percentage=pct, amount=round((pct / 100) * capital, 2))
        for bucket, pct in model
    ]
    return PortfolioRecommendation(capital=capital, risk_profile=profile, recommendations=allocation)
