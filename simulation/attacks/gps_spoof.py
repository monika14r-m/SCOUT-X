import random
class GPSSpoof:
  def __init__(self):
    self.active = False
    self.drift = 0.0

  def execute(self, data):
      #random trigger attack
    if random.random () <0.1:
        self.active = True

    if self.active:
      #gradual drift (realistic spoofing)
      self.drift += random.uniform(0.0005,0.002)

      data["lat"] += self.drift
      data["lon"] += self.drift
      data["attack"] = "GPS_SPOOF"
    else:
      data["attack"] = "NONE"

    return data
