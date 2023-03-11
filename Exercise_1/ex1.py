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


def _ullman_recursive(mat: np.mat, g1: nx.Graph, g2: nx.Graph) -> bool:
    """
    Recursive part of the Ullman's algorithm

    Args:
        mat: Initialized Ullman matrix
        g1: A networkx graph object
        g2: A networkx graph object

    Returns:
        True if g1 is a subgraph of g2 and False otherwise
    """
    # Code here
    for w in range(1, g1.number_of_nodes()):  # Line 3 in Alg 2
        for w2 in range(1, g2.number_of_nodes()):  # Line 4 in Alg 2
            # TODO The following line, what exactly is u, v, or rather A in Serie_1.pdf
            # if mat[u, w2 - 1] != mat[v, w2 - 1]:  # Line 5 in Alg 2 TODO!
                    mat[w - 1, w2 - 1] = 0  # Line 6 in Alg 2
        for row in range(0, mat.shape[0]):  # Line 8 in Alg 2
            if mat[row, :].all() == 0:  # Line 8 in Alg 2
                return False  # Line 9 in Alg 2
    return True


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
    # Initializing future match table f(u, v) [lines 1 and 2 in Algorithm 2]
    for u in range(1, g1.number_of_nodes()):
        for v in range(1, g2.number_of_nodes()):
            if len(g1.edges(g1.nodes[u])) <= len(g2.edges(g2.nodes[v])):
                ullman_mat[u - 1, v - 1] = 1
    #           else:
    #               ullman_mat[s, t] = 0
    print(ullman_mat)
    _ullman_recursive(ullman_mat, g1, g2)

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
