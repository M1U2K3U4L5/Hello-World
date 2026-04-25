import DashboardCard from "../components/DashboardCard";
import StockSearch from "../components/StockSearch";

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

async function getOverview() {
  const res = await fetch(`${API_BASE}/market/overview`, { cache: "no-store" });
  return res.json();
}

export default async function HomePage() {
  const overview = await getOverview();
  const sentimentClass = (overview.market_sentiment || "Neutral").toLowerCase();

  return (
    <>
      <section className="card" style={{ marginBottom: "1rem" }}>
        <h1 style={{ marginTop: 0 }}>Indian Stock Market Dashboard</h1>
        <p className="small">Real-time style overview with top movers, search, and trading analytics.</p>
        <span className={`badge ${sentimentClass}`}>Market Sentiment: {overview.market_sentiment}</span>
      </section>

      <div className="grid">
        <DashboardCard title="Top Trending" items={overview.trending || []} />
        <DashboardCard title="Top Gainers" items={overview.gainers || []} />
        <DashboardCard title="Top Losers" items={overview.losers || []} />
      </div>

      <h2 className="section-title">Stock Search</h2>
      <StockSearch />
    </>
  );
}
