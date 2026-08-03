import { defineConfig } from "vite";

// Proxy /api to the FastAPI backend during development.
export default defineConfig({
  server: {
    port: 5173,
    proxy: {
      "/api": "http://localhost:8000",
    },
  },
});
