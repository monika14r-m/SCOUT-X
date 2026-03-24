import time
import random
import math

class TelemetryEngine:
    def __init__(self):
        self.lat = 12.9716
        self.lon = 77.5946
        self.altitude = 10.0
        self.speed = 5.0
        self.battery = 100
        self.timestamp = time.time()
        self.sequence = 0

    def update(self):
        self.sequence += 1
        self.timestamp = time.time()

        # simulate movement
        self.lat += random.uniform(-0.0001, 0.0001)
        self.lon += random.uniform(-0.0001, 0.0001)

        # altitude fluctuation
        self.altitude += random.uniform(-0.5, 0.5)

        # speed variation
        self.speed += random.uniform(-0.2, 0.2)

        # battery drain
        self.battery -= random.uniform(0.05, 0.2)

        return self.get_packet()

    def get_packet(self):
        return {
            "seq": self.sequence,
            "timestamp": self.timestamp,
            "gps": {"lat": self.lat, "lon": self.lon},
            "altitude": round(self.altitude, 2),
            "speed": round(self.speed, 2),
            "battery": round(self.battery, 2)
        }
