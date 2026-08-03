// Minimal API client for the DEPict backend.

export async function getHealth() {
  const res = await fetch("/api/health");
  return res.json();
}

export async function runAssay(port = "/dev/ttyUSB0") {
  const res = await fetch(`/api/assays?port=${encodeURIComponent(port)}`, {
    method: "POST",
  });
  return res.json();
}

export async function listAssays() {
  const res = await fetch("/api/assays");
  return res.json();
}
