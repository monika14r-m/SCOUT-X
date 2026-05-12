from simulation.security.response_engine import ResponseEngine
from simulation.logging.attack_logger import AttackLogger
from simulation.analysis.attack_analyzer import AttackAnalyzer
from simulation.security.enforcer import ResponseEnforcer
from simulation.analysis.threat_stats import ThreatStats

import socket
import json

analyzer = AttackAnalyzer()
logger = AttackLogger()
engine = ResponseEngine()
enforcer = ResponseEnforcer()
stats = ThreatStats()

HOST = "127.0.0.1"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print("[GCS] Listening on port 9999...\n")

while True:
    data, addr = sock.recvfrom(4096)

    try:
        packet = json.loads(data.decode())

        # Analyze attack pattern
        pattern = analyzer.analyze(packet)

        # Merge packet + pattern
        enriched_packet = {**packet, **pattern}

        # Decide response
        decision = engine.decide(enriched_packet)
        enriched_packet["response"] = decision

        # Enforce action
        enriched_packet = enforcer.enforce(enriched_packet)

        # Update live stats
        stats.update(enriched_packet)
        stats.display()

        # Log event
        logger.log(enriched_packet, pattern, decision)

        # Console output
        print(
            f"[SEQ {enriched_packet.get('seq')}] | "
            f"{pattern['pattern']} ({pattern['severity']}) | "
            f"Trust: {enriched_packet.get('trust_score'):.2f} | "
            f"Response: {decision}"
        )

        validation = enriched_packet.get("validation", {})
        if validation.get("is_anomalous"):
            print(f"  ⚠ Flags: {validation.get('flags')}")

    except Exception as e:
        print("[ERROR] Failed to parse packet:", e)