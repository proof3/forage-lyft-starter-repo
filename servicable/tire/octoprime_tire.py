from servicable.tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_sensor_reading: list[float]) -> None:
        self.tire_sensor_reading = tire_sensor_reading
    
    def needs_service(self) -> bool:   
        return True if sum(self.tire_sensor_reading) >= 3 else False