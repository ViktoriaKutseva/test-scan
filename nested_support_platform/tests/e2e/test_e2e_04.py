import unittest

class E2E04Tests(unittest.TestCase):
    def test_render_path(self):
        self.assertIn("ui", "support-ui")
