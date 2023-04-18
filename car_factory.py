from datetime import date

from servicable.car import Car
from servicable.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from servicable.battery import SpindlerBattery, NubbinBattery

class CarFactory():
    def create_calliope(self, current_date: date, last_service_date: date,  current_mileage: int, last_service_mileage: int) -> Car:
        new_calliope = Car(CapuletEngine(last_service_mileage, current_mileage),
                           SpindlerBattery(last_service_date, current_date))
        return new_calliope
    
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        new_glissade = Car(WilloughbyEngine(last_service_mileage, current_mileage),
                           SpindlerBattery(last_service_date, current_date))
        return new_glissade

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        new_palindrome = Car(SternmanEngine(warning_light_on),
                           SpindlerBattery(last_service_date, current_date))
        return new_palindrome

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        new_rorschach = Car(WilloughbyEngine(last_service_mileage, current_mileage),
                           NubbinBattery(last_service_date, current_date))
        return new_rorschach

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int)-> Car:
        new_thovex = Car(CapuletEngine(last_service_mileage, current_mileage),
                           NubbinBattery(last_service_date, current_date))
        return new_thovex
