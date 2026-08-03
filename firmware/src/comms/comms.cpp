#include "comms/comms.h"

#include <Arduino.h>

namespace depict {

void Comms::begin() {
  Serial.begin(115200);
}

bool Comms::assayRequested() {
  // TODO: parse a real command protocol. For now: any line starting with 'a'.
  if (Serial.available() && Serial.peek() == 'a') {
    while (Serial.available()) Serial.read();
    return true;
  }
  return false;
}

void Comms::reportResult(const Classification& c) {
  // TODO: emit a JSON line: {"top":..,"confidence":..,"probs":[..]}.
  Serial.printf("{\"top\":%u,\"confidence\":%.3f}\n",
                static_cast<unsigned>(c.top), c.confidence);
}

void Comms::streamRaw(const DepFeatures&, const EisFeatures&, const VisionFeatures&) {
  // TODO: stream raw feature vectors (or full spectra) for the offline pipeline.
}

void Comms::log(const char* msg) {
  Serial.printf("[log] %s\n", msg);
}

}  // namespace depict
