import unittest
import networkx as nx
import ex1

class TestStringMethods(unittest.TestCase):
    def get_simple_triangle_graph(self):
        graph = nx.Graph()
        graph.add_nodes_from([1,2,3])
        graph.add_edges_from([(1,2),(2,3)])
        return graph
    
    def test_self_isomorphism(self):
        graph_1 = self.get_simple_triangle_graph()
        graph_2 = self.get_simple_triangle_graph()
        is_isomorphic = ex1.Ullman(graph_1, graph_2)
        self.assertTrue(is_isomorphic)

if __name__ == '__main__':
    unittest.main()