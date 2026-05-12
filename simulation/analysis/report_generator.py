import json
from collections import Counter

class ReportGenerator:
    def __init__(self, file="attack_log.json"):
        self.file = file

    def generate(self):
        try:
            with open(self.file, "r") as f:
                logs = [json.loads(line) for line in f if line.strip()]
        except FileNotFoundError:
            print("[REPORT] No attack log found")
            return

        total = len(logs)
        responses = Counter(log.get("response", "UNKNOWN") for log in logs)
        patterns = Counter(log.get("pattern", "UNKNOWN") for log in logs)

        print("\n===== FINAL REPORT =====")
        print(f"Total Packets Logged : {total}")
        print(f"Attack Patterns      : {dict(patterns)}")
        print(f"Responses Issued     : {dict(responses)}")
        print("========================\n")