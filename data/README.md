# Data

Payloads in these folders are **git-ignored** (only `.gitkeep`/`README` are tracked) —
raw captures and datasets can be large and are managed out-of-band.

| Folder         | Contents                                                              |
|----------------|----------------------------------------------------------------------|
| `raw/`         | Untouched device captures (JSONL of `AssayRecord`s).                  |
| `processed/`   | Pipeline intermediates (cleaned/featurized frames).                   |
| `calibration/` | Calibration references: EIS open/short/load, CV size standards.      |
| `labels/`      | Ground-truth labels for supervised training.                         |

## Flow

`acquisition` writes → `raw/` → `datapipeline` reads `raw/` (+ `calibration/`) → writes
`processed/` and, finally, datasets into `software/datasets/`.

## Provenance

For every dataset, record: device id, firmware version, operator, sample source, and
polymer ground-truth method. Put a `manifest.json` alongside each capture batch.
