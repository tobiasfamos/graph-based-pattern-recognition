#######################
#
# Name: Tobias Famos
# Matriculation Number: 16-933-764
#
# Name: Brian Schweigler
# Matriculation Number: 16-102-071
#
#######################

import networkx as nx
import numpy as np

from utils import load_graph, load_all_graphs, draw_graph, draw_all_graphs


# You can potentially add more code here (constants, functions, ...)


def _ullman_recursive() -> bool:
    """
    Recursive part of the Ullman's algorithm
    # TODO Is this the pruning part?
    Returns:
        True if g1 is a subgraph of g2 and False otherwise
    """
    # Code here
    return False


def Ullman(g1: nx.Graph, g2: nx.Graph) -> bool:
    """
    Perform the subgraph isomorphism test between g1 and g2

    Args:
        g1: A networkx graph object
        g2: A networkx graph object

    Returns:
        True if g1 is a subgraph of g2 and False otherwise
    """
    ullman_mat = np.zeros((g1.number_of_nodes(), g2.number_of_nodes()))
    for s in range(1, g1.number_of_nodes()):
        for t in range(1, g2.number_of_nodes()):
            if len(g1.edges(g1.nodes[s])) <= len(g2.edges(g2.nodes[t])):
                ullman_mat[s-1, t-1] = 1
#           else:
#               ullman_mat[s, t] = 0

    print(ullman_mat)
    # TODO
    if ullman_mat.all() == 1:
        return True
    return False


if __name__ == '__main__':
    # 1. Load the graphs in the './graphs' folder
    graphs = load_all_graphs("./graphs")

    # 1.5 (You can visualize the graphs using utils.draw_all_graphs())
    draw_all_graphs(graphs, "./graphs", False)

    # 2. Perform the Ullman's subgraph isomorphic test between all pairs of graphs.
    matrix = np.zeros((len(graphs), len(graphs)))
    for i in range(len(graphs)):
        for j in range(len(graphs)):
            if Ullman(graphs[i], graphs[j]):
                matrix[i, j] = 1

    np.savetxt("./results/ullman_subgraph_isomorphism.csv", matrix, fmt="%f", delimiter=",")

    pass
