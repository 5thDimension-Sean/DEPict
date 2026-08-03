
#pragma once

#include <array>
#include <cstdint>

namespace depict {


enum class Polymer : uint8_t {
  Unknown = 0,
  PE,   // polyethylene
  PP,   // polypropylene
  PS,   // polystyrene
  PET,  // polyethylene terephthalate
  PVC,  // polyvinyl chloride
  PLA,  // polylactic acid
  COUNT
};

constexpr std::size_t kNumClasses = static_cast<std::size_t>(Polymer::COUNT);

// One complex impedance point (real, imaginary) at a given frequency.
struct ImpedancePoint {
  float freq_hz;
  float z_real;
  float z_imag;
};

// Feature vector emitted by each modality. Sizes are placeholders.
struct DepFeatures    { std::array<float, 16> v{}; };
struct EisFeatures    { std::array<float, 32> v{}; };
struct VisionFeatures { std::array<float, 16> v{}; };

// Result of a full measurement + fusion cycle.
struct Classification {
  Polymer top = Polymer::Unknown;
  std::array<float, kNumClasses> probs{};  // softmax over classes
  float confidence = 0.0f;
  uint32_t timestamp_ms = 0;
};

}  // namespace depict
