from servicable.tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_sensor_reading: list[float]) -> None:
        self.tire_sensor_reading = tire_sensor_reading
    
    def needs_service(self) -> bool:
        for reading in self.tire_sensor_reading:
            if reading >= 0.9:
                return True
            
        return False