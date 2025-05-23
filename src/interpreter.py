"""Simple interpreter that resolves glyphs from a search path."""
import os

class Interpreter:
    def __init__(self, search_path=None):
        # Use the GLYPHS environment variable if provided
        self.search_path = search_path or os.environ.get('GLYPHS', './glyphs')

    def get_search_path(self):
        """Return the active search path used for glyph resolution."""
        return self.search_path
