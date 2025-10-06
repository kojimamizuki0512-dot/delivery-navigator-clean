import React from "react";

export default function CockpitBar({ progress = 70, hourly = 1780, streakMin = 95 }) {
  return (
    <div className="panel border border-white/10">
      <div className="text-sm opacity-80 mb-2">本日の目標達成率</div>
      <div className="h-2 rounded-full bg-white/10 overflow-hidden">
        <div className="h-full bg-blue-500" style={{ width: `${progress}%` }} />
      </div>
      <div className="mt-2 text-xs opacity-80 flex gap-4">
        <div>現在の時給 <span className="opacity-100">¥{hourly.toLocaleString()}</span></div>
        <div>連続稼働 <span className="opacity-100">{streakMin}分</span></div>
      </div>
    </div>
  );
}
