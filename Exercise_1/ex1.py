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


class Mapping_Node:
    def __init__(self, node_1, node_2):
        self.node_1 = node_1
        self.node_2 = node_2
        self.next_nodes = []
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.next_nodes.append(child)
        child.set_parent(self)

    def get_unused_nodes(self, g1: nx.Graph, g2: nx.Graph):
        nodes_g1 = list(g1.nodes())
        nodes_g2 = list(g2.nodes())
        current = self
        while (current.node_1):
            nodes_g1.remove(current.node_1)
            nodes_g2.remove(current.node_2)
            current = current.parent
        return nodes_g1, nodes_g2

    def has_same_structure(self, to, g1: nx.Graph, g2: nx.Graph):
        return g1.has_edge(self.node_1, to.node_1) == g2.has_edge(self.node_2, to.node_2)

    def is_possible_mapping(self, g1, g2):
        current = self
        while (current and current.node_1):
            if (not self.has_same_structure(current, g1, g2)):
                return False
            current = current.parent
        return True

        # Backtrack to the root:
        # Compare the node g2 and g1 in relation to all the mapped nodes
        # if mapping_node.g1 has an edge to parent.g1 then mappping_node.g2 must have an edge to parent.g2


def construct_a_level(parent_mapping, node_g1, unuse_nodes_g2, g1, g2):
    for current_node_g2 in unuse_nodes_g2:
        current_mapping_node = Mapping_Node(node_g1, current_node_g2)
        current_mapping_node.set_parent(parent_mapping)
        if (current_mapping_node.is_possible_mapping(g1, g2)):
            parent_mapping.add_child(current_mapping_node)


def is_isomorphic_brute_force(g1: nx.Graph, g2: nx.Graph):
    # Build Root
    root_node = Mapping_Node(None, None)
    nodes_g1 = list(g1.nodes())
    nodes_g2 = list(g2.nodes())
    # Construct first level
    construct_a_level(root_node, nodes_g1[0], nodes_g2, g1, g2)
    can_be_reached = build_tree_recursive_has_leaf_been_reached(root_node, g1, g2)
    return can_be_reached


def build_tree_recursive_has_leaf_been_reached(current_mapping_node, g1, g2):
    can_be_reached = False
    for child in current_mapping_node.next_nodes:
        unused_nodes_g1, unused_nodes_g2 = child.get_unused_nodes(g1, g2)
        if (len(unused_nodes_g1)):
            construct_a_level(child, unused_nodes_g1[0], unused_nodes_g2, g1, g2)
            can_be_reached = build_tree_recursive_has_leaf_been_reached(child, g1, g2)
        else:
            can_be_reached = True
        if(can_be_reached):
            break
    return can_be_reached
            
def build_future_match_table(g1: nx.Graph, g2:nx.Graph):
    nodes_g1 = list(g1.nodes())
    nodes_g2 = list(g2.nodes())
    future_match_table = [ [0]*len(nodes_g2) for i in range(len(nodes_g1))]
    for index_1 in range(0, len(nodes_g1)):
        for index_2 in range(0, len(nodes_g1)):
            if g1.degree(nodes_g1[index_1]) <= g2.degree(nodes_g2[index_2]):
                future_match_table[index_1][index_2] = 1
    return future_match_table

def Ullman(g1: nx.Graph, g2: nx.Graph) -> bool:
    """
    Perform the subgraph isomorphism test between g1 and g2

    Args:
        g1: A networkx graph object
        g2: A networkx graph object

    Returns:
        True if g1 is a subgraph of g2 and False otherwise
    """
    """ 
    // Step 1: Multiset-label determination
2: Mi(v)={li−1(u) | u∈N(v)}foreachnodevinV andV′
3: Sort elements in Mi(v) and concatenate them into a string si(v).
4: si(v) = li−1(v) + si(v) // concatenate li−1(v) as prefix
5: // Step 2: Label compression and elabeling
6: Sort all strings si(v) for all nodes v in V and V ′
7: Map each string si(v) to f(si(v)), such that f(si(v)) = f(si(w)) if and only if
si(v) = si(w)
8: Set li(v) := f(si(v)) for all nodes v in V and V ′
 """
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
                matrix[u, v] = int(is_isomorphic_brute_force(graphs[u], graphs[v]))  # Graphs are identical
            else:
                matrix[u, v] = int(is_isomorphic_brute_force(graphs[u], graphs[v]))

    np.savetxt("./results/ullman_subgraph_isomorphism.csv",
               matrix, fmt="%i", delimiter=",")
