# Board targets

Board-specific pin maps and build variants.

- **esp32s3** (default) — ESP32-S3 DevKitC-1 with PSRAM; camera + AFE + DDS attached
  to the DEPict carrier PCB (`../../hardware/pcb`).

Add a new target by creating an `[env:<name>]` in `../platformio.ini` and a pin-map
header here (e.g. `pins_esp32s3.h`).
