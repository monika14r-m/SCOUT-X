import json
from collections import Counter


def generate_report(log_file="attack_log.json"):
    attacks = []
    trust_scores = []
    isolated_count = 0

    with open(log_file, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())

                attack_type = entry.get("pattern", "NORMAL")
                attacks.append(attack_type)

                trust = entry.get("trust_score", 1.0)
                trust_scores.append(trust)

                if entry.get("enforced") == "ISOLATED":
                    isolated_count += 1

            except:
                continue

    if not attacks:
        print("No logs found.")
        return

    attack_counts = Counter(attacks)
    most_common_attack = attack_counts.most_common(1)[0]

    print("\n=== SCOUT-X FINAL SECURITY REPORT ===")
    print(f"Total packets analyzed: {len(attacks)}")
    print(f"Average trust score: {round(sum(trust_scores) / len(trust_scores), 2)}")
    print(f"Total isolated packets: {isolated_count}")
    print(f"Most frequent attack: {most_common_attack[0]} ({most_common_attack[1]} events)")

    print("\nAttack breakdown:")
    for attack, count in attack_counts.items():
        print(f"{attack}: {count}")


if __name__ == "__main__":
    generate_report()