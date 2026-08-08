class NavigationManager:

    def __init__(self):
        self.current_waypoint = None

    def set_waypoint(self, x, y):
        self.current_waypoint = (x, y)

    def get_waypoint(self):
        return self.current_waypoint

    def calculate_distance(self, current_x, current_y):
        if not self.current_waypoint:
            return None

        wx, wy = self.current_waypoint

        return ((wx - current_x)**2 + (wy - current_y)**2)**0.5
