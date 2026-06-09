from mission_state import MissionState


class DroneController:

    def __init__(self):
        self.state = MissionState()

    def decide_action(self):

        if self.state.threat_level == "HIGH":
            return "TRACK_TARGET"

        if self.state.mode == "PATROL":
            return "FOLLOW_WAYPOINTS"

        return "IDLE"


if __name__ == "__main__":

    controller = DroneController()

    controller.state.update_threat("HIGH")

    action = controller.decide_action()

    print(f"Action: {action}")
