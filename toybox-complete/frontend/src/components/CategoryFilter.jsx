export default function CategoryFilter({ categories, selected, onSelect }) {
  return (
    <div className="chips" role="group" aria-label="Toy categories">
      {categories.map((cat) => (
        <button
          key={cat}
          className={`chip ${selected === cat ? "chip-active" : ""}`}
          onClick={() => onSelect(cat)}
          aria-pressed={selected === cat}
        >
          {cat}
        </button>
      ))}
    </div>
  );
}
