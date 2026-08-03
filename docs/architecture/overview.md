# System Architecture

DEPict has four cooperating parts. Data flows left-to-right; the trained model flows
right-to-left back onto the device.

```
 ┌───────────┐   USB/Wi-Fi   ┌───────────────┐        ┌──────────────┐
 │  firmware │ ────────────► │ datapipeline  │ ─────► │  software/ml │
 │ (sensor)  │  raw records  │ (offline ETL) │datasets│  (training)  │
 └─────┬─────┘               └───────────────┘        └──────┬───────┘
       │  ▲                                                  │
       │  └──────────── exported model (model_data.cc) ◄─────┘
       │
       ▼  results + raw
 ┌───────────┐
 │    app    │  operators trigger assays, view/label runs
 └───────────┘
```

## The three modalities

| Modality | Physical quantity                       | What it discriminates                |
|----------|-----------------------------------------|--------------------------------------|
| **DEP**  | Frequency-dependent dielectrophoretic force | Bulk permittivity / conductivity of the polymer |
| **EIS**  | Complex impedance vs frequency          | Interfacial + bulk electrical response |
| **CV**   | Morphology, size, optical texture       | Shape/appearance priors, size normalization |

No single modality separates all polymers; the learned fusion exploits their
complementarity. See [firmware.md](firmware.md) and [ml.md](ml.md).

## Design principles

- **One schema everywhere** — `depict.common.schemas` is the record contract shared by
  firmware output, pipeline, and app.
- **Model round-trips to the edge** — training happens on the host, but the model is
  quantized and shipped back into `firmware/src/fusion/`.
- **Cheap, reproducible, documented** — every result traces to a firmware version,
  calibration set, and dataset.
