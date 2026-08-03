# Getting Started

> Scaffold-stage guide. Commands describe the intended workflow; many components are
> still stubs.

## 1. Prerequisites

- Python 3.10+
- [PlatformIO](https://platformio.org/) (firmware)
- Node 18+ (app frontend)
- [KiCad 8+](https://www.kicad.org/) (only if editing hardware)

## 2. Host tooling

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e "software[ml,ui,dev]"
```

## 3. Build & flash firmware

```bash
cd firmware
pio run              # build
pio run -t upload    # flash a connected ESP32-S3
pio device monitor   # watch logs
```

## 4. Capture data

```bash
depict-acquire --port /dev/ttyUSB0 --count 20 --label PET --out data/raw/pet.jsonl
```

## 5. Build datasets → train → deploy model

```bash
python -m datapipeline.run --config datapipeline/config/pipeline.yaml
depict-train --dataset software/datasets/train.parquet --out software/models/fusion.pt
depict-infer export --model software/models/fusion.pt \
    --out firmware/src/fusion/model_data.cc
cd firmware && pio run -t upload      # ship the model to the device
```

## 6. Run the app

```bash
cd app && make install && make dev
# backend → http://localhost:8000 , frontend → http://localhost:5173
```

## Troubleshooting

- **No serial port**: check `dmesg`/permissions (`dialout` group on Linux).
- **Import errors**: ensure the venv is active and `pip install -e software` ran.
