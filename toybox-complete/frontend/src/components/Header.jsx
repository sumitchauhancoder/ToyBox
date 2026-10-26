import { useCart } from "../context/CartContext.jsx";

export default function Header({ onCartClick }) {
  const { count } = useCart();

  return (
    <header className="header">
      <a className="logo" href="/">
        <span className="logo-block">🧸</span> ToyBox
      </a>
      <button className="btn btn-yellow" onClick={onCartClick} aria-label={`Open cart, ${count} items`}>
        🛒 Cart
        <span className="badge">{count}</span>
      </button>
    </header>
  );
}
