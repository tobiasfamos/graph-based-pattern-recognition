import unittest
from utils import compare_graphs_naive, load_graph
import utils
import networkx as nx
import ex0
import os

def emtpy_drawings_folder():

    for filename in os.listdir("Exercise_0/drawings"):       
        try :
            os.remove(filename)            
        except:
            pass
    

def is_directory_empty(path):  
    dir = os.listdir(path)
    return len(dir) == 0

class ReadingGraphs(unittest.TestCase):
    def test_does_return_something(self):
        graph = utils.load_graph("Exercise_0/graphs/graph_00.graphml")
        self.assertIsNotNone(graph)
    
    def test_is_nx_graph(self):
        graph = utils.load_graph("Exercise_0/graphs/graph_00.graphml")
        self.assertIs(type(graph), nx.Graph)

    def test_part_1_returns_list(self):
        result = ex0.part1()
        self.assertIs(type(result), list)

    def test_part_1_returns_list_of_graphs(self):
        results = ex0.part1()
        for result in results:
            self.assertIs(type(result), nx.Graph) 

    def test_part_1_plots_graphs(self):
        emtpy_drawings_folder()
        resutls = ex0.part1()
        self.assertFalse(is_directory_empty("Exercise_0/drawings"))


class ComparingGraphs(unittest.TestCase):
    graph_0 = load_graph("Exercise_0/graphs/graph_00.graphml")
    graph_1 = load_graph("Exercise_0/graphs/graph_01.graphml")
    graph_2 = load_graph("Exercise_0/graphs/graph_02.graphml")
    graph_3 = load_graph("Exercise_0/graphs/graph_03.graphml")
    graph_4 = load_graph("Exercise_0/graphs/graph_04.graphml")


    def test_same_numer_of_nodes(self):
        self.assertFalse(compare_graphs_naive(self.graph_0, self.graph_1))
        self.assertTrue(compare_graphs_naive(self.graph_0, self.graph_2))
        # Graph 0 != Graph 1
        # Graph 0 == Graph 2
        

    def test_number_of_edges(self):
        # 0 == 1
        # 1 != 2
        self.assertFalse(compare_graphs_naive(self.graph_0, self.graph_1))
        self.assertTrue(compare_graphs_naive(self.graph_0, self.graph_2))
        

    def test_number_of_labels(self):
        # 0 != 1
        # 2 == 4    
        self.assertFalse(compare_graphs_naive(self.graph_0, self.graph_1))
        self.assertTrue(compare_graphs_naive(self.graph_2, self.graph_4))


if __name__ == '__main__':
    unittest.main()