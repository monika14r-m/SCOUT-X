class SensorManager:

    def get_gps(self):
        return (10.2, 5.1)

    def get_altitude(self):
        return 25.4

    def get_battery(self):
        return 87

    def get_camera_status(self):
        return "ACTIVE"


if __name__ == "__main__":

    sensor = SensorManager()

    print(sensor.get_gps())
    print(sensor.get_altitude())
    print(sensor.get_battery())
