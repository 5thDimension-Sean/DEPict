
#include <unity.h>

#include "core/scheduler.h"

void test_periodic_fires_once_per_period() {
  depict::Periodic p(100);
  TEST_ASSERT_TRUE(p.due(0));      // first call fires
  TEST_ASSERT_FALSE(p.due(50));    // not yet
  TEST_ASSERT_TRUE(p.due(100));    // period elapsed
  TEST_ASSERT_FALSE(p.due(150));
}

int main(int, char**) {
  UNITY_BEGIN();
  RUN_TEST(test_periodic_fires_once_per_period);
  return UNITY_END();
}
