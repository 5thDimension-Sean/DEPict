// dep.h — Dielectrophoresis assay control.
//
// Drives a non-uniform AC field across a logarithmic frequency sweep and observes
// the frequency-dependent response of particles (crossover frequency etc.), which
// encodes their effective dielectric properties.
#pragma once

#include "depict_config.h"
#include "depict_types.h"

namespace depict {

class Dep {
 public:
  explicit Dep(const DepConfig& cfg) : cfg_(cfg) {}

  void begin();               // configure signal generator / DDS + electrode driver
  DepFeatures assay();        // run sweep, return extracted features

 private:
  DepConfig cfg_;
};

}  // namespace depict
