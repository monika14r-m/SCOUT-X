class MissionState:

    def __init__(self):
        self.mode = "PATROL"
        self.current_target = None
        self.threat_level = "LOW"
        self.intrusions_detected = 0

    def update_mode(self, mode):
        self.mode = mode

    def update_threat(self, threat):
        self.threat_level = threat

    def add_intrusion(self):
        self.intrusions_detected += 1


if __name__ == "__main__":

    state = MissionState()

    state.update_mode("TRACKING")
    state.update_threat("HIGH")
    state.add_intrusion()

    print(vars(state))
