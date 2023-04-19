from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def needs_service(self):
        pass