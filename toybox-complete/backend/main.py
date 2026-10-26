"""FastAPI application with product and order endpoints."""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from database import engine, get_db
from database_models import Base, Product, Order, OrderItem
from schemas import (
    ProductResponse,
    ProductCreate,
    OrderCreate,
    OrderCheckoutResponse,
    OrderResponse,
)

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ToyBox API",
    description="E-commerce API for kids' toys",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
#  HEALTH CHECK
# ============================================================

@app.get("/", tags=["Health"])
def health_check():
    """Health check endpoint."""
    return {
        "message": "ToyBox API is running! 🧸",
        "docs": "http://localhost:8000/docs",
    }


# ============================================================
#  PRODUCT ENDPOINTS
# ============================================================

@app.get("/api/products", response_model=List[ProductResponse], tags=["Products"])
def get_products(db: Session = Depends(get_db)):
    """Get all products."""
    products = db.query(Product).all()
    return products


@app.get(
    "/api/products/{product_id}",
    response_model=ProductResponse,
    tags=["Products"],
)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """Get a single product by ID."""
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found",
        )
    return product


@app.post("/api/products", response_model=ProductResponse, tags=["Products"])
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """Create a new product (admin only)."""
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.put(
    "/api/products/{product_id}",
    response_model=ProductResponse,
    tags=["Products"],
)
def update_product(
    product_id: int, product: ProductCreate, db: Session = Depends(get_db)
):
    """Update a product (admin only)."""
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found",
        )

    for key, value in product.model_dump().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


@app.delete("/api/products/{product_id}", tags=["Products"])
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Delete a product (admin only)."""
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found",
        )

    db.delete(db_product)
    db.commit()
    return {"message": f"Product {product_id} deleted"}


# ============================================================
#  ORDER ENDPOINTS
# ============================================================

@app.post("/api/orders", response_model=OrderCheckoutResponse, tags=["Orders"])
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """Place a new order."""
    total = 0
    order_items_data = []

    # Validate products and calculate total
    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product {item.product_id} not found",
            )

        if product.stock < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Not enough stock for {product.name}. Available: {product.stock}",
            )

        line_total = product.price * item.quantity
        total += line_total

        order_items_data.append(
            {
                "product": product,
                "quantity": item.quantity,
                "price_at_purchase": product.price,
            }
        )

    # Create order
    db_order = Order(total=total)
    db.add(db_order)
    db.flush()

    # Create order items and update stock
    for item_data in order_items_data:
        db_order_item = OrderItem(
            order_id=db_order.id,
            product_id=item_data["product"].id,
            quantity=item_data["quantity"],
            price_at_purchase=item_data["price_at_purchase"],
        )
        db.add(db_order_item)
        item_data["product"].stock -= item_data["quantity"]

    db.commit()
    db.refresh(db_order)

    return {
        "order_id": db_order.id,
        "total": db_order.total,
    }


@app.get("/api/orders/{order_id}", response_model=OrderResponse, tags=["Orders"])
def get_order(order_id: int, db: Session = Depends(get_db)):
    """Get a single order by ID."""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order {order_id} not found",
        )
    return order
