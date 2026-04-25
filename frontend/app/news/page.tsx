const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

async function getNews() {
  const res = await fetch(`${API_BASE}/news/latest`, { cache: "no-store" });
  return res.json();
}

export default async function NewsPage() {
  const news = await getNews();

  return (
    <>
      <h1>Latest Stock News</h1>
      <div className="grid">
        {news.map((item: any) => (
          <article className="card" key={item.url}>
            <div className={`badge ${item.sentiment === "positive" ? "bullish" : item.sentiment === "negative" ? "bearish" : "neutral"}`}>
              {item.sentiment}
            </div>
            <h3>{item.title}</h3>
            <div className="small">{item.source}</div>
            <a href={item.url} target="_blank">Read</a>
          </article>
        ))}
      </div>
    </>
  );
}
