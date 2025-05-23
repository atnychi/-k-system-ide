# Core simulation engine

GLYPH_MAP = {
    'Ω': 'OMEGA',
    'Δ': 'DELTA',
    '⦿': 'CIRCLE_WITH_DOT',
}

class SimEngine:
    def parse_glyph(self, glyph):
        """Return a simple name for the glyph or 'UNKNOWN'."""
        return GLYPH_MAP.get(glyph, 'UNKNOWN')

    def simulate(self, input_signal):
        return f"Simulated output for: {input_signal}"
