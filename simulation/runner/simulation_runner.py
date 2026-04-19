from simulation.validators.consistency_validator import validate_consistency
from defense_logic import DefenseLogic
from security_middleware import SecurityMiddleware
from simulation.telemetry.telemetry_engine import TelemetryEngine
import socket
import json
import time

engine = TelemetryEngine()
security = SecurityMiddleware()
defense = DefenseLogic()

HOST = "127.0.0.1"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
prev_state = None

while True:
    # Step 1: update simulation state
    # engine.update()

    # Step 2: fetch telemetry data
    data = engine.update()
    # FORCE ATTACK after sequence > 5
    if data["seq"] > 5:
      data["altitude"] += 500
      data["attack"] = "ALTITUDE_SPOOF"

    # Step 3: security validation layer
    data = security.validate_telemetry(data)
    data = defense.apply_defense(data)

    if prev_state is not None:
      result = validate_consistency(prev_state, data)
    else:
      result = {
        "score": 1.0,
        "flags": [],
        "is_anomalous": False
    }

    data["validation"] = result
    prev_state = data

    # Step 4: send to ground control
    sock.sendto(json.dumps(data).encode(), (HOST, PORT))
    
    
    print("[SIMULATION]", data)

    time.sleep(1)