import unittest
import networkx as nx
import ex1

class TestStringMethods(unittest.TestCase):
    def get_simple_triangle_graph(self):
        graph = nx.Graph()
        graph.add_nodes_from([1,2,3])
        graph.add_edges_from([(1,2),(2,3)])
        return graph
    
    def get_fully_connected_3_nodes_graph(self):
        graph = nx.Graph()
        graph.add_nodes_from([1,2,3])
        graph.add_edges_from([(1,2),(1,3),(2,3)])
        return graph
    
    def get_graph_from_lecture_nodes(self):
        graph_1 = nx.Graph()
        graph_1.add_nodes_from([1,2,3,4])
        graph_1.add_edges_from([(1,2),(2,3),(3,4),(4,2)])

        graph_2 = nx.Graph()
        graph_2.add_nodes_from(["a", "b", "c", "d", "e"])
        graph_2.add_edges_from([("a", "c"), ("a","e"), ("b", "d"), ("c", "b"), ("d", "c")])

        return graph_1, graph_2

    def test_self_isomorphism(self):
        graph_1 = self.get_simple_triangle_graph()
        graph_2 = self.get_simple_triangle_graph()
        is_isomorphic = ex1.is_isomorphic_brute_force(graph_1, graph_2)
        self.assertTrue(is_isomorphic)

    def test_lecture_example(self):
        graph_1, graph_2 = self.get_graph_from_lecture_nodes()
        is_isomorphic = ex1.is_isomorphic_brute_force(graph_1, graph_2)
        self.assertTrue(is_isomorphic)

    def test_fully_connected_not_fully_connected(self):
        graph_1 = self.get_simple_triangle_graph()
        graph_2 = self.get_fully_connected_3_nodes_graph()
        is_isomorphic = ex1.is_isomorphic_brute_force(graph_1, graph_2)
        self.assertFalse(is_isomorphic)

    def test_build_future_match_table(self):
        graph_1, graph_2 = self.get_graph_from_lecture_nodes()
        future_match_table = ex1.build_future_match_table(graph_1, graph_2)
        must_be = [[1,1,1,1,0],
                   [0,0,1,0,0],
                   [1,1,1,1,0],
                   [1,1,1,1,0]]
        self.assertEqual(future_match_table, must_be)

    

if __name__ == '__main__':
    unittest.main()