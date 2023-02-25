from typing import Callable, List

import networkx as nx
from matplotlib import pyplot as plt


###############
#  CONSTANTS  #
###############

COLOR_MAP = {
    1.: '#648FFF',
    2.: '#785EF0',
    3.: '#DC267F',
    4.: '#FE6100',
    5.: '#FFB000',
    6.: '#004D40',
    7.: '#420E00'
}

NODE_LABEL = 'x'


###############
#   UTILS     #
###############

def get_node_colors(graph: nx.Graph):
    node_colors = []
    id_to_x_map = graph.nodes(data="x")
    for node in graph:
        x_value = id_to_x_map[node]
        node_colors.append(COLOR_MAP[x_value])
    return node_colors

def load_graph(filename: str) -> nx.Graph:
    """
    Load the **file.graphml** as a **nx.Graph**.

    Args:
        filename:

    Returns:
        The loaded NetworkX graph
    """
    graph = nx.read_graphml(filename)
    return graph


def draw_graph(graph: nx.Graph,
               filename: str,
               labels: dict = None,
               node_color: List[str] = None,
               layout: Callable[[nx.Graph], dict] = None) -> None:
    """
    This function draws a given networkx graph object, saves the drawing to a specified file 

    Args:
        graph: A networkx graph object.
        filename: A string representing the path and filename
                  where the graph will be saved as an image.
        labels: A dictionary that maps node indices to labels.
        node_color: A list of strings representing the color of each node in the graph.
        layout: A layout function that takes a graph as input and returns a dictionary of node positions
                If None, the **nx.kamada_kawai_layout** layout will be used.
    """
    if layout == None:
        layout = nx.layout.bipartite_layout
    positions = layout(graph)
    nx.draw(graph, labels=labels, with_labels = True, node_color=node_color, pos=positions)
    plt.savefig(filename)
    plt.clf()

def compare_graphs_naive(graph_1: nx.Graph, graph_2: nx.Graph)-> bool:
    same_node_count = len(graph_1.nodes()) == len(graph_2.nodes())
    same_edge_count = len(graph_1.edges()) == len(graph_1.edges())

    labels_1 = dict(graph_1.nodes(data="x"))
    labels_2 = dict(graph_2.nodes(data="x"))
    

    number_values_1 = set(labels_1.values())
    number_values_2 = set(labels_2.values())

    same_labels = number_values_1 == number_values_2

    return same_node_count and same_edge_count and same_labels



