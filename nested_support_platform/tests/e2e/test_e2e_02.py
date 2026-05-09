import unittest

class E2E02Tests(unittest.TestCase):
    def test_render_path(self):
        self.assertIn("ui", "support-ui")
