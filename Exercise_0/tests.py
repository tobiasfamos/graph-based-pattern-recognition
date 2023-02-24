import unittest
import utils
import networkx as nx
import ex0
import os

def emtpy_drawings_folder():

    for filename in os.listdir("Exercise_0/drawings"):        
        os.remove(filename)

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
        self.assertTrue(is_directory_empty("Exercise_0/drawings"))




if __name__ == '__main__':
    unittest.main()