// C:\Users\kojim\Documents\deliveryNavigator_clean\frontend\src\api\index.js
const BASE = (import.meta.env.VITE_API_BASE || "").replace(/\/$/, "");

async function jget(path) {
  const url = `${BASE}${path}`;
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.json();
}

export const api = {
  heatmap: () => jget("/api/heatmap-data/"),
  route:   () => jget("/api/daily-route/"),
  summary: () => jget("/api/daily-summary/"),
  weekly:  () => jget("/api/weekly-forecast/"),
  upload: async (file) => {
    const fd = new FormData();
    fd.append("file", file);
    const res = await fetch(`${BASE}/api/upload-screenshot/`, {
      method: "POST",
      body: fd,
    });
    if (!res.ok) throw new Error(`${res.status}`);
    return res.json();
  },
};

// 起動時に現在のBASEを確認したい場合：
// console.log("VITE_API_BASE =", import.meta.env.VITE_API_BASE);
