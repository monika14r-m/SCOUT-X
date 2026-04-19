class DefenseLogic:
    def apply_defense(self, data):
        if data.get("flagged"):
            print("[DEFENSE] Taking corrective action")

            # Clamp altitude if spoofed
            if "altitude" in data and data["altitude"] > 100:
                data["altitude"] = 100

            data["action"] = "ALTITUDE_CLAMPED"

        return data