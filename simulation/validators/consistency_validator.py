import math

def validate_consistency(prev_state, current_state):
    flags = []
    score = 1.0

    # Extract values safely
    try:
        prev_lat = prev_state["gps"]["lat"]
        prev_lon = prev_state["gps"]["lon"]
        curr_lat = current_state["gps"]["lat"]
        curr_lon = current_state["gps"]["lon"]

        prev_alt = prev_state.get("altitude", 0)
        curr_alt = current_state.get("altitude", 0)

        prev_t = prev_state["timestamp"]
        curr_t = current_state["timestamp"]
    except:
        return {
            "score": 0.0,
            "flags": ["STATE_ERROR"],
            "is_anomalous": True
        }

    dt = max(curr_t - prev_t, 0.001)

    # crude distance approximation
    dist = math.sqrt((curr_lat - prev_lat)**2 + (curr_lon - prev_lon)**2)
    speed = dist / dt

    if speed > 0.001:
        flags.append("GPS_JUMP")
        score -= 0.4

    if abs(curr_alt - prev_alt) > 5:
        flags.append("ALT_SPIKE")
        score -= 0.3

    if dt <= 0:
        flags.append("TIME_ERROR")
        score -= 0.5

    score = max(0.0, min(1.0, score))

    return {
        "score": score,
        "flags": flags,
        "is_anomalous": len(flags) > 0
    }
