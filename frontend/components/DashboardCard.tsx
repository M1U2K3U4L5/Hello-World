import Link from "next/link";

type Item = {
  symbol: string;
  name: string;
  price: number;
  change_pct: number;
};

export default function DashboardCard({ title, items }: { title: string; items: Item[] }) {
  return (
    <section className="card">
      <h3>{title}</h3>
      {items.map((item) => (
        <div key={item.symbol} style={{ display: "flex", justifyContent: "space-between", marginTop: "0.7rem" }}>
          <div>
            <Link href={`/stocks/${item.symbol}`}><strong>{item.symbol}</strong></Link>
            <div className="small">{item.name}</div>
          </div>
          <div style={{ textAlign: "right" }}>
            <div>₹{item.price}</div>
            <div className={item.change_pct >= 0 ? "pos" : "neg"}>{item.change_pct}%</div>
          </div>
        </div>
      ))}
    </section>
  );
}
