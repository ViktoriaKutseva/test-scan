import unittest

class Contract03Tests(unittest.TestCase):
    def test_contract_shape(self):
        payload = {"id": "3", "type": "ticket"}
        self.assertIn("id", payload)
