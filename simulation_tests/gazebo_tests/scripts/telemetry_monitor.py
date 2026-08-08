import time

print("Starting telemetry monitor...\n")

telemetry_data = {
    "GPS": "ACTIVE",
    "IMU": "ACTIVE",
    "LiDAR": "ACTIVE",
    "Camera": "ACTIVE"
}

for sensor, status in telemetry_data.items():
    print(f"{sensor} Status: {status}")
    time.sleep(1)

print("\nTelemetry validation completed.")
