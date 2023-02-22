import unittest
import utils
import networkx as nx

class ReadingGraphs(unittest.TestCase):
    def test_does_return_something(self):
        graph = utils.load_graph("Exercise_0/graphs/graph_00.graphml")
        self.assertIsNotNone(graph)
    
    def test_is_nx_graph(self):
        graph = utils.load_graph("Exercise_0/graphs/graph_00.graphml")
        self.assertIs(type(graph), nx.Graph)



if __name__ == '__main__':
    unittest.main()