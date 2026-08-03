# Safety

The **dielectrophoresis stage drives elevated AC voltages** across closely spaced
electrodes. Treat it with the same care as any HV bench setup.

## Rules

- **Interlock**: the HV driver must be physically disabled when the cell is open.
  Firmware also gates it behind an explicit software enable.
- **Enclosure closed** during any DEP assay.
- **No wet hands / spills** near the electrode header; the microfluidic cell handles
  liquid — keep it away from the electronics.
- **Discharge** the driver output before servicing.
- **Isolation**: power from a properly rated, isolated supply.

## Chemical

Samples may contain environmental contaminants. Wear gloves, dispose of sample fluid
per local regulations, and never eat/drink at the bench.

> This document is a placeholder checklist — complete it with real voltage/current
> figures once the hardware is finalized, and have it reviewed before publishing a
> build guide.
