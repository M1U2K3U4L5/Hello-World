"use client";

import { useState } from "react";

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

export default function ChatbotPage() {
  const [question, setQuestion] = useState("Should I buy ICICI Bank today?");
  const [answer, setAnswer] = useState<string>("");
  const [loading, setLoading] = useState(false);

  const ask = async () => {
    setLoading(true);
    const res = await fetch(`${API_BASE}/chatbot/ask`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });
    const data = await res.json();
    setAnswer(`${data.answer}\n\n${data.disclaimer}`);
    setLoading(false);
  };

  return (
    <>
      <h1>AI Stock Assistant</h1>
      <div className="card" style={{ maxWidth: 800 }}>
        <label className="small">Ask anything about NSE stocks</label>
        <textarea
          className="input"
          style={{ minHeight: 100, marginTop: "0.5rem" }}
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button className="button" style={{ marginTop: "0.8rem" }} onClick={ask} disabled={loading}>
          {loading ? "Analyzing..." : "Ask AI"}
        </button>
      </div>

      {answer && (
        <pre className="card" style={{ marginTop: "1rem", whiteSpace: "pre-wrap" }}>{answer}</pre>
      )}
    </>
  );
}
