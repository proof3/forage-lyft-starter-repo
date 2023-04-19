import unittest
from servicable.tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTires(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_sensor_readings = [1, 0.5, 1, 0.5]
        tires = OctoprimeTire(tire_sensor_readings)
        self.assertTrue(tires.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_sensor_readings = [1, 1, 0, 0]
        tires = OctoprimeTire(tire_sensor_readings)
        self.assertFalse(tires.needs_service())
