#######################
#
# Name: Tobias Famos
# Matriculation Number:
#
# Name: Brian Schweigler
# Matriculation Number:
#
#######################


from typing import List

import networkx as nx
import numpy as np
from utils import load_graph, draw_graph, COLOR_MAP, NODE_LABEL, get_node_colors

import os


#################
#    Part 1     #
#################

def turn_name_to_png(filename : str):
    name = filename.split(".")[0]
    return name + ".png"

def part1() -> List[nx.Graph]:
    """
    1. Load all the graphs in './graphs'
    2. Plot and save the corresponding graph drawing in './drawings'
    3. Return the list of loaded graphs

    Returns:
        The list of loaded graphs
    """
    list_of_graphs = []
    for filename in os.listdir("Exercise_0/graphs"):
        png_file_name = turn_name_to_png(filename)
        graph = load_graph("Exercise_0/graphs/" + filename)
        list_of_graphs.append(graph)
        node_labels = dict(graph.nodes(data="x"))
        draw_graph(graph, "Exercise_0/drawings/"+png_file_name, node_labels, get_node_colors(graph), nx.layout.planar_layout)
        
    return list_of_graphs


#################
#    Part 2     #
#################

def naive_graph_isomorphism(graph1: nx.Graph, graph2: nx.Graph) -> bool:
    """
    This function checks if two input graphs are isomorphic
    by comparing the number of nodes, number of edges and the labels of the nodes.

    Args:
        graph1: A networkx graph object
        graph2: A networkx graph object

    Returns:
        Returns True if the input graphs are isomorphic, else False.
    """
    # Code here
    return False


def part2(graphs: List[nx.Graph]) -> None:
    """
    1. Complete 'naive_graph_isomorphism(graph1, graph2)'
    2. Construct an NxN matrix in which each element represents
       the result of the isomorphic test between two graphs.
       The value at the intersection of row i and column j indicating
       whether the i-th and j-t graphs are isomorphic.
    3. Save the NxN matrix in './results/naive_isomorphic_test.csv'

    Args:
        graphs: A list of networkx graph objects

    """
    # Code here
    pass


def main():
    # Run part 1
    graphs = part1()

    # Run part 2
    part2(graphs)


if __name__ == '__main__':
    main()
