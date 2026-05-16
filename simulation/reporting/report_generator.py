import json
from collections import Counter


def generate_report(log_file="attack_log.json"):
    attacks = []
    trust_scores = []

    with open(log_file, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                attacks.append(entry.get("pattern", "NORMAL"))
                trust_scores.append(entry.get("trust_score", 1.0))
            except:
                continue

    attack_counts = Counter(attacks)

    print("\n=== SCOUT-X FINAL REPORT ===")
    print(f"Total packets analyzed: {len(attacks)}")
    print(f"Average trust score: {round(sum(trust_scores)/len(trust_scores), 2)}")

    print("\nAttack classification summary:")
    for attack, count in attack_counts.items():
        print(f"{attack}: {count}")


if __name__ == "__main__":
    generate_report()