import React, { useRef } from "react";

export default function CardDeck({ children }) {
  const scroller = useRef(null);
  const prev = () => scroller.current?.scrollBy({ left: -360, behavior: "smooth" });
  const next = () => scroller.current?.scrollBy({ left: +360, behavior: "smooth" });

  return (
    <div className="relative">
      <div ref={scroller}
           className="flex gap-4 overflow-x-auto snap-x snap-mandatory pb-2"
           style={{ scrollSnapType: "x mandatory" }}>
        {React.Children.map(children, (child, i) => (
          <div className="min-w-[360px] md:min-w-0 md:flex-1 snap-center">{child}</div>
        ))}
      </div>

      <button onClick={prev}
              className="hidden md:flex absolute -left-4 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 items-center justify-center">
        ‹
      </button>
      <button onClick={next}
              className="hidden md:flex absolute -right-4 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 items-center justify-center">
        ›
      </button>
    </div>
  );
}
