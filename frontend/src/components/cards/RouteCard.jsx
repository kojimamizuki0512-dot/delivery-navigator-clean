import React, { useEffect, useState } from "react";
import { api } from "../../api";

export default function RouteCard() {
  const [data, setData] = useState(null);
  const [err, setErr] = useState("");

  async function load() {
    setErr("");
    try {
      const d = await api.route();
      setData(d);
    } catch (e) {
      setErr(e.message || String(e));
    }
  }

  useEffect(() => { load(); }, []);

  return (
    <section className="card">
      <div className="card-title">今日のおすすめルート</div>

      {!data && !err && <div className="skeleton h-20" />}
      {err && <div className="text-amber-300 text-sm">ルートの取得に失敗しました（{err}）</div>}

      {data && (
        <>
          <div className="grid grid-cols-2 gap-3 mb-3">
            <div className="panel">
              <div className="opacity-70 text-xs">本日の推奨エリア</div>
              <div className="mt-1 text-lg">{data.recommended_area}</div>
            </div>
            <div className="panel">
              <div className="opacity-70 text-xs">予測日給</div>
              <div className="mt-1 text-lg">¥{data.predicted_income.toLocaleString()}</div>
            </div>
          </div>

          <div className="space-y-2">
            {data.timeline.map((t, i) => (
              <div key={i} className="panel">
                <div className="font-semibold">{t.time}</div>
                <div className="opacity-90 mt-1">{t.action}</div>
              </div>
            ))}
          </div>

          <div className="text-xs opacity-60 mt-3">＊状況により30〜60分ごとに自動で最適化（ここではダミー）</div>
        </>
      )}

      <div className="mt-4">
        <button onClick={load} className="btn">今日のプランを作成</button>
      </div>
    </section>
  );
}
