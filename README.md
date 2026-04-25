# Indian Stock Analysis Platform

A full-stack platform for Indian stock market analysis with:
- **Frontend:** Next.js (App Router)
- **Backend:** FastAPI
- **Database:** PostgreSQL
- **UI:** Modern fintech-style dark theme

## Features implemented

1. **Homepage dashboard**
   - Top trending stocks
   - Top gainers
   - Top losers
   - Market sentiment

2. **Stock search**
   - Search NSE stocks from backend API

3. **Stock details page**
   - TradingView widget integration
   - Moving averages (SMA20/SMA50)
   - RSI
   - MACD
   - Buy zone / Sell zone / Stop loss insights

4. **News section**
   - Latest stock news feed endpoint
   - Rule-based sentiment analysis

5. **Portfolio section**
   - User capital input
   - Allocation recommendation based on risk profile

6. **AI chatbot endpoint**
   - Example: “Should I buy ICICI Bank today?”
   - Returns transparent, rules-based response with risk notes

---

## Project structure

```
.
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── services
│   │   │   ├── market_data.py
│   │   │   ├── sentiment.py
│   │   │   ├── portfolio.py
│   │   │   └── chatbot.py
│   │   └── routers
│   │       ├── market.py
│   │       ├── stocks.py
│   │       ├── news.py
│   │       ├── portfolio.py
│   │       └── chatbot.py
│   └── requirements.txt
├── frontend
│   ├── app
│   │   ├── page.tsx
│   │   ├── stocks/[symbol]/page.tsx
│   │   ├── news/page.tsx
│   │   ├── portfolio/page.tsx
│   │   └── chatbot/page.tsx
│   ├── components
│   │   ├── Navbar.tsx
│   │   ├── DashboardCard.tsx
│   │   ├── StockSearch.tsx
│   │   └── TradingViewWidget.tsx
│   └── package.json
├── db
│   └── init.sql
└── docker-compose.yml
```

---

## Quick start

### 1) Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 2) Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: `http://localhost:3000`  
Backend: `http://localhost:8000`  
API docs: `http://localhost:8000/docs`

---

## Environment variables

### Backend (`backend/.env`)

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/stock_platform
ALLOWED_ORIGINS=http://localhost:3000
```

### Frontend (`frontend/.env.local`)

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

> If you run through `docker compose`, frontend server-side requests should use the backend service hostname:
>
> `NEXT_PUBLIC_API_BASE_URL=http://backend:8000`

---

## Notes

- Market data helper uses Yahoo Finance symbols with `.NS` suffix.
- Endpoints include fallback mock values to keep the UI functional in local/offline environments.
- AI chatbot is designed for educational use and is **not financial advice**.
