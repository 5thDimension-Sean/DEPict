# DEPict Firmware

On-device embedded software for the DEPict sensor node.

## Target

- **MCU**: ESP32-S3 (dual-core, PSRAM, camera interface, Wi-Fi/BLE) — chosen for the
  built-in camera controller (CV modality) and enough RAM for a small fused model.
- **Toolchain**: [PlatformIO](https://platformio.org/) + Arduino/ESP-IDF.
- Alternate board targets live in [`boards/`](boards/).

## Modules (`src/`)

| Module    | Responsibility                                                            |
|-----------|---------------------------------------------------------------------------|
| `core/`   | Scheduler, config, logging, board HAL, main loop / state machine.         |
| `dep/`    | Dielectrophoresis drive: AC waveform generation, frequency sweep control. |
| `eis/`    | Impedance spectroscopy: excitation + measurement (e.g. AD5941 AFE).       |
| `vision/` | Camera capture, ROI/particle detection, feature extraction.               |
| `fusion/` | On-device inference: runs the fused model, emits polymer class + score.   |
| `comms/`  | USB CDC / serial + Wi-Fi telemetry, command protocol, raw data streaming. |

## Build

```bash
pio run                 # build default env
pio run -t upload       # flash
pio device monitor      # serial console
pio test                # on-host unit tests (native env)
```

Or via the Makefile: `make build`, `make flash`, `make test`.

## Measurement cycle

```
 INIT ─► IDLE ─► CAPTURE_CV ─► SWEEP_EIS ─► DEP_ASSAY ─► FUSE ─► REPORT ─► IDLE
                                    ▲                              │
                                    └──────── on error ───────────┘
```

See [`../docs/architecture/firmware.md`](../docs/architecture/firmware.md).
