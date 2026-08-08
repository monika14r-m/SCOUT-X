import time

waypoints = [
    "Waypoint A",
    "Waypoint B",
    "Waypoint C"
]

print("Starting surveillance patrol...\n")

for point in waypoints:
    print(f"Navigating to {point}")
    time.sleep(2)

print("\nPatrol completed successfully.")
