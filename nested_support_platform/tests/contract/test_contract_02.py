import unittest

class Contract02Tests(unittest.TestCase):
    def test_contract_shape(self):
        payload = {"id": "2", "type": "ticket"}
        self.assertIn("id", payload)
