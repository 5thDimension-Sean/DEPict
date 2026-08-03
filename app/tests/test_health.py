"""Backend health-route test (requires fastapi + httpx)."""

import pytest


def test_health_ok():
    pytest.importorskip("fastapi")
    from fastapi.testclient import TestClient

    from app.backend.main import app

    client = TestClient(app)
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
