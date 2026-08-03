from __future__ import annotations

from pydantic import BaseModel, Field


class ImpedancePoint(BaseModel):
    freq_hz: float
    z_real: float
    z_imag: float


class ModalityFeatures(BaseModel):


    dep: list[float] = Field(default_factory=list)
    eis: list[float] = Field(default_factory=list)
    vision: list[float] = Field(default_factory=list)
    eis_spectrum: list[ImpedancePoint] = Field(default_factory=list)


class Classification(BaseModel):
    top: str  # one of depict.POLYMER_LABELS
    probs: list[float] = Field(default_factory=list)
    confidence: float = 0.0


class AssayRecord(BaseModel):


    record_id: str
    timestamp: str  # ISO-8601
    device_id: str = "unknown"
    features: ModalityFeatures
    onboard_result: Classification | None = None
    label: str | None = None  # ground-truth polymer, when known (for training)
    notes: str | None = None
