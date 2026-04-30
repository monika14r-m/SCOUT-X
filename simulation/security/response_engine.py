class ResponseEngine:
    def decide(self, data):
        trust = data.get("trust_score", 1.0)
        pattern = data.get("pattern")
        severity = data.get("severity")

        # 1. HIGHEST PRIORITY: CRITICAL ATTACK
        if pattern == "PERSISTENT_ATTACK" and severity == "HIGH":
            return "FORCE_LAND"

        # 2. LOW TRUST
        if trust < 0.3:
            return "ISOLATE_DRONE"

        # 3. INTERMITTENT ATTACK
        if pattern == "INTERMITTENT_ATTACK":
            return "LIMIT_MOVEMENT"

        # 4. MINOR
        if severity == "LOW":
            return "MONITOR"

        return "NORMAL_OPERATION"