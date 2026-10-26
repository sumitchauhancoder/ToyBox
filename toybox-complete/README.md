# ToyBox – Complete E-Commerce App

A full-stack e-commerce application for kids' toys built with React, FastAPI, and PostgreSQL.

## Project Structure

```
toybox-complete/
├── frontend/          (React app)
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── CategoryFilter.jsx
│   │   │   ├── ProductCard.jsx
│   │   │   └── CartDrawer.jsx
│   │   ├── context/
│   │   │   └── CartContext.jsx
│   │   ├── data/
│   │   │   └── products.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── api.js
│   │   └── styles.css
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
│
└── backend/           (FastAPI app)
    ├── database.py
    ├── database_models.py
    ├── schemas.py
    ├── main.py
    ├── seed.py
    ├── requirements.txt
    └── README.md
```

## Quick Start

### 1. Create PostgreSQL Database

```bash
psql -U postgres
CREATE DATABASE Toybox;
\q
```

### 2. Set Up Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # or: venv\Scripts\activate (Windows)
pip install -r requirements.txt
python seed.py
uvicorn main:app --reload --port 8000
```

Backend will be at: http://localhost:8000/docs

### 3. Set Up Frontend (in a new terminal)

```bash
cd frontend
npm install
npm run dev
```

Frontend will be at: http://localhost:5173

## Features

✅ Browse 12 different toys by category
✅ Search for toys by name
✅ Add items to cart
✅ Adjust quantities and remove items
✅ Place orders
✅ Order confirmation with order ID and total

## API Endpoints

- `GET /api/products` – Get all toys
- `GET /api/products/{id}` – Get one toy
- `POST /api/products` – Create toy (admin)
- `PUT /api/products/{id}` – Update toy (admin)
- `DELETE /api/products/{id}` – Delete toy (admin)
- `POST /api/orders` – Place order
- `GET /api/orders/{id}` – Get order details

## Technologies Used

- **Frontend:** React, Vite, Context API
- **Backend:** FastAPI, SQLAlchemy, Pydantic
- **Database:** PostgreSQL
- **Styling:** CSS (custom, no frameworks)

## What You'll Learn

**React concepts:** useState, useEffect, Context API, component composition
**FastAPI concepts:** Routing, dependency injection, Pydantic validation
**Database concepts:** ORM models, relationships, foreign keys, CRUD operations
**Full Stack:** API design, CORS, request/response handling

## Next Steps

After getting it working:

1. Add user authentication (JWT)
2. Add order history for users
3. Add product filtering by price
4. Create an admin panel
5. Integrate payment processing (Stripe/Razorpay)
6. Deploy to cloud (Heroku, Render, etc.)

---

Happy coding! 🧸
