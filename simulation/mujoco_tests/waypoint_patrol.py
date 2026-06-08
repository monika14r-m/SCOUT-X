import time
import math

waypoints = [
    (0, 0),
    (10, 0),
    (10, 10),
    (0, 10)
]

current_x = 0
current_y = 0

for waypoint_num, (target_x, target_y) in enumerate(waypoints, start=1):

    print(f"\nMoving to Waypoint {waypoint_num}: ({target_x}, {target_y})")

    while True:

        dx = target_x - current_x
        dy = target_y - current_y

        distance = math.sqrt(dx**2 + dy**2)

        if distance < 0.5:
            print(f"Reached Waypoint {waypoint_num}")
            break

        current_x += dx * 0.2
        current_y += dy * 0.2

        print(
            f"Position: ({current_x:.2f}, {current_y:.2f})"
        )

        time.sleep(0.2)

print("\nPatrol Complete")
