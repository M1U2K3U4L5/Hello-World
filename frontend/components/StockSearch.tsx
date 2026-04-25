"use client";

import { useState } from "react";
import Link from "next/link";

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

export default function StockSearch() {
  const [q, setQ] = useState("");
  const [results, setResults] = useState<{ symbol: string; name: string }[]>([]);

  const handleSearch = async () => {
    if (!q.trim()) return;
    const res = await fetch(`${API_BASE}/stocks/search?q=${encodeURIComponent(q)}`);
    const data = await res.json();
    setResults(data.results || []);
  };

  return (
    <section className="card">
      <h3>Search NSE Stocks</h3>
      <div style={{ display: "flex", gap: "0.6rem", marginTop: "0.7rem" }}>
        <input className="input" placeholder="Try: ICICI, RELIANCE, INFY" value={q} onChange={(e) => setQ(e.target.value)} />
        <button className="button" onClick={handleSearch} style={{ width: 130 }}>Search</button>
      </div>
      <div style={{ marginTop: "1rem" }}>
        {results.map((stock) => (
          <div key={stock.symbol} style={{ marginBottom: "0.5rem" }}>
            <Link href={`/stocks/${stock.symbol}`}>{stock.symbol} - {stock.name}</Link>
          </div>
        ))}
      </div>
    </section>
  );
}
