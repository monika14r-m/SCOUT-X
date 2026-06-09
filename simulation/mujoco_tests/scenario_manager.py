from mission_state import MissionState
from event_logger import log_event

class ScenarioManager:

    def __init__(self):
        self.state = MissionState()

    def single_intruder(self):
        log_event(
            "INFO",
            "Running Single Intruder Scenario"
        )

        self.state.update_threat("MEDIUM")

    def multiple_intruders(self):
        log_event(
            "INFO",
            "Running Multiple Intruder Scenario"
        )

        self.state.update_threat("HIGH")

    def perimeter_breach(self):
        log_event(
            "ALERT",
            "Restricted Area Breach"
        )

        self.state.update_threat("HIGH")


if __name__ == "__main__":

    manager = ScenarioManager()

    manager.single_intruder()
