// DEPict frontend entry point (vanilla + Vite scaffold).
import { getHealth, runAssay, listAssays } from "./api.js";

const app = document.getElementById("app");

app.innerHTML = `
  <main style="font-family: system-ui; max-width: 720px; margin: 2rem auto;">
    <h1>🔬 DEPict</h1>
    <p>Tri-modal microplastic polymer ID — DEP · EIS · CV.</p>
    <p id="status">checking backend…</p>
    <button id="run">Run assay</button>
    <h2>Recent runs</h2>
    <ul id="runs"><li>none yet</li></ul>
  </main>
`;

async function refreshStatus() {
  try {
    const h = await getHealth();
    document.getElementById("status").textContent = `backend: ${h.status} (v${h.version})`;
  } catch {
    document.getElementById("status").textContent = "backend: unreachable";
  }
}

async function refreshRuns() {
  const runs = await listAssays();
  const ul = document.getElementById("runs");
  ul.innerHTML = runs.length
    ? runs
        .map((r) => `<li>${r.record_id}: ${r.top} (${(r.confidence * 100).toFixed(0)}%)</li>`)
        .join("")
    : "<li>none yet</li>";
}

document.getElementById("run").addEventListener("click", async () => {
  await runAssay();
  await refreshRuns();
});

refreshStatus();
refreshRuns();
