from simulation.security.response_engine import ResponseEngine
from simulation.logging.attack_logger import AttackLogger
from simulation.analysis.attack_analyzer import AttackAnalyzer

import socket
import json

analyzer = AttackAnalyzer()
logger = AttackLogger()
engine = ResponseEngine()

HOST = "127.0.0.1"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print("[GCS] Listening on port 9999...\n")

while True:
    data, addr = sock.recvfrom(4096)

    try:
        packet = json.loads(data.decode())

        # STEP 1 — Analyze attack pattern
        pattern = analyzer.analyze(packet)

        # STEP 2 — Merge pattern into packet (CRITICAL)
        enriched_packet = {**packet, **pattern}

        # STEP 3 — Decide response ONCE
        decision = engine.decide(enriched_packet)

        # STEP 4 — Attach response
        enriched_packet["response"] = decision

        # STEP 5 — Log everything
        logger.log(enriched_packet, pattern, decision)

        # STEP 6 — Clean monitoring output
        print(
            f"[SEQ {packet.get('seq')}] | "
            f"{pattern['pattern']} ({pattern['severity']}) | "
            f"Trust: {packet.get('trust_score'):.2f} | "
            f"Response: {decision}"
        )

        # Optional anomaly detail
        validation = packet.get("validation", {})
        if validation.get("is_anomalous"):
            print(f"  ⚠ Flags: {validation.get('flags')}")

    except Exception as e:
        print("[ERROR] Failed to parse packet:", e)