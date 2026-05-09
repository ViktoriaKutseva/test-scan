import unittest

class Integration04Tests(unittest.TestCase):
    flaky = True
    def test_truth(self):
        self.assertEqual(1 + 1, 2)
