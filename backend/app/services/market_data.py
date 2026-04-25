from __future__ import annotations

from dataclasses import dataclass
from typing import List

import numpy as np
import pandas as pd
import yfinance as yf

from app.schemas import IndicatorSet, StockSummary, TradeZones

NSE_UNIVERSE = {
    "RELIANCE": "Reliance Industries",
    "TCS": "Tata Consultancy Services",
    "INFY": "Infosys",
    "HDFCBANK": "HDFC Bank",
    "ICICIBANK": "ICICI Bank",
    "SBIN": "State Bank of India",
    "LT": "Larsen & Toubro",
    "ITC": "ITC",
    "BHARTIARTL": "Bharti Airtel",
    "KOTAKBANK": "Kotak Mahindra Bank",
}


@dataclass
class Quote:
    symbol: str
    name: str
    price: float
    change_pct: float


def _ticker(symbol: str) -> str:
    return f"{symbol}.NS"


def _safe_float(value: float | int | np.number | None) -> float:
    return float(value) if value is not None and not pd.isna(value) else 0.0


def fetch_quotes(symbols: List[str]) -> List[StockSummary]:
    results: List[StockSummary] = []
    for symbol in symbols:
        try:
            df = yf.download(_ticker(symbol), period="5d", interval="1d", progress=False, auto_adjust=True)
            if df.empty:
                continue
            close = df["Close"].dropna()
            if len(close) < 2:
                continue
            price = _safe_float(close.iloc[-1])
            prev = _safe_float(close.iloc[-2])
            change_pct = ((price - prev) / prev) * 100 if prev else 0.0
            results.append(
                StockSummary(
                    symbol=symbol,
                    name=NSE_UNIVERSE.get(symbol, symbol),
                    price=round(price, 2),
                    change_pct=round(change_pct, 2),
                )
            )
        except Exception:
            continue

    if results:
        return results

    # offline fallback
    return [
        StockSummary(symbol="RELIANCE", name="Reliance Industries", price=2964.10, change_pct=1.42),
        StockSummary(symbol="ICICIBANK", name="ICICI Bank", price=1221.20, change_pct=0.89),
        StockSummary(symbol="INFY", name="Infosys", price=1610.50, change_pct=-0.31),
        StockSummary(symbol="TCS", name="TCS", price=3955.00, change_pct=1.21),
        StockSummary(symbol="SBIN", name="State Bank of India", price=819.30, change_pct=-1.10),
    ]


def search_stocks(query: str) -> List[dict]:
    q = query.upper().strip()
    return [
        {"symbol": symbol, "name": name}
        for symbol, name in NSE_UNIVERSE.items()
        if q in symbol or q in name.upper()
    ][:10]


def _ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False).mean()


def calculate_indicators(symbol: str) -> tuple[float, IndicatorSet, TradeZones]:
    df = yf.download(_ticker(symbol), period="6mo", interval="1d", progress=False, auto_adjust=True)
    if df.empty:
        # fallback values
        return (
            1221.2,
            IndicatorSet(sma20=1208.1, sma50=1170.4, rsi=58.4, macd=9.6, signal=7.9),
            TradeZones(buy_zone="₹1180 - ₹1210", sell_zone="₹1270 - ₹1310", stop_loss="₹1145"),
        )

    close = df["Close"].dropna()
    current = float(close.iloc[-1])
    sma20 = float(close.rolling(20).mean().iloc[-1])
    sma50 = float(close.rolling(50).mean().iloc[-1])

    delta = close.diff()
    gains = delta.clip(lower=0)
    losses = -delta.clip(upper=0)
    avg_gain = gains.rolling(14).mean()
    avg_loss = losses.rolling(14).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    rsi = float((100 - (100 / (1 + rs))).fillna(50).iloc[-1])

    ema12 = _ema(close, 12)
    ema26 = _ema(close, 26)
    macd_line = ema12 - ema26
    signal_line = _ema(macd_line, 9)

    buy_low = min(sma20, current) * 0.98
    buy_high = min(sma20, current) * 1.01
    sell_low = max(current, sma20) * 1.03
    sell_high = max(current, sma20) * 1.07
    stop_loss = min(sma50, current) * 0.96

    return (
        round(current, 2),
        IndicatorSet(
            sma20=round(sma20, 2),
            sma50=round(sma50, 2),
            rsi=round(rsi, 2),
            macd=round(float(macd_line.iloc[-1]), 2),
            signal=round(float(signal_line.iloc[-1]), 2),
        ),
        TradeZones(
            buy_zone=f"₹{buy_low:.2f} - ₹{buy_high:.2f}",
            sell_zone=f"₹{sell_low:.2f} - ₹{sell_high:.2f}",
            stop_loss=f"₹{stop_loss:.2f}",
        ),
    )
