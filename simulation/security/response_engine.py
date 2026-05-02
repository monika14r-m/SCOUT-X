class ResponseEngine:
    def __init__(self):
        self.attack_streak = 0

    def decide(self, data):
        trust = data.get("trust_score", 1.0)
        pattern = data.get("pattern")
        severity = data.get("severity")

        # Track attack persistence
        if pattern in ["PERSISTENT_ATTACK", "INTERMITTENT_ATTACK"]:
            self.attack_streak += 1
        else:
            self.attack_streak = max(0, self.attack_streak - 1)

        # HARD FAILSAFE
        if trust < 0.2:
            return "ISOLATE_DRONE"

        # ESCALATION based on streak
        if self.attack_streak > 5 and severity == "HIGH":
            return "FORCE_LAND"

        if self.attack_streak > 3:
            return "LIMIT_MOVEMENT"

        # Pattern-based logic
        if pattern == "INTERMITTENT_ATTACK":
            return "MONITOR"

        return "NORMAL_OPERATION"