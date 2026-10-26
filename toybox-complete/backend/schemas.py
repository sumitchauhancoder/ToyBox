"""Pydantic request/response schemas."""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class ProductCreate(BaseModel):
    """Schema for creating a product."""
    name: str
    category: str
    description: str
    price: int = Field(gt=0)
    emoji: str
    color: str
    age: str
    stock: int = Field(default=50, ge=0)


class ProductResponse(BaseModel):
    """Schema for returning a product."""
    id: int
    name: str
    category: str
    description: str
    price: int
    emoji: str
    color: str
    age: str
    stock: int

    class Config:
        from_attributes = True


class OrderItemCreate(BaseModel):
    """Schema for items in an order."""
    product_id: int
    quantity: int = Field(gt=0)


class OrderItemResponse(BaseModel):
    """Schema for returning an order item."""
    id: int
    product_id: int
    quantity: int
    price_at_purchase: int

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    """Schema for creating an order."""
    items: List[OrderItemCreate] = Field(min_items=1)


class OrderCheckoutResponse(BaseModel):
    """Schema for checkout response."""
    order_id: int
    total: int


class OrderResponse(BaseModel):
    """Schema for returning a full order."""
    id: int
    total: int
    created_at: datetime
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True
