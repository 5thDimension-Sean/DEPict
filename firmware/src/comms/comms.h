
#pragma once

#include "depict_types.h"

namespace depict {

class Comms {
 public:
  void begin();

  bool assayRequested();                         
  void reportResult(const Classification& c);    
  void streamRaw(const DepFeatures& dep,
                 const EisFeatures& eis,
                 const VisionFeatures& cv);       // send raw features for logging
  void log(const char* msg);
};

}  // namespace depict
