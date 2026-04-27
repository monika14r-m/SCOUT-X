class ResponseEngine:
    def decide(self, data):
        trust = data.get("trust_score", 1.0)
        pattern = data.get("pattern")
        severity = data.get("severity")

        # HARD DEFENSE
        if trust < 0.3:
            return "ISOLATE_DRONE"

        # PERSISTENT ATTACK = ESCALATE
        if pattern == "PERSISTENT_ATTACK" and severity == "HIGH":
            return "FORCE_LAND"

        # INTERMITTENT ATTACK
        if pattern == "INTERMITTENT_ATTACK":
            return "LIMIT_MOVEMENT"

        # MINOR ISSUES
        if severity == "LOW":
            return "MONITOR"

        return "NORMAL_OPERATION"