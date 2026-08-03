"""Assay endpoints: trigger a measurement and list past runs."""

from __future__ import annotations

from fastapi import APIRouter

from ..services import runs

router = APIRouter(prefix="/api/assays", tags=["assays"])


@router.post("")
def run_assay(port: str = "/dev/ttyUSB0") -> dict:
    """Trigger a new assay on the connected device and store the result."""
    # TODO: call services.device.run_assay(port), persist via services.runs.
    record = runs.create_stub(port)
    return record


@router.get("")
def list_assays() -> list[dict]:
    """Return stored assay records (most recent first)."""
    return runs.list_all()


@router.get("/{record_id}")
def get_assay(record_id: str) -> dict:
    return runs.get(record_id)
