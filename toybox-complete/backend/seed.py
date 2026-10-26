"""Seed database with 12 toys."""

from database import SessionLocal, engine
from database_models import Base, Product

SEED_PRODUCTS = [
    {
        "name": "Rainbow Building Blocks",
        "category": "Blocks",
        "description": "100 chunky, colorful blocks for towers, bridges and castles.",
        "price": 799,
        "emoji": "🧱",
        "color": "#FFD23F",
        "age": "3+",
        "stock": 50,
    },
    {
        "name": "Mega Block Castle Set",
        "category": "Blocks",
        "description": "Build a castle with towers, gates and tiny knights.",
        "price": 1899,
        "emoji": "🏰",
        "color": "#FF9F68",
        "age": "5+",
        "stock": 30,
    },
    {
        "name": "Zoom Racer Car",
        "category": "Cars",
        "description": "Pull back, let go, and watch it zoom across the room.",
        "price": 499,
        "emoji": "🏎️",
        "color": "#FF6B6B",
        "age": "3+",
        "stock": 60,
    },
    {
        "name": "Rescue Fire Truck",
        "category": "Cars",
        "description": "Lights, sounds and an extendable ladder.",
        "price": 1299,
        "emoji": "🚒",
        "color": "#FF8E8E",
        "age": "4+",
        "stock": 25,
    },
    {
        "name": "Cuddly Teddy Bear",
        "category": "Plushies",
        "description": "Super soft and washable. Perfect for bedtime hugs.",
        "price": 899,
        "emoji": "🧸",
        "color": "#F7C59F",
        "age": "0+",
        "stock": 40,
    },
    {
        "name": "Sleepy Bunny",
        "category": "Plushies",
        "description": "A floppy-eared friend who loves cuddles.",
        "price": 649,
        "emoji": "🐰",
        "color": "#FFC4E1",
        "age": "0+",
        "stock": 45,
    },
    {
        "name": "Animal Jigsaw Puzzle",
        "category": "Puzzles",
        "description": "48 pieces with a big, bright jungle picture.",
        "price": 399,
        "emoji": "🧩",
        "color": "#B8A1FF",
        "age": "4+",
        "stock": 35,
    },
    {
        "name": "Space Shape Sorter",
        "category": "Puzzles",
        "description": "Match the shapes to the right holes. Great for little hands.",
        "price": 549,
        "emoji": "🚀",
        "color": "#8FA8FF",
        "age": "2+",
        "stock": 50,
    },
    {
        "name": "Washable Crayon Box",
        "category": "Art",
        "description": "24 non-toxic crayons that wash off easily.",
        "price": 249,
        "emoji": "🖍️",
        "color": "#7FDBCA",
        "age": "2+",
        "stock": 80,
    },
    {
        "name": "Paint & Splash Kit",
        "category": "Art",
        "description": "Paints, brushes and a mixing palette. Aprons included.",
        "price": 699,
        "emoji": "🎨",
        "color": "#6EC6F5",
        "age": "4+",
        "stock": 40,
    },
    {
        "name": "Bubble Blaster",
        "category": "Outdoor",
        "description": "Makes thousands of bubbles with one button.",
        "price": 449,
        "emoji": "🫧",
        "color": "#9BE3F7",
        "age": "3+",
        "stock": 55,
    },
    {
        "name": "Soccer Ball (Size 3)",
        "category": "Outdoor",
        "description": "Soft-touch ball that's easy to kick and catch.",
        "price": 599,
        "emoji": "⚽",
        "color": "#A8E6A1",
        "age": "5+",
        "stock": 35,
    },
]


def seed_database():
    """Create tables and seed the database."""
    print("🔨 Creating tables...")
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        existing_count = db.query(Product).count()
        if existing_count > 0:
            print(f"✓ Database already has {existing_count} products. Skipping seed.")
            return

        products = [Product(**data) for data in SEED_PRODUCTS]
        db.add_all(products)
        db.commit()

        print(f"✓ Seeded {len(SEED_PRODUCTS)} toys into the database!")
        print()
        print("Sample products:")
        for product in products[:3]:
            print(f"  {product.emoji}  {product.name} ({product.category}) – ₹{product.price}")

    except Exception as e:
        print(f"✗ Error seeding database: {e}")
        db.rollback()

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
