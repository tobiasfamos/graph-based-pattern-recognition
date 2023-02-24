#######################
#
# Name: Tobias Famos
# Matriculation Number: 16-933-764
#
# Name: Brian Schweigler
# Matriculation Number: 16-102-071
#
#######################


from typing import List

import networkx as nx
import numpy as np
import csv
import os
import matplotlib.pyplot as plt
import utils

from utils import load_graph, draw_graph, COLOR_MAP, NODE_LABEL


#################
#    Part 1     #
#################

def part1() -> List[nx.Graph]:
    """
    1. Load all the graphs in './graphs'
    2. Plot and save the corresponding graph drawing in './drawings'
    3. Return the list of loaded graphs

    Returns:
        The list of loaded graphs
    """
    graph_list = []
    i = 0
    for file in os.scandir('graphs'):  # For loop through files
        if not file.name.endswith('.graphml'):  # If the file is not an .graphml
            continue  # Do nothing and go to next iteration
        G = nx.read_graphml(file.path)
        graph_list.append(G)
        nx.draw(G, with_labels=True, font_weight='bold', node_color=list(utils.COLOR_MAP.values())[0:len(G.nodes())])
        # TODO Does this work on non-windows?
        plt.savefig("drawings/graph_" + str(i))
        plt.show()
        i = i+1

    return graph_list


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

    if ((len(graph1.nodes()) == len(graph2.nodes)) and
            (len(graph1.edges()) == len(graph2.edges)) and
            (set(graph1.nodes().keys()) == set(graph2.nodes().keys()))):
        return True

    return False


def part2(graphs: List[nx.Graph]) -> None:
    """
    1. Complete 'naive_graph_isomorphism(graph1, graph2)' X
    2. Construct an NxN matrix in which each element represents
       the result of the isomorphic test between two graphs.
       The value at the intersection of row i and column j indicating
       whether the i-th and j-t graphs are isomorphic.
    3. Save the NxN matrix in './results/naive_isomorphic_test.csv'

    Args:
        graphs: A list of networkx graph objects

    """
    matrix = []
    for graph in graphs:
        current_row = []
        for compare_to in graphs:
            if(naive_graph_isomorphism(graph, compare_to)):
                current_row.append(1)
            else: 
                current_row.append(0)
        matrix.append(current_row)

        with open('./results/naive_isomorphic_test.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(matrix)



def main():
    # Run part 1
    graphs = part1()

    # Run part 2
    part2(graphs)


if __name__ == '__main__':
    main()
