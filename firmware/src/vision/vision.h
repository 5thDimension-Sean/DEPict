
#pragma once

#include "depict_config.h"
#include "depict_types.h"

namespace depict {

class Vision {
 public:
  explicit Vision(const VisionConfig& cfg) : cfg_(cfg) {}

  void begin();               // init camera sensor
  VisionFeatures capture();   // grab frame, segment particle, extract features

 private:
  VisionConfig cfg_;
};

}  // namespace depict
