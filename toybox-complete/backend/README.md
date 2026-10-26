# ToyBox Backend

FastAPI e-commerce API for kids' toys.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate
pip install -r requirements.txt
```

## Create Database

```bash
psql -U postgres
CREATE DATABASE Toybox;
\q
```

## Run

```bash
python seed.py
uvicorn main:app --reload --port 8000
```

Open http://localhost:8000/docs for API documentation.
