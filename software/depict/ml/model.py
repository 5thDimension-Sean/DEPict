from __future__ import annotations

from dataclasses import dataclass

DEP_DIM = 16
EIS_DIM = 32
VISION_DIM = 16
INPUT_DIM = DEP_DIM + EIS_DIM + VISION_DIM
NUM_CLASSES = 7  # len(depict.POLYMER_LABELS)


@dataclass
class ModelConfig:
    input_dim: int = INPUT_DIM
    hidden_dim: int = 64
    num_classes: int = NUM_CLASSES
    dropout: float = 0.1


def build_model(cfg: ModelConfig | None = None):

    cfg = cfg or ModelConfig()

    return None
