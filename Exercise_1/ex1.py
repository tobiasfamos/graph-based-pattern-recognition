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
import copy

from utils import load_all_graphs, draw_all_graphs


def _ullman_recursive():
    pass


class Mapping_Node:
    def __init__(self, node_1, node_2, graphs):
        self.node_1 = node_1
        self.node_2 = node_2
        self.next_nodes = []
        self.graphs = graphs
        self.parent = None

    @staticmethod
    def build_root_node(graphs):
        root_node = Mapping_Node(None, None, graphs)
        future_match_table = build_future_match_table(graphs)
        root_node.set_future_match_table(future_match_table)
        return root_node

    def set_parent(self, parent):
        self.parent = parent
    
    def set_future_match_table(self, future_match_table):
        self.future_match_table = future_match_table

    def add_child(self, child):
        self.next_nodes.append(child)
        child.set_parent(self)

    def might_be_possible_mapping(self, node_g1, node_g2):
        """
        Returns true if the mapping is allowed acccording to the future match table 
        """
        nodes_g1 = list(self.graphs[1].nodes())
        nodes_g2 = list(self.graphs[2].nodes())
        index_1 = nodes_g1.index(node_g1)
        index_2 = nodes_g2.index(node_g2)
        return bool(self.future_match_table[index_1][index_2])


    def get_nodes_for_next_level(self):
        """ Takes the two graphs, and the future match table. It determines any unused nodes that are still
         possible based on the future match table. """
        nodes_g1 = list(self.graphs[1].nodes())
        nodes_g2 = list(self.graphs[2].nodes())
        current = self
        while (current.node_1):
            nodes_g1.remove(current.node_1)
            nodes_g2.remove(current.node_2)
            current = current.parent
        if (len(nodes_g1)):
            node_g1 = nodes_g1[0]
            for node in nodes_g2:
                if (not self.might_be_possible_mapping(node_g1, node)):
                    nodes_g2.remove(node)
            return node_g1, nodes_g2
        else:
            return None, None

    def update_future_match_table(self) -> bool:
        self.set_future_match_table(copy.deepcopy(self.parent.future_match_table))
        # Set all nodes in in row to and column of this mapping to 0
        nodes_g1 = list(self.graphs[1].nodes())
        nodes_g2 = list(self.graphs[2].nodes())
        index_g2 = nodes_g2.index(self.node_2)
        self.future_match_table[nodes_g1.index(self.node_1)] = [0]*len(nodes_g2)
        for row in self.future_match_table:
            row[index_g2] = 0
        self.future_match_table[nodes_g1.index(self.node_1)][index_g2] = 1
        
        # Remove all violating edge constraints
            # Iterate over all 1s in table
                # If n1 is neighbour of 1 then n2 must be neighbour of a (and with not neightbour)
        for i1 in range(len(self.future_match_table)):
            for i2 in range(len(self.future_match_table[i1])):
                if(self.future_match_table[i1][i2]):
                    #TODO make method violates edge constraint
                    if(not self.graphs[1].has_edge(self.node_1, nodes_g1[i1]) == self.graphs[2].has_edge(self.node_2, nodes_g2[i2])):
                        self.future_match_table[i1][i2] = 0
        # Look for 0 rows
        for row in self.future_match_table:
            if row == [0]*len(row):
                return False
        return True


def construct_a_level(parent_mapping, node_g1, unuse_nodes_g2):
    for current_node_g2 in unuse_nodes_g2:
        current_mapping_node = Mapping_Node(node_g1, current_node_g2, parent_mapping.graphs)
        # TODO set parent mapping in constructor
        current_mapping_node.set_parent(parent_mapping)
        is_possible = current_mapping_node.update_future_match_table()
        if not is_possible:
            continue
        parent_mapping.add_child(current_mapping_node)    


def build_tree_recursive_has_leaf_been_reached(current_mapping_node, graphs):
    can_be_reached = False
    for child in current_mapping_node.next_nodes:
        next_node_g1, unused_nodes_g2 = child.get_nodes_for_next_level()
        if (next_node_g1):
            construct_a_level(child, next_node_g1, unused_nodes_g2)
            can_be_reached = build_tree_recursive_has_leaf_been_reached(
                child, graphs)
        else:
            can_be_reached = True
        if (can_be_reached):
            break
    return can_be_reached


def build_future_match_table(graphs: dict):
    nodes_g1 = list(graphs[1].nodes())
    nodes_g2 = list(graphs[2].nodes())
    future_match_table = [[0]*len(nodes_g2) for i in range(len(nodes_g1))]
    for index_1 in range(0, len(nodes_g1)):
        for index_2 in range(0, len(nodes_g2)):
            if graphs[1].degree(nodes_g1[index_1]) <= graphs[2].degree(nodes_g2[index_2]):
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
    # Build Root
    graphs = {1: g1, 2: g2}
    root_node = Mapping_Node.build_root_node(graphs)
    nodes_g1 = list(graphs[1].nodes())
    nodes_g2 = list(graphs[2].nodes())
    # Construct first level
    construct_a_level(root_node, nodes_g1[0], nodes_g2)
    can_be_reached = build_tree_recursive_has_leaf_been_reached(root_node, graphs)
    return can_be_reached


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
                matrix[u, v] = int(Ullman(
                    graphs[u], graphs[v]))  # Graphs are identical
            else:
                matrix[u, v] = int(
                    Ullman(graphs[u], graphs[v]))

    np.savetxt("./results/ullman_subgraph_isomorphism.csv",
               matrix, fmt="%i", delimiter=",")
