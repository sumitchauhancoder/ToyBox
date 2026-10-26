import { useEffect, useMemo, useState } from "react";
import { fetchProducts } from "./api.js";
import Header from "./components/Header.jsx";
import CategoryFilter from "./components/CategoryFilter.jsx";
import ProductCard from "./components/ProductCard.jsx";
import CartDrawer from "./components/CartDrawer.jsx";

export default function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [category, setCategory] = useState("All");
  const [search, setSearch] = useState("");
  const [cartOpen, setCartOpen] = useState(false);

  useEffect(() => {
    fetchProducts()
      .then(setProducts)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  const categories = useMemo(
    () => ["All", ...new Set(products.map((p) => p.category))],
    [products]
  );

  const visible = products.filter((p) => {
    const matchesCategory = category === "All" || p.category === category;
    const matchesSearch = p.name.toLowerCase().includes(search.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  return (
    <>
      <Header onCartClick={() => setCartOpen(true)} />

      <main className="page">
        <section className="hero">
          <h1>Find your next favorite toy</h1>
          <p>Safe, fun and ready to play. Pick a group or search by name.</p>
          <input
            className="search"
            type="search"
            placeholder="Search toys, like 'bear' or 'blocks'"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            aria-label="Search toys"
          />
        </section>

        <CategoryFilter categories={categories} selected={category} onSelect={setCategory} />

        {loading && <p className="status">Unpacking the toy box… 🎁</p>}
        {error && <p className="status error">{error}. Check that your backend is running.</p>}

        {!loading && !error && visible.length === 0 && (
          <p className="status">No toys match that search. Try a different word or group.</p>
        )}

        <div className="grid">
          {visible.map((p) => (
            <ProductCard key={p.id} product={p} />
          ))}
        </div>
      </main>

      <CartDrawer open={cartOpen} onClose={() => setCartOpen(false)} />
    </>
  );
}
