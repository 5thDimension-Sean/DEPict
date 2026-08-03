
#pragma once

#include <cstdint>

namespace depict {

class Periodic {
 public:
  explicit Periodic(uint32_t period_ms) : period_ms_(period_ms) {}
  bool due(uint32_t now_ms);

 private:
  uint32_t period_ms_;
  uint32_t last_ms_ = 0;
};

}  // namespace depict
