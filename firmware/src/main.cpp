#include <Arduino.h>

#include "depict_config.h"
#include "depict_types.h"
#include "core/scheduler.h"
#include "dep/dep.h"
#include "eis/eis.h"
#include "vision/vision.h"
#include "fusion/fusion.h"
#include "comms/comms.h"

namespace {
depict::SystemConfig g_cfg;
depict::Dep     g_dep(g_cfg.dep);
depict::Eis     g_eis(g_cfg.eis);
depict::Vision  g_vision(g_cfg.vision);
depict::Fusion  g_fusion(g_cfg.fusion);
depict::Comms   g_comms;
}  // namespace

void setup() {
  g_comms.begin();
  g_comms.log("DEPict fw " DEPICT_FW_VERSION " booting");
  g_dep.begin();
  g_eis.begin();
  g_vision.begin();
  g_fusion.begin();
  g_comms.log("ready");
}

void loop() {
  if (!g_comms.assayRequested()) {
    delay(10);
    return;
  }

 
  const auto cv = g_vision.capture();

 
  const auto eis = g_eis.sweep();

 
  const auto dep = g_dep.assay();

  const depict::Classification result = g_fusion.classify(dep, eis, cv);

  g_comms.reportResult(result);
  g_comms.streamRaw(dep, eis, cv);
}
