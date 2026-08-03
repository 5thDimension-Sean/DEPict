# DEPict Data Pipeline

Offline pipeline that turns raw device records into clean, featurized, labeled
training datasets — and manages calibration references.

## Stages

```
 ingest ─► preprocess ─► features ─► fusion ─► export
```

| Stage         | Input                        | Output                               |
|---------------|------------------------------|--------------------------------------|
| `ingest/`     | raw JSONL from `acquisition` | validated `AssayRecord`s             |
| `preprocess/` | raw records                  | cleaned/normalized signals           |
| `features/`   | cleaned signals              | per-modality feature tables          |
| `fusion/`     | feature tables               | merged tri-modal feature matrix      |
| `export/`     | feature matrix + labels      | train/val/test `.parquet` datasets   |

Config for a run lives in [`config/pipeline.yaml`](config/pipeline.yaml).

## Run

```bash
make run                       # ingest → export using config/pipeline.yaml
python -m datapipeline.run --config config/pipeline.yaml
```

Outputs land in `../software/datasets/` for `depict-train` to consume.

## Design notes

- Each stage is a pure function `(input_frame) -> output_frame` so stages are testable
  and composable; the pipeline just chains them.
- Schemas come from `depict.common.schemas` — the pipeline never invents its own record
  format.
- Calibration references (open/short/load, size standards) are versioned in
  `../data/calibration/` and applied in `preprocess/`.

