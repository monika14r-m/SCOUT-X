import math

def validate_consistency(prev_state, current_state):
    flags = []
    score = 1.0

    try:
        lat1 = prev_state["gps"]["lat"]
        lon1 = prev_state["gps"]["lon"]
        lat2 = current_state["gps"]["lat"]
        lon2 = current_state["gps"]["lon"]

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

    # --- TIME DELTA ---
    dt = curr_t - prev_t
    if dt <= 0 or dt > 2:
        dt = 1.0

    # --- GPS DISTANCE (convert to meters) ---
    distance = math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2) * 111000

    implied_speed = distance / dt
    reported_speed = current_state.get("speed", 0)

    # --- SPEED vs GPS CHECK ---
    if abs(implied_speed - reported_speed) > 4:
        flags.append("SPEED_GPS_MISMATCH")
        score -= 0.4

    # --- GPS JUMP CHECK ---
    if distance > 20:  # >20 meters jump per tick
        flags.append("GPS_JUMP")
        score -= 0.4

    # --- ALTITUDE SPIKE ---
    if abs(curr_alt - prev_alt) > 5:
        flags.append("ALT_SPIKE")
        score -= 0.3

    # --- FINAL SCORE NORMALIZATION ---
    score = max(0.0, min(1.0, score))

    return {
        "score": score,
        "flags": flags,
        "is_anomalous": len(flags) > 0
    }