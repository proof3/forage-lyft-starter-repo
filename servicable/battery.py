from abc import ABC, abstractmethod
from datetime import date

class Battery(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days > 365 * 3
    
class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date


    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days > 365 * 4