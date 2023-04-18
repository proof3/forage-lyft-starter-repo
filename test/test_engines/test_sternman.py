import unittest
from servicable.engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())