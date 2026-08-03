# ML / Fusion Architecture

## Task

Multi-class classification: given tri-modal features for one particle, predict its
polymer among `{PE, PP, PS, PET, PVC, PLA}` (+ `Unknown` reject class).

## Model

A small MLP over the concatenated feature vector
(`DEP(16) ‖ EIS(32) ‖ CV(16) = 64 → hidden → 7`). Small on purpose: it must quantize to
int8 and run within the MCU's memory/latency budget. Feature dims are defined once in
`software/depict/ml/model.py` and mirrored in `firmware/include/depict_types.h`.

## Pipeline

```
 raw records ─► datapipeline (clean, featurize, fuse, split) ─► train/val/test .parquet
             ─► depict-train ─► checkpoint ─► depict-infer export ─► firmware model_data.cc
```

## Guardrails

- **No leakage**: split by physical particle id, never by row.
- **Calibrated confidence**: below `FusionConfig.min_confidence` → report `Unknown`.
- **Track everything**: dataset hash, firmware version, and metrics per model.

## Open questions

- Best EIS spectrum reduction (equivalent-circuit fit vs learned features)?
- Does DEP crossover frequency alone separate PVC/PET from the polyolefins?
- Domain shift between lab standards and field samples — needs field validation data.
