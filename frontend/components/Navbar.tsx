import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="nav">
      <div className="container nav-inner">
        <Link href="/" style={{ fontWeight: 700 }}>StockPulse India</Link>
        <div className="links">
          <Link href="/">Dashboard</Link>
          <Link href="/news">News</Link>
          <Link href="/portfolio">Portfolio</Link>
          <Link href="/chatbot">AI Chatbot</Link>
        </div>
      </div>
    </nav>
  );
}
