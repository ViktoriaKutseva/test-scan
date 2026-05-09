import unittest

class GraphWorkflowTests(unittest.TestCase):
    def test_parametrized_graph_edges(self):
        cases = [({"a": ["b"]}, 1), ({"a": ["b", "c"], "b": []}, 2)]
        for graph, expected_edges in cases:
            with self.subTest(graph=graph):
                edges = sum(len(v) for v in graph.values())
                self.assertEqual(edges, expected_edges)
