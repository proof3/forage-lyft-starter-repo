from abc import ABC, abstractmethod
from datetime import date

class Battery(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def need_service(self):
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def need_service(self):
        return (self.current_date - self.last_service_date).year >= 2
    
class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def need_service(self):
        return (self.current_date - self.last_service_date).year >= 4