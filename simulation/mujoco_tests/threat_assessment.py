import random

def assess_threat(distance, speed, restricted_zone):

    score = 0

    if restricted_zone:
        score += 50

    if distance < 5:
        score += 30

    if speed > 8:
        score += 20

    if score >= 70:
        return "HIGH"

    if score >= 40:
        return "MEDIUM"

    return "LOW"


for _ in range(10):

    distance = random.uniform(1, 20)
    speed = random.uniform(0, 15)
    restricted_zone = random.choice([True, False])

    level = assess_threat(
        distance,
        speed,
        restricted_zone
    )

    print(
        f"Distance={distance:.1f} "
        f"Speed={speed:.1f} "
        f"Zone={restricted_zone} "
        f"Threat={level}"
    )
