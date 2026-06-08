import math
import time

# Drone position
drone_x = 0
drone_y = 0

# Simulated moving target
target_x = 10
target_y = 5

current_yaw = 0

def calculate_target_angle(dx, dy, tx, ty):
    return math.degrees(math.atan2(ty - dy, tx - dx))

for step in range(20):

    # Simulate target movement
    target_x += 0.5

    desired_yaw = calculate_target_angle(
        drone_x,
        drone_y,
        target_x,
        target_y
    )

    error = desired_yaw - current_yaw

    # Simple proportional controller
    current_yaw += error * 0.2

    print(
        f"Step {step} | "
        f"Target Angle: {desired_yaw:.2f}° | "
        f"Current Yaw: {current_yaw:.2f}° | "
        f"Error: {error:.2f}°"
    )

    time.sleep(0.1)
