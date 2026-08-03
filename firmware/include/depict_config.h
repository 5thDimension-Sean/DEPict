
#pragma once

#include <cstdint>

namespace depict {

// Dielectrophoresis
struct DepConfig {
  uint32_t sweep_start_hz = 1'000;       // AC drive sweep start
  uint32_t sweep_stop_hz  = 20'000'000;  // AC drive sweep stop
  uint16_t sweep_points   = 32;          // logarithmically spaced
  float    drive_vpp      = 10.0f;       // peak-to-peak drive voltage
};

// Impedance Spectroscopy 
struct EisConfig {
  uint32_t start_hz   = 100;
  uint32_t stop_hz    = 200'000;
  uint16_t points     = 50;
  float    excite_mv  = 50.0f;           // excitation amplitude (mV) to stay linear
  uint8_t  settle_ms  = 5;
};

// Computer Vision (CV)
struct VisionConfig {
  uint16_t width      = 640;
  uint16_t height     = 480;
  uint8_t  jpeg_qual  = 12;
  float    px_per_um  = 1.0f;            // calibrated at manufacture / setup
};

// Fusion / inference
struct FusionConfig {
  float    min_confidence = 0.60f;       // below this → report "unknown"
};

struct SystemConfig {
  DepConfig     dep;
  EisConfig     eis;
  VisionConfig  vision;
  FusionConfig  fusion;
};

}  // namespace depict
