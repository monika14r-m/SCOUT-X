class AttackAnalyzer:
    def __init__(self, window_size=10):
        self.history = []
        self.window_size = window_size

    def analyze(self, packet):
        validation = packet.get("validation", {})
        is_anomalous = validation.get("is_anomalous", False)

        # Store history
        self.history.append({
            "seq": packet.get("seq"),
            "anomaly": is_anomalous,
            "flags": validation.get("flags", [])
        })

        # Maintain fixed window
        if len(self.history) > self.window_size:
            self.history.pop(0)

        return self._detect_patterns()

    def _detect_patterns(self):
        anomaly_count = sum(1 for h in self.history if h["anomaly"])

        # Pattern 1: Persistent anomaly
        if anomaly_count >= int(0.7 * len(self.history)):
            return {
                "pattern": "PERSISTENT_ATTACK",
                "severity": "HIGH"
            }

        # Pattern 2: Frequent spikes
        if anomaly_count >= int(0.4 * len(self.history)):
            return {
                "pattern": "INTERMITTENT_ATTACK",
                "severity": "MEDIUM"
            }

        return {
            "pattern": "NORMAL",
            "severity": "LOW"
        }