"""Database connection and session management."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#local testing(commented out)
#DATABASE_URL = "postgresql://postgres:admin@localhost:5432/toybox"

#cloud production database
import os
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://toybox_user:LvrZkgKIMpizYUrKbsdzbO75IZRWD6qZ@dpg-dbffv7tg1s2s73fm15dg-a.oregon-postgres.render.com/toybox_2grl")

engine = create_engine(
    DATABASE_URL,
    echo=False,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependency function for FastAPI to provide database sessions."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
