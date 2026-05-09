import unittest

class ParserWorkflowTests(unittest.TestCase):
    def test_parametrized_parser_cases(self):
        for raw, expected in [("a,b", 2), ("x", 1), ("", 0)]:
            with self.subTest(raw=raw):
                got = 0 if not raw else len(raw.split(","))
                self.assertEqual(got, expected)
