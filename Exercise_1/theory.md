Name: Tobias Famos  
Matriculation Number: 16-933-764

Name: Brian Schweigler  
Matriculation Number: 16-102-071


### 1. Summarize the advantages and drawbacks of graph based pattern representation when compared with vectorial approaches.

Generally, graphsare  able to describe relationships among different parts of underlying data.
Usually the number of nodes and edges are not limited a priori.

Advantages and Disadvantages in table form for easier comparison:

| Graph-Based Pattern Recognition 	                                                  | Vector Based Pattern Recognition  	                      |
|------------------------------------------------------------------------------------|----------------------------------------------------------|
| High representational power <br/>(can represent semantical relationships better) 	 | Low representational power 	                             |
| Low Efficiency	                                                                    | High efficiency	                                         |
| Includes the structural information of data	                                       | Scale better	                                            |
| Difficulty of scalability	                                                         | Scale better                                             |
| Can handle data sparsity                                                           | Can not handle data sparsity well                        |
| Difficult to capture global context <br/>(overall meaning of entities)             | Can capture global context <br/> e.g. sentiment analysis |


### 2. Regard the following fours graphs and decide for each of them which special graph type it represents the best.

If we look at the graphs as

| A	  | B	  |
|-----|-----|
| 	 C | 	 D |

A is weighted graph, as each edge has a weight associated with it.

B is a tree, as every node has at most one parent and at least 1 or more children.

C is a graph with unique nodel labels. 

D is simply an ordered (directed) graph.

### 3. (a) Suppose N(n, k) is the number of non-isomorphic graphs with n nodes and k edges. Find N(4, 3).

N(4, 3) = 2, as only two non-isomorphic graphs with 4 nodes and 3 edges exist:

 ![](\figs\ex_3a.PNG)

The others are isomorphic to one of the two above.

### 3. (b) Define and sketch the set of distinct (i.e., non-isomorphic) unlabeled graphs of size 4. Additionally, find the total number of nonisomorphic graphs of size 4. 

The size of a graph is the number of nodes, according to the lecture.

![](\figs\ex_3b.PNG)

(Might have missed one or two, but I think this is all of them)

It should be 11 in total.

### 4. Determine whether the three unlabeled graphs g1, g2 and g3 given in the figure above are isomorphic. Formally, for any isomorphic graph pair gi, gj explicitly determine the isomorphism f : Vi → Vj .

At a glance, it seems that all nodes of these graphs have the same degree.

v1 neighbors: v2, v5, v5  
w1 neighbors: w2, w3, w4  
x1 neighbors: x4, x5, x6

v2 neighbors: v1, v6, v3  
w2 neighbors: w1, w3, w5  
x2 neighbors: x4, x5, x6

v3 neighbors: v2, v4, v5  
w3 neighbors: w1, w2, w6  
x3 neighbors: x4, x5, x6

v4 neighbors: v1, v3, v5  
w4 neighbors: w1, w5, w6  
x4 neighbors: x1, x2, x3

v5 neighbors: v1, v3, v6  
w5 neighbors: w2, w4, w6  
x5 neighbors: x1, x2, x3

v6 neighbors: v2, v4, v5  
w6 neighbors: w3, w4, w5  
x6 neighbors: x1, x2, x3


* f(v1) = w1  
* f(v2) = w3
* f(v4) = w4
* f(v5) = w4
* f(v6) = w6
* f(v3) = w2  
##### -> g1 and g2 are ismorphic.

##### For g3 this is not the case, as it is a bipartite graph.  
Going by the explicit ismorphism, we can already see that it will not work.  
If f(v1) -> x1, then f(v2) -> x4, f(v4) -> x6, and f(v5) -> x5.    
f(v3) -> x3.  
f(v6) -> x6.

Neighbors of v2 are v4, v5, v6  .
The neighbors of f(v2)=x4 are x1, x2, x3.  
x1 does not correspond to v4, v5 or v6, so the isomorphism is not correct.

### 5. Compute the association graph on the following two labeled graphs and find the maximum clique in it (different shades of gray represent different node labels).

![](\figs\ex_5.PNG)

Maximum clique given our representation is  
[(1, 1'), (2, 2'), (3, 3'), (4, 4')]

### 6. For each paper briefly describe how the underlying patterns/objects are actually represented as a graph g = (V,E, μ, ν). In particular, elaborate on the semantic of both nodes and edges as well as the corresponding labeling functions.

* Malware classification:
  * Here they have the concept of Call Graph, "a directed graph G with vertex set V=V(G), representing the functions, and edge set E=E(G), where E(G) ⊆ V(G)×V(G), in correspondence with the function calls."
    * So nodes are the functions
    * Edges are directed and show what functions call what other functions.
    * The node labels are simply the function names, while edges are not labeled.
* Fingerprint Classification
  * Here they use planar graphs which are then matched to each other and have a corresponding graph edit distance.
    * Each pixel in a window as a graph node without attributes
    * Edge generated in two, out of eight, possible directions that best match the vector orthogonal to the average window gradient.
    * "Simple edit cost function that assigns constant costs pn to node insertions and deletions, and constant costs pe to edge insertions and deletions"
    * NMote that nodes are unlabeled!