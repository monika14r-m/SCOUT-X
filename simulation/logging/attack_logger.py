import json
from datetime import datetime

class AttackLogger:
    def __init__(self, file_path="attack_logs.json"):
        self.file_path = file_path

    def log(self, packet, pattern):
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
            "flags": packet.get("validation", {}).get("flags", [])
        }

        with open(self.file_path, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

        if pattern.get("severity") == "HIGH":
            with open("high_severity_logs.json", "a") as f:
                f.write(json.dumps(log_entry) + "\n")