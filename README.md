# DEPict

**Tri-modal microplastic polymer identification for under $400.**

DEPict is an open-source platform that identifies the polymer type of microplastic
particles by fusing three orthogonal sensing modalities with on-device machine
learning:

1. **Dielectrophoresis (DEP)** — particles are manipulated in a non-uniform AC
   electric field; their frequency-dependent movement encodes dielectric properties.
2. **Impedance Spectroscopy (EIS)** — a swept-frequency electrical measurement of the
   particle/medium under test.
3. **Computer Vision (CV)** — morphology, size, and optical texture from a low-cost
   camera.

The three streams are fused by an on-device model to classify common environmental
polymers (PE, PP, PS, PET, PVC, PLA, …). DEPict targets a bill of materials **under
$400** as an accessible alternative to FTIR spectroscopy instruments that cost
**$30,000+**.

> Status: **early scaffold** — this repository currently contains skeleton code,
> stubs, and documentation placeholders. Nothing here is validated for scientific use
> yet.

---

## Why

FTIR and Raman spectroscopy are the gold standard for microplastic identification but
are prohibitively expensive for widespread environmental monitoring, citizen science,
and education. DEPict trades single-modality spectral precision for the redundancy of
three cheap, complementary modalities fused by ML — enough to be *useful* at a price
point that is *deployable*.

## Repository layout

| Path             | What lives here                                                        |
|------------------|-----------------------------------------------------------------------|
| `firmware/`      | Embedded code for the on-device MCU (DEP drive, EIS, camera, fusion).  |
| `hardware/`      | PCB, schematics, BOM, enclosure CAD, and reference datasheets.         |
| `software/`      | Host-side tools: acquisition, ML training/inference, models, UI.       |
| `datapipeline/`  | Offline data pipeline: ingest → preprocess → features → fusion → export.|
| `app/`           | Companion application (backend API + frontend dashboard).              |
| `data/`          | Raw, processed, calibration, and label data (git-ignored payloads).    |
| `docs/`          | Architecture, hardware, and user/developer guides.                    |
| `paper/`         | Manuscript and figures for publication.                               |

See [`docs/architecture/overview.md`](docs/architecture/overview.md) for how the
pieces connect.

## Quick start

```bash
# 1. Host-side Python tooling (acquisition, ML, pipeline)
python -m venv .venv && source .venv/bin/activate
pip install -e "software[dev]"          # see software/pyproject.toml

# 2. Firmware (PlatformIO)
cd firmware && pio run                    # build
pio run -t upload                         # flash the board

# 3. Companion app
cd app && make dev                        # backend + frontend dev servers
```

Full setup: [`docs/guides/getting-started.md`](docs/guides/getting-started.md).

## Data flow

```
  ┌─────────┐   ┌─────────┐   ┌─────────┐
  │   DEP   │   │   EIS   │   │   CV    │      on-device sensing
  └────┬────┘   └────┬────┘   └────┬────┘
       └─────────────┼─────────────┘
                ┌────▼─────┐
                │  Fusion  │  on-device ML → polymer class + confidence
                └────┬─────┘
                     │  (raw + result streamed over USB/Wi-Fi)
             ┌───────▼────────┐
             │  datapipeline  │  offline: features, training sets, calibration
             └───────┬────────┘
                ┌─────▼─────┐
                │    app    │  visualize, label, manage runs
                └───────────┘
```

## Contributing

DEPict is open hardware + open source. See [`CONTRIBUTING.md`](CONTRIBUTING.md) and
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Licensing

- **Software** (firmware, host tools, app, pipeline): [MIT](LICENSE).
- **Hardware** (PCB, schematics, enclosure): CERN-OHL-S v2 — see
  [`hardware/LICENSE`](hardware/LICENSE).
- **Documentation & paper**: CC BY 4.0.

## Citation

If you use DEPict in academic work, please cite it — see [`CITATION.cff`](CITATION.cff).


AI aided in the writing of the README and all .md files. 
