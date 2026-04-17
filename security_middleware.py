class SecurityMiddleware:
    def __init__(self):
        self.trust_score = 1.0
        self.anomaly_threshold = 0.6

    def validate_telemetry(self, data):
        """
        Main entry point for all telemetry data
        """
        anomaly = self.detect_anomaly(data)

        if anomaly:
            self.update_trust(flag=True)
            data["flagged"] = True
        else:
            self.update_trust(flag=False)
            data["flagged"] = False

        data["trust_score"] = self.trust_score
        return data

    def detect_anomaly(self, data):
        """
        Basic rule-based anomaly detection (expand later)
        """
        if "gps" in data:
            gps = data["gps"]

            # Simple sanity check: values out of range
            if abs(gps.get("lat", 0)) > 90 or abs(gps.get("lon", 0)) > 180:
                return True

        if data.get("noise_level", 0) > 0.8:
            return True

        return False

    def update_trust(self, flag):
        """
        Adjust trust score based on behavior
        """
        if flag:
            self.trust_score -= 0.1
        else:
            self.trust_score += 0.02

        # clamp between 0 and 1
        self.trust_score = max(0.0, min(1.0, self.trust_score))