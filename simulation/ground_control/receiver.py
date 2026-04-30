from simulation.security.response_engine import ResponseEngine
from simulation.logging.attack_logger import AttackLogger
from simulation.analysis.attack_analyzer import AttackAnalyzer
analyzer = AttackAnalyzer()
logger = AttackLogger()
engine = ResponseEngine()

import socket
import json

HOST = "127.0.0.1"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print("[GCS] Listening on port 9999...\n")

while True:
    data, addr = sock.recvfrom(4096)

    try:
        packet = json.loads(data.decode())

        pattern = analyzer.analyze(packet)

        decision = engine.decide({**packet, **pattern})

        logger.log(packet, pattern, decision)

        decision = engine.decide({**packet, **pattern})
        packet["response"] = decision
        print(f"Response Decision: {decision}")

        print(f"Pattern: {pattern['pattern']}")
        print(f"Severity: {pattern['severity']}")

        print("=" * 50)
        print(f"[RECEIVED] SEQ: {packet.get('seq')}")

        print(f"GPS: {packet.get('gps')}")
        print(f"Altitude: {packet.get('altitude')}")
        print(f"Speed: {packet.get('speed')}")
        print(f"Battery: {packet.get('battery')}")

        print(f"Trust Score: {packet.get('trust_score')}")
        print(f"Flagged: {packet.get('flagged')}")
        print(f"Action: {packet.get('action', 'NONE')}")

        validation = packet.get("validation", {})
        print(f"Validation Score: {validation.get('score')}")
        print(f"Flags: {validation.get('flags')}")

        if validation.get("is_anomalous"):
            print(">>> ANOMALY DETECTED <<<")

    except Exception as e:
        print("[ERROR] Failed to parse packet:", e)