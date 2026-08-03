# Firmware Architecture

The sensor node runs a simple state machine over one measurement cycle:

```
 INIT ─► IDLE ─► CAPTURE_CV ─► SWEEP_EIS ─► DEP_ASSAY ─► FUSE ─► REPORT ─► IDLE
                                    ▲                              │
                                    └──────── on error ───────────┘
```

Each modality is a self-contained module (`src/dep`, `src/eis`, `src/vision`) exposing
a `begin()` + a single measurement call that returns a fixed-size feature vector
(`depict_types.h`). `src/fusion` concatenates the three vectors and runs the exported
model; `src/comms` handles the host protocol.

## Why ESP32-S3

- Integrated camera controller → CV without a second MCU.
- PSRAM → room for frame buffers + a small quantized model.
- Wi-Fi/BLE → optional untethered telemetry.
- Cheap → keeps the BOM under budget.

## Real-time notes

- Keep DEP/EIS acquisition off the allocator; pre-size all buffers.
- The HV DEP driver must have a hardware interlock; firmware also gates it behind an
  explicit enable. See [../hardware/safety.md](../hardware/safety.md).
