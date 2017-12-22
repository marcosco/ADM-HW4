Algorithmic Methods of Data Mining
Homework 4
Group 23: Marco Scordino, Alba Puy Tapia, Daniele Mocavini



For the first exercise we first created a function ('read_json') that return a dictionary parsing the locally saved json file.
Given its use in the continuation of the exercises we then decided to write the function ('dist') to calculate 
the weight for each arc to be able to then recall later.
The create_graph function is the basis of the first exercise: creating the graph through the networkx package we also create
authors, publications and conferences dictionaries that will be useful during the implementation of the further exercises.
Here we add vertex that refers to each author and we have associated the author's object to the graph node;
finally the connection between the authors is added as arc that represents the set of common publications if exists. The weight of the connection refers to the Jaccardi distance between the publications of the authors connected by this edge.

For the second exercise we used predominantly 3 functions: inducted_subgraph, centralities and subgraph_inducted_by_author.
The inducted_subgraph takes as argument the created graph and the id of a conference. This allows us to create and return the subgraph induced by the set of 
authors who published at that conference at least once.
The centralities, takes as parameter the newly created subgraph allowsing 
us to calculate some centralities measures (degree, closeness, betweeness). This function returns a dictionary that contains the three measures.
The subgraph_inducted_by_author allows us to find the subgraph induced by the nodes that have hop distance at most equal to d given the graph, the author and an integer. This function returns the subgraph to plot.
In these three excercises we largely used functions implmented in the networkx library.

Exercise 3 required us to write a function that returns the weight of the shortest path to Aris given an author id and a function that groups the nodes of the graph in clusters given a list of nodes that represents the center of that clusters.
The second point use an implmentation of the dijkastra distance and an utility function that compares the computed distances and group the nodes in the corresponding cluster. This function returns a dictionary that relates the nodes in the graph to the node that represent the assigned cluster.

