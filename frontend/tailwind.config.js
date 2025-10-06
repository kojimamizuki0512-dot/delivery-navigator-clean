/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        bg: "#0f1115",
        panel: "#141821",
        card: "#0f1320",
        text: "#e6e6e6",
      },
    },
  },
  plugins: [],
};
