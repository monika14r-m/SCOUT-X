import json
from datetime import datetime

class AttackLogger:
    def __init__(self):
        self.file = "attack_log.json"

    def log(self, packet, pattern, decision):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "seq": packet.get("seq"),
            "gps": packet.get("gps"),
            "altitude": packet.get("altitude"),
            "speed": packet.get("speed"),
            "battery": packet.get("battery"),

            "trust_score": packet.get("trust_score"),
            "flagged": packet.get("flagged"),
            "action": packet.get("action"),

            "pattern": pattern.get("pattern"),
            "severity": pattern.get("severity"),

            "response": decision,  # ← THIS is what you were missing

            "flags": packet.get("validation", {}).get("flags", [])
        }

        with open(self.file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")