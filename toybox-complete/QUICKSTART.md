# Quick Start Guide

## Prerequisites

- Node.js (https://nodejs.org)
- Python 3.9+ (https://www.python.org)
- PostgreSQL (https://www.postgresql.org)

## 1. Database Setup

```bash
psql -U postgres
CREATE DATABASE Toybox;
\q
```

If this fails, update the password in `backend/database.py`:
```python
DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/Toybox"
```

## 2. Backend (Terminal 1)

```bash
cd backend
python -m venv venv

# Activate
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
python seed.py
uvicorn main:app --reload --port 8000
```

You should see: `Uvicorn running on http://127.0.0.1:8000`

Visit http://localhost:8000/docs to see the API

## 3. Frontend (Terminal 2)

```bash
cd frontend
npm install
npm run dev
```

You should see: `Local: http://localhost:5173`

Visit http://localhost:5173 to see the app

## 4. Test It

1. Open http://localhost:5173
2. You should see 12 toys
3. Click "Add to cart" on any toy
4. Click "Cart" button
5. Click "Place order"
6. You should see order confirmation with order ID

## If Something Breaks

**"Cannot POST /api/orders"**
- Backend not running? Check http://localhost:8000/docs

**"Product 1 not found"**
- Did you run `python seed.py`?

**"password authentication failed"**
- PostgreSQL password is wrong. Update `backend/database.py`

**CORS errors in browser**
- Make sure frontend is on port 5173, backend on 8000

---

Good luck! 🧸
