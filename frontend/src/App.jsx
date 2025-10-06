import React from "react";
import ErrorBoundary from "./components/common/ErrorBoundary";
import CockpitBar from "./components/layout/CockpitBar";
import CardDeck from "./components/CardDeck";
import HeatmapCard from "./components/cards/HeatmapCard";
import RouteCard from "./components/cards/RouteCard";
import SummaryCard from "./components/cards/SummaryCard";

const BASE = (import.meta.env.VITE_API_BASE || "").replace(/\/$/, "");

export default function App() {
  return (
    <div className="min-h-screen bg-bg text-text">
      {/* ヘッダー */}
      <header className="sticky top-0 z-40 backdrop-blur bg-bg/70 border-b border-white/10">
        <div className="mx-auto max-w-6xl px-4 py-3 flex items-center justify-between">
          <div className="text-white/90 font-semibold tracking-wide">Delivery Navigator</div>
          <nav className="flex gap-3 text-sm">
            <a href="#" className="px-3 py-1 rounded-lg bg-white/10 hover:bg-white/20">ホーム</a>
            <span className="px-3 py-1 rounded-lg bg-white/5">API: {BASE || "未設定"}</span>
          </nav>
        </div>
      </header>

      {/* コンテンツ */}
      <main className="mx-auto max-w-6xl px-4 py-6 space-y-6">
        {/* コックピット */}
        <CockpitBar progress={70} hourly={1780} streakMin={95} />

        {/* カードデッキ */}
        <ErrorBoundary>
          <CardDeck>
            <HeatmapCard />
            <RouteCard />
            <SummaryCard />
          </CardDeck>
        </ErrorBoundary>

        <div className="text-xs opacity-70">左右にスワイプしてカードを切り替えられます。</div>
      </main>
    </div>
  );
}
