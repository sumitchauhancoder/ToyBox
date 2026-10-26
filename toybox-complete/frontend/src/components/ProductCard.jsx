import { useCart } from "../context/CartContext.jsx";

export default function ProductCard({ product }) {
  const { addToCart } = useCart();

  return (
    <article className="card">
      <div className="card-art" style={{ background: product.color }}>
        <span className="card-emoji" aria-hidden="true">{product.emoji}</span>
        <span className="age-tag">Ages {product.age}</span>
      </div>
      <div className="card-body">
        <h3>{product.name}</h3>
        <p className="card-desc">{product.description}</p>
        <div className="card-footer">
          <span className="price">₹{product.price}</span>
          <button className="btn btn-coral" onClick={() => addToCart(product)}>
            Add to cart
          </button>
        </div>
      </div>
    </article>
  );
}
