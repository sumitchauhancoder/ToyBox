import { products as mockProducts } from "./data/products.js";

const USE_MOCK = true;
const API_URL = "/api";

const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

export async function fetchProducts() {
  if (USE_MOCK) {
    await wait(600);
    return mockProducts;
  }
  const res = await fetch(`${API_URL}/products`);
  if (!res.ok) throw new Error("Could not load toys");
  return res.json();
}

export async function createOrder(items) {
  if (USE_MOCK) {
    await wait(800);
    const total = items.reduce((sum, i) => sum + i.price * i.quantity, 0);
    return { order_id: Math.floor(Math.random() * 9000) + 1000, total };
  }
  const res = await fetch(`${API_URL}/orders`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      items: items.map((i) => ({ product_id: i.id, quantity: i.quantity })),
    }),
  });
  if (!res.ok) throw new Error("Could not place order");
  return res.json();
}
