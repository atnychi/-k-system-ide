import unittest
from src.sim_engine import SimEngine

class TestParseGlyph(unittest.TestCase):
    def test_known_glyph(self):
        engine = SimEngine()
        self.assertEqual(engine.parse_glyph('Ω'), 'OMEGA')

    def test_unknown_glyph(self):
        engine = SimEngine()
        self.assertEqual(engine.parse_glyph('?'), 'UNKNOWN')

if __name__ == '__main__':
    unittest.main()
