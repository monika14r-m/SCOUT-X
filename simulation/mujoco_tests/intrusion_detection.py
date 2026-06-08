import random
import time

RESTRICTED_ZONE = {
    "xmin": 5,
    "xmax": 15,
    "ymin": 5,
    "ymax": 15
}

def is_intruder_in_zone(x, y):
    return (
        RESTRICTED_ZONE["xmin"] <= x <= RESTRICTED_ZONE["xmax"]
        and
        RESTRICTED_ZONE["ymin"] <= y <= RESTRICTED_ZONE["ymax"]
    )

for step in range(20):

    intruder_x = random.randint(0, 20)
    intruder_y = random.randint(0, 20)

    print(
        f"Target Position: ({intruder_x}, {intruder_y})"
    )

    if is_intruder_in_zone(
        intruder_x,
        intruder_y
    ):
        print("[ALERT] Intruder detected!")

    time.sleep(1)
