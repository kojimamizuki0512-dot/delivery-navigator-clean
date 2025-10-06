import React, { useEffect, useMemo, useState } from "react";
import { MapContainer, TileLayer, CircleMarker, Tooltip } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { api } from "../../api";

export default function HeatmapCard() {
  const [points, setPoints] = useState([]);
  const [err, setErr] = useState("");

  useEffect(() => {
    let alive = true;
    api.heatmap()
      .then((d) => { if (alive) setPoints(d); })
      .catch((e) => { if (alive) setErr(e.message || String(e)); });
    return () => { alive = false; };
  }, []);

  const center = useMemo(() => [35.6595, 139.7005], []);

  return (
    <section className="card">
      <div className="card-title">いま強いエリア（ヒート）</div>

      <div className="rounded-xl overflow-hidden border border-white/10">
        <MapContainer
          center={center}
          zoom={14}
          style={{ height: 420, width: "100%" }}
          scrollWheelZoom
        >
          <TileLayer
            attribution='&copy; OpenStreetMap & Carto'
            url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
          />
          {points.map((p, i) => (
            <CircleMarker
              key={i}
              center={[p.lat, p.lng]}
              radius={8 + Math.round(p.intensity * 10)}
              pathOptions={{ color: "#60a5fa", fillColor: "#60a5fa", fillOpacity: 0.45 }}
            >
              <Tooltip>
                <div className="text-xs">
                  <div>強度: {p.intensity}</div>
                  <div className="mt-1 opacity-70">人気店</div>
                  <ul className="list-disc ml-4">
                    {p.restaurants?.map((r, idx) => <li key={idx}>{r}</li>)}
                  </ul>
                </div>
              </Tooltip>
            </CircleMarker>
          ))}
        </MapContainer>
      </div>

      {err && (
        <div className="mt-2 text-sm text-amber-300">地図データの取得に失敗しました（{err}）</div>
      )}
      <div className="mt-2 text-xs opacity-70">＊色が濃いほど強い（青系）</div>
    </section>
  );
}
