from app.services.market_data import calculate_indicators


def answer_investment_question(question: str) -> str:
    text = question.strip().upper()
    symbol = "ICICIBANK"
    for candidate in ["ICICIBANK", "RELIANCE", "TCS", "INFY", "SBIN", "HDFCBANK"]:
        if candidate in text.replace(" ", ""):
            symbol = candidate
            break

    current, indicators, zones = calculate_indicators(symbol)

    signal = "HOLD"
    rationale = []

    if current > indicators.sma20 > indicators.sma50:
        rationale.append("price is above SMA20 and SMA50")
        signal = "BUY ON DIPS"
    if indicators.rsi > 70:
        rationale.append("RSI indicates overbought conditions")
        signal = "WAIT"
    elif indicators.rsi < 35:
        rationale.append("RSI indicates potential oversold rebound")
        signal = "ACCUMULATE CAREFULLY"

    if indicators.macd < indicators.signal:
        rationale.append("MACD is below signal line (weak momentum)")
    else:
        rationale.append("MACD is above signal line (positive momentum)")

    return (
        f"For {symbol}, current price is ₹{current}. Model signal: {signal}. "
        f"Key reasons: {', '.join(rationale)}. "
        f"Buy zone: {zones.buy_zone}, Sell zone: {zones.sell_zone}, Stop loss: {zones.stop_loss}."
    )
