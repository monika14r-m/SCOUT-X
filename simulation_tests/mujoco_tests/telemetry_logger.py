import csv
import time
import random

LOG_FILE = "telemetry.csv"

with open(LOG_FILE, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "x",
        "y",
        "z",
        "velocity"
    ])

    x, y, z = 0, 0, 10

    for _ in range(50):
        x += random.uniform(0.1, 1.0)
        y += random.uniform(0.1, 1.0)

        velocity = random.uniform(5, 15)

        writer.writerow([
            time.time(),
            round(x, 2),
            round(y, 2),
            z,
            round(velocity, 2)
        ])

        print(
            f"Position=({x:.2f},{y:.2f},{z}) "
            f"Velocity={velocity:.2f}"
        )

        time.sleep(0.1)

print(f"Saved telemetry to {LOG_FILE}")
