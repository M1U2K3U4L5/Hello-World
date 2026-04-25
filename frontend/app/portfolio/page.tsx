"use client";

import { useState } from "react";

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

export default function PortfolioPage() {
  const [capital, setCapital] = useState("100000");
  const [risk, setRisk] = useState("moderate");
  const [data, setData] = useState<any>(null);

  const generate = async () => {
    const res = await fetch(`${API_BASE}/portfolio/recommend`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ capital: Number(capital), risk_profile: risk }),
    });
    setData(await res.json());
  };

  return (
    <>
      <h1>Portfolio Allocator</h1>
      <div className="card" style={{ maxWidth: 600 }}>
        <label className="small">Capital (₹)</label>
        <input className="input" value={capital} onChange={(e) => setCapital(e.target.value)} />

        <label className="small" style={{ marginTop: "0.8rem", display: "block" }}>Risk Profile</label>
        <select className="select" value={risk} onChange={(e) => setRisk(e.target.value)}>
          <option value="conservative">Conservative</option>
          <option value="moderate">Moderate</option>
          <option value="aggressive">Aggressive</option>
        </select>

        <button className="button" style={{ marginTop: "1rem" }} onClick={generate}>Recommend Allocation</button>
      </div>

      {data && (
        <div className="grid" style={{ marginTop: "1rem" }}>
          {data.recommendations.map((item: any) => (
            <div className="card" key={item.bucket}>
              <strong>{item.bucket}</strong>
              <div>{item.percentage}%</div>
              <div className="small">₹{item.amount}</div>
            </div>
          ))}
        </div>
      )}
    </>
  );
}
