Algorithmic Methods of Data Mining
Homework 4
Group 23: Daniele Mocavini, Alba Puy Tapia, Marco Scordino



For the first exercise the following set of functions are defined:
	- 'read_json': this function returns a dictionary parsing the locally saved json file as input.
	- 'dist': this function returns the weight of the edge that connects the two nodes (authors) 
		  given as input, computed using the Jaccardi distance.
	- 'create_graph': this function not only creates the graph using the networkx package but also 
			  the authors, publications and conferences dictionaries that are required for 
			  the implementation of the following exercises.
			  Each node of the graph represents an author and if an edge exists it is due 
		          to the existance of at least one publication together, being the weight of 
			  the edge computed with the previous defined function 'dist'.

For the second exercise the following set of functions are defined:
	- 'inducted_subgraph': takes as an argument a graph and the id of a conference and returns the 
			       subgraph induced by the set of authors who published at that conference 
                               at least once.
	- 'centralities': takes as parameter a graph and return a dictionary with the computed centrali-
			  ty measures: degree, closeness and betweeness. 
	- 'subgraph_inducted_by_author': this function takes as an input a graph, an author and an inte-
					 ger and returns the subgraph induced by the nodes that have hop
                                         distance at most d with the author given. 

For the third exercise the following set of functions are defined:
	- 'tell_me_the_id': takes as an input a name an returns the identifier.
	- 'tell_me_the_name': takes as an input an identifier and returns a name.
	- 'my_dijkstra': takes as an input a graph, the node from which the algorithm starts and also,
			 can take a target in order to stop the algorithm in case the distance desired 
			 is already computed. It returns a dictionary which has as keys the nodes and as
			 values the distance between the starting node and them.
	- 'my_dijkstra_group': takes as an input a graph and a list and computes for each node of the 
			       graph the distance to the set defined by the list, returning a dictionary 
			       which has as keys the nodes and as values the group number defined as the 
			       distance to the set.
