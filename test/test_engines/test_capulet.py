import unittest
from servicable.engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(0, 30001)
        self.assertTrue(engine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        engine = CapuletEngine(0, 2000)
        self.assertFalse(engine.needs_service())