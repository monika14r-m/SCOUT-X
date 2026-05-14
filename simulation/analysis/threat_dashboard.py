import json
import os

LOG_FILE = "attack_log.json"

if not os.path.exists(LOG_FILE):
    print("No attack logs found.")
    exit()

attack_count = 0
isolated_count = 0

with open(LOG_FILE, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        try:
            entry = json.loads(line)

            if entry.get("flagged"):
                attack_count += 1

            if entry.get("enforced") == "ISOLATED":
                isolated_count += 1

        except json.JSONDecodeError:
            continue

print("\n=== THREAT DASHBOARD ===")
print(f"Total detected attacks: {attack_count}")
print(f"Total drone isolations: {isolated_count}")