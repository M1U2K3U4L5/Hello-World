import TradingViewWidget from "../../../components/TradingViewWidget";

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

async function getStock(symbol: string) {
  const res = await fetch(`${API_BASE}/stocks/${symbol}`, { cache: "no-store" });
  return res.json();
}

export default async function StockDetailPage({ params }: { params: { symbol: string } }) {
  const stock = await getStock(params.symbol);

  return (
    <>
      <section className="card" style={{ marginBottom: "1rem" }}>
        <h1 style={{ marginTop: 0 }}>{stock.symbol} Details</h1>
        <div>Current Price: <strong>₹{stock.current_price}</strong></div>
      </section>

      <TradingViewWidget symbol={stock.symbol} />

      <h2 className="section-title">Technical Indicators</h2>
      <div className="grid">
        <div className="card"><strong>SMA20</strong><div>₹{stock.indicators.sma20}</div></div>
        <div className="card"><strong>SMA50</strong><div>₹{stock.indicators.sma50}</div></div>
        <div className="card"><strong>RSI</strong><div>{stock.indicators.rsi}</div></div>
        <div className="card"><strong>MACD</strong><div>{stock.indicators.macd}</div></div>
      </div>

      <h2 className="section-title">Trade Zones</h2>
      <div className="grid">
        <div className="card"><strong>Buy Zone</strong><div>{stock.zones.buy_zone}</div></div>
        <div className="card"><strong>Sell Zone</strong><div>{stock.zones.sell_zone}</div></div>
        <div className="card"><strong>Stop Loss</strong><div>{stock.zones.stop_loss}</div></div>
      </div>
    </>
  );
}
