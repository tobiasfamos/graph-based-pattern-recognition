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


def _ullman_recursive(adj_u: list, adj_v: list, P: list, Q: list) -> bool:
    """
    Recursive part of the Ullman's algorithm

    Args:
        adj_u: Adjacency matrix of g1 as a list
        adj_v: Adjacency matrix of g2 as a list
        P: List of nodes of g1
        Q: List of nodes of g2

    Returns:
        True if g1 is a subgraph of g2 and False otherwise
    """

    # Base case: all vertices have been matched
    if not P:
        return True

    # Select the next vertex to match
    v = Q[0]

    # Try to match u with each vertex in P
    for u in P:
        if adj_u[u][u] == adj_v[v][v] and all(adj_u[u][w] == adj_v[v][q] for q, w in enumerate(Q) if w != v):
            # Found a valid match, update the partial mapping
            P.remove(u)
            Q.remove(v)
            if _ullman_recursive(adj_u, adj_v, P, Q):
                return True
            P.append(u)
            Q.append(v)

        # No valid match found for u
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
    adj_u = nx.adjacency_matrix(g1).todense().tolist()
    adj_v = nx.adjacency_matrix(g2).todense().tolist()

    p, q = list(g1.nodes()), list(g2.nodes())
    # TODO If respecting nodel labels, then none will return true I'd assume
    if len(p) != len(q) or set(g1.nodes) != set(g2.nodes):  # if differing length or differing node labels, return false
        return False

    return _ullman_recursive(adj_u, adj_v, p, q)


if __name__ == '__main__':
    # 1. Load the graphs in the './graphs' folder
    graphs = load_all_graphs("./graphs")

    # 1.5 (You can visualize the graphs using utils.draw_all_graphs())
    draw_all_graphs(graphs, "./graphs", False)

    # 2. Perform the Ullman's subgraph isomorphic test between all pairs of graphs.
    matrix = np.zeros((len(graphs), len(graphs)), dtype=int)
    for u in range(len(graphs)):
        for v in range(len(graphs)):
            if u == v:
                matrix[u, v] = 1  # Graphs are identical
            else:
                matrix[u, v] = int(Ullman(graphs[u], graphs[v]))

    np.savetxt("./results/ullman_subgraph_isomorphism.csv", matrix, fmt="%i", delimiter=",")
