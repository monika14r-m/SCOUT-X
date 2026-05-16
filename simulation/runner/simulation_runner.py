from simulation.validators.consistency_validator import validate_consistency
from simulation.validators.motion_validator import validate_motion
from simulation.analysis.attack_classifier import classify_attack
from defense_logic import DefenseLogic
from security_middleware import SecurityMiddleware
from simulation.telemetry.telemetry_engine import TelemetryEngine
from simulation.logging.attack_logger import AttackLogger

import socket
import json
import time

engine = TelemetryEngine()
security = SecurityMiddleware()
defense = DefenseLogic()
logger = AttackLogger()

HOST = "127.0.0.1"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
prev_state = None

while True:
    # Step 1: generate telemetry
    data = engine.update()

    # Step 2: inject spoof attack
    if 5 < data["seq"] < 15:
        data["altitude"] += 500
        data["gps"]["lat"] += 1.5
        data["attack"] = "ALTITUDE_SPOOF"

    # Step 3: security validation
    data = security.validate_telemetry(data)
    data = defense.apply_defense(data)

    # Step 4: run validators
    consistency_result = validate_consistency(prev_state, data)
    motion_result = validate_motion(prev_state, data)

    data["validation"] = {
        "consistency": consistency_result,
        "motion": motion_result
    }

    # Step 5: classify attack
    data["classified_attack"] = classify_attack(data)

    # Step 6: send packet
    sock.sendto(json.dumps(data).encode(), (HOST, PORT))

    # Step 7: logging
    pattern = {
        "pattern": data["classified_attack"],
        "severity": "HIGH" if data.get("flagged") else "LOW"
    }

    decision = data.get("enforced", "NONE")
    logger.log(data, pattern, decision)

    # Step 8: print output
    print("[SIMULATION]", data)

    # Step 9: update previous state
    prev_state = data.copy()

    time.sleep(1)