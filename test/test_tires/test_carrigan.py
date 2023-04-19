import unittest
from servicable.tire.carrigan_tire import CarriganTire

class TestCarriganTires(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_sensor_readings = [0.8,0.8, 0.9, 0]
        tires = CarriganTire(tire_sensor_readings)
        self.assertTrue(tires.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_sensor_readings = [0.8,0.8, 0.89, 0]
        tires = CarriganTire(tire_sensor_readings)
        self.assertFalse(tires.needs_service())
