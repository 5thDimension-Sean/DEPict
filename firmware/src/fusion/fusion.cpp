#include "fusion/fusion.h"

namespace depict {

void Fusion::begin() {

}

Classification Fusion::classify(const DepFeatures& dep,
                                const EisFeatures& eis,
                                const VisionFeatures& cv) {
  Classification out;

  if (out.confidence < cfg_.min_confidence) {
    out.top = Polymer::Unknown;
  }
  return out;
}

}  
