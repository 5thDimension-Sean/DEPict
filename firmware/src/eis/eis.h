
#pragma once

#include "depict_config.h"
#include "depict_types.h"

namespace depict {

class Eis {
 public:
  explicit Eis(const EisConfig& cfg) : cfg_(cfg) {}

  void begin();          // configure AFE, calibrate against reference resistor
  EisFeatures sweep();   // run frequency sweep, return extracted features

 private:
  EisConfig cfg_;
};

}  // namespace depict
