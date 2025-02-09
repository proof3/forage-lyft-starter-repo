from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int) -> None:
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000
    
class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool) -> None:
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on
    
class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int) -> None:
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000