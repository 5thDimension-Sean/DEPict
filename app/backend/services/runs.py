"""In-memory run storage (placeholder for a real DB / file store)."""

from __future__ import annotations

_RUNS: dict[str, dict] = {}


def create_stub(port: str) -> dict:
    record = {
        "record_id": f"stub-{len(_RUNS) + 1}",
        "port": port,
        "top": "Unknown",
        "confidence": 0.0,
    }
    _RUNS[record["record_id"]] = record
    return record


def list_all() -> list[dict]:
    return list(reversed(_RUNS.values()))


def get(record_id: str) -> dict:
    return _RUNS.get(record_id, {})
