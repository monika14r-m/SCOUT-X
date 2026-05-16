def classify_attack(data):
    """
    Classify attack based on validation flags.
    """
    validation = data.get("validation", {})
    all_flags = []

    for section in validation.values():
        if isinstance(section, dict):
            all_flags.extend(section.get("flags", []))

    all_flags = list(set(all_flags))

    if "ALT_SPIKE" in all_flags:
        return "ALTITUDE_SPOOF"

    if "GPS_JUMP" in all_flags or "GPS_SPEED_MISMATCH" in all_flags:
        return "GPS_HIJACK"

    if "SPEED_GPS_MISMATCH" in all_flags:
        return "SENSOR_DESYNC"

    return "NORMAL"