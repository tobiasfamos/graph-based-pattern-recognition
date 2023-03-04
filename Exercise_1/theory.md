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

D is simply a directed graph.

### 3. (a) Suppose N(n, k) is the number of non-isomorphic graphs with n nodes and k edges. Find N(4, 3).

N(4, 3) = 2, as only two non-isomorphic graphs with 4 nodes and 3 edges exist:

 ![](\figs\ex_3a.PNG)

The others are isomorphic to one of the two above.

### 3. (b) Define and sketch the set of distinct (i.e., non-isomorphic) unlabeled graphs of size 4. Additionally, find the total number of nonisomorphic graphs of size 4. 

The size of a graph is the number of nodes, according to the lecture.

![](\figs\ex_3b.PNG)

(Might have missed one or two, but I think this is all of them)

It should be 11 in total.