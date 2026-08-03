# DEPict Hardware

Open hardware for the DEPict sensor node. Licensed under **CERN-OHL-S v2** (see
[`LICENSE`](LICENSE)).

## Contents

| Path           | What                                                                  |
|----------------|-----------------------------------------------------------------------|
| `pcb/`         | KiCad project: carrier board (MCU, EIS AFE, DDS, HV driver, camera hdr).|
| `schematics/`  | Exported PDFs / netlists for review without KiCad.                    |
| `bom/`         | Bill of materials (`bom.csv`) — kept **under $400** total.             |
| `enclosure/`   | Mechanical: microfluidic cell holder + housing (OpenSCAD / STEP).     |
| `datasheets/`  | Vendored datasheets for key parts (AFE, DDS, camera, MCU).            |
| `simulation/`  | Electrode-geometry / field simulations for the DEP cell.              |

## Functional blocks

```
 ┌──────────────┐   ┌───────────────┐   ┌───────────────┐
 │ MCU (ESP32-S3)│──│ EIS AFE (AD5941)│──│ Sense electrodes│
 └──────┬───────┘   └───────────────┘   └───────────────┘
        │           ┌───────────────┐   ┌───────────────┐
        ├──────────│ DDS (AD9833)   │──│ HV driver → DEP │
        │           └───────────────┘   │ interdigitated  │
        │                               │ electrodes      │
        │           ┌───────────────┐   └───────────────┘
        └──────────│ Camera (OV5640)│──► CV of the cell
                    └───────────────┘
```

## Manufacturing

1. Fabricate `pcb/` (2-layer, standard process).
2. Order parts per `bom/bom.csv`.
3. Print/machine `enclosure/`.
4. Assemble, then run calibration (`../software/acquisition/calibrate.py`).

> ⚠️ The DEP stage uses elevated AC voltages. Follow the safety notes in
> [`../docs/hardware/safety.md`](../docs/hardware/safety.md).
