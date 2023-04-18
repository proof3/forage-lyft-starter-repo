from servicable.servicable import Servicable
from servicable.engine import Engine
from servicable.battery import Battery

class Car(Servicable):
    def __init__(self, engine: Engine, battery: Battery) -> None:
        self.engine = engine
        self.battery = battery
    
    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()