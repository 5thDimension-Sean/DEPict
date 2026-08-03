// fusion.h — on-device sensor fusion + inference.
//
// Concatenates the three modality feature vectors and runs a small trained model
// (exported from software/ml as a TFLite-Micro / flatbuffer) to produce a polymer
// classification with calibrated confidence.
#pragma once

#include "depict_config.h"
#include "depict_types.h"

namespace depict {

class Fusion {
 public:
  explicit Fusion(const FusionConfig& cfg) : cfg_(cfg) {}

  void begin();  // load model weights into the inference runtime
  Classification classify(const DepFeatures& dep,
                          const EisFeatures& eis,
                          const VisionFeatures& cv);

 private:
  FusionConfig cfg_;
};

}  // namespace depict
