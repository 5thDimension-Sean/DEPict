#include "core/scheduler.h"

namespace depict {

bool Periodic::due(uint32_t now_ms) {
  if (now_ms - last_ms_ >= period_ms_) {
    last_ms_ = now_ms;
    return true;
  }
  return false;
}

}  
