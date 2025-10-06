import React, { useEffect, useState } from "react";
import { api } from "../../api";

export default function SummaryCard() {
  const [data, setData] = useState(null);
  const [err, setErr] = useState("");

  useEffect(() => {
    let alive = true;
    api.summary()
      .then((d) => { if (alive) setData(d); })
      .catch((e) => { if (alive) setErr(e.message || String(e)); });
    return () => { alive = false; };
  }, []);

  return (
    <section className="card">
      <div className="card-title">実績サマリー</div>

      {!data && !err && <div className="skeleton h-24" />}
      {err && <div className="text-amber-300 text-sm">サマリーの取得に失敗しました（{err}）</div>}

      {data && (
        <div className="grid grid-cols-2 gap-3">
          <div className="panel">
            <div className="text-xs opacity-70">総売上</div>
            <div className="mt-1 text-lg">¥{data.total_sales?.toLocaleString?.() ?? data.total_sales}</div>
          </div>
          <div className="panel">
            <div className="text-xs opacity-70">平均時給</div>
            <div className="mt-1 text-lg">¥{data.avg_hourly?.toLocaleString?.() ?? data.avg_hourly}</div>
          </div>
          <div className="panel">
            <div className="text-xs opacity-70">件数</div>
            <div className="mt-1 text-lg">{data.count}</div>
          </div>
          <div className="panel">
            <div className="text-xs opacity-70">稼働時間</div>
            <div className="mt-1 text-lg">{data.worked_minutes} 分</div>
          </div>
        </div>
      )}
    </section>
  );
}
