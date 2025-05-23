import unittest
from src.sim_engine import SimEngine

class TestSimEngine(unittest.TestCase):
    def test_simulate(self):
        engine = SimEngine()
        self.assertIn('⦿ΔΩ', engine.simulate('⦿ΔΩ'))

if __name__ == '__main__':
    unittest.main()
