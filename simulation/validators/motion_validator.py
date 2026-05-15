import math


def calculate_distance(prev_gps, curr_gps):
    """
    Simple Euclidean approximation for GPS delta.
    Suitable for simulation-scale movement.
    """
    lat_diff = curr_gps["lat"] - prev_gps["lat"]
    lon_diff = curr_gps["lon"] - prev_gps["lon"]

    return math.sqrt(lat_diff**2 + lon_diff**2)


def validate_motion(prev_state, current_state):
    """
    Checks whether GPS movement matches reported speed.
    Returns anomaly report.
    """
    if prev_state is None:
        return {
            "score": 1.0,
            "flags": [],
            "is_anomalous": False
        }

    prev_gps = prev_state["gps"]
    curr_gps = current_state["gps"]

    distance = calculate_distance(prev_gps, curr_gps)
    reported_speed = current_state["speed"]

    flags = []
    score = 1.0

    # crude simulation threshold
    expected_max_distance = reported_speed * 0.001

    if distance > expected_max_distance:
        flags.append("GPS_SPEED_MISMATCH")
        score -= 0.4

    return {
        "score": max(score, 0.0),
        "flags": flags,
        "is_anomalous": len(flags) > 0
    }