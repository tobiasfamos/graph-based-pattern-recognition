# Exercise 0
Authors: Brian Schweigler & Tobias Famos 
## Comparing naive isomorphism with ground truth


When comparing the ground truth to the naive isomorphism function implemented in Task 2, we can spot the following differences:
1. In the ground truth, any given graph is not Isomorphic to itself. I would guess this is an error in the ground truth as a graph is by definition isomorphic to himself. 
2. In the ground truth all only graphs 0 and graph 2 are isomorphic. This isomorphism is also shown in the naive test. 
3. The other false positives are due to the fact, that only the number of edges, nodes and labels are counted but not the order and connection of said attributes. Lets go through the flase positives:
    1. Graph 0 - Graph 3. They have been labeled as isomorphic as they have the same number of edges, nodes and labels. But there is a node with label 3.0 in Graph 1 which has degree 2 and in graph 3 only has degree 1. 
    2. Graph 0 - Graph 4.  They have been labeled as isomorphic as they have the same number of edges, nodes and labels. But there is a node with label 2.0 in graph 0 which has a degree of 1 and in graph 4 all nodes with label 2.0 have a degree of 2.
    3. Graph 2 - Graph 3.  They have been labeled as isomorphic as they have the same number of edges, nodes and labels. But there is a node with label 3.0 in Graph 2 which has degree 2 and in graph 3 only has degree 1. 
    4. Graph 2 - Graph 4.  They have been labeled as isomorphic as they have the same number of edges, nodes and labels. But there is a node with label 2.0 in graph 2 which has a degree of 1 and in graph 4 all nodes with label 2.0 have a degree of 2.
    5. Graph 3 - Graph 4.  They have been labeled as isomorphic as they have the same number of edges, nodes and labels. But there is a node with label 3.0 in graph 3 which has a degree of 1 and in graph 4 the node with label 3.0 has a degree of 2.