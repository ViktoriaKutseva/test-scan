import unittest

class Integration02Tests(unittest.TestCase):
    @unittest.skip("integration dependency unavailable")
    def test_truth(self):
        self.assertEqual(1 + 1, 2)
