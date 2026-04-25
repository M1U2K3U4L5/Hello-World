import "./globals.css";
import Navbar from "../components/Navbar";

export const metadata = {
  title: "StockPulse India",
  description: "Indian stock analysis platform",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        <main className="container" style={{ padding: "1.2rem 0 2rem" }}>{children}</main>
      </body>
    </html>
  );
}
