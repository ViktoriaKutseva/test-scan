import unittest

class Contract01Tests(unittest.TestCase):
    def test_contract_shape(self):
        payload = {"id": "1", "type": "ticket"}
        self.assertIn("id", payload)
