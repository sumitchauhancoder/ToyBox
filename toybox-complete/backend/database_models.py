"""SQLAlchemy ORM models for database tables."""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Product(Base):
    """Product (toy) table."""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    emoji = Column(String, nullable=False)
    color = Column(String, nullable=False)
    age = Column(String, nullable=False)
    stock = Column(Integer, default=50)

    order_items = relationship("OrderItem", back_populates="product")

    def __repr__(self):
        return f"<Product id={self.id} name={self.name}>"


class Order(Base):
    """Order (purchase) table."""
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    total = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Order id={self.id} total={self.total}>"


class OrderItem(Base):
    """OrderItem (line in order) table."""
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_at_purchase = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")

    def __repr__(self):
        return f"<OrderItem order_id={self.order_id} product_id={self.product_id}>"
