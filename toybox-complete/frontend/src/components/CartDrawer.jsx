import { useState } from "react";
import { useCart } from "../context/CartContext.jsx";
import { createOrder } from "../api.js";

export default function CartDrawer({ open, onClose }) {
  const { items, total, changeQuantity, removeFromCart, clearCart } = useCart();
  const [placing, setPlacing] = useState(false);
  const [error, setError] = useState("");
  const [confirmation, setConfirmation] = useState(null);

  async function handleCheckout() {
    setPlacing(true);
    setError("");
    try {
      const result = await createOrder(items);
      setConfirmation(result);
      clearCart();
    } catch (err) {
      setError(err.message);
    } finally {
      setPlacing(false);
    }
  }

  function handleClose() {
    setConfirmation(null);
    setError("");
    onClose();
  }

  if (!open) return null;

  return (
    <>
      <div className="overlay" onClick={handleClose} />
      <aside className="drawer" role="dialog" aria-label="Your cart">
        <div className="drawer-head">
          <h2>Your cart</h2>
          <button className="icon-btn" onClick={handleClose} aria-label="Close cart">✕</button>
        </div>

        {confirmation ? (
          <div className="empty">
            <div className="empty-emoji">🎉</div>
            <h3>Order placed!</h3>
            <p>Order #{confirmation.order_id} · Total ₹{confirmation.total}</p>
            <button className="btn btn-yellow" onClick={handleClose}>Keep shopping</button>
          </div>
        ) : items.length === 0 ? (
          <div className="empty">
            <div className="empty-emoji">🧺</div>
            <h3>Your cart is empty</h3>
            <p>Pick a toy you like and tap "Add to cart".</p>
            <button className="btn btn-yellow" onClick={handleClose}>Browse toys</button>
          </div>
        ) : (
          <>
            <ul className="cart-list">
              {items.map((item) => (
                <li key={item.id} className="cart-item">
                  <div className="cart-thumb" style={{ background: item.color }}>{item.emoji}</div>
                  <div className="cart-info">
                    <strong>{item.name}</strong>
                    <span>₹{item.price}</span>
                    <div className="qty">
                      <button onClick={() => changeQuantity(item.id, -1)} aria-label="Decrease quantity">−</button>
                      <span>{item.quantity}</span>
                      <button onClick={() => changeQuantity(item.id, 1)} aria-label="Increase quantity">+</button>
                    </div>
                  </div>
                  <button className="link-btn" onClick={() => removeFromCart(item.id)}>Remove</button>
                </li>
              ))}
            </ul>
            <div className="drawer-foot">
              {error && <p className="error">{error}. Please try again.</p>}
              <div className="total-row">
                <span>Total</span>
                <strong>₹{total}</strong>
              </div>
              <button className="btn btn-coral btn-wide" onClick={handleCheckout} disabled={placing}>
                {placing ? "Placing order…" : "Place order"}
              </button>
            </div>
          </>
        )}
      </aside>
    </>
  );
}
