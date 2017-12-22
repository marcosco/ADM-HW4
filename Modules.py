
# coding: utf-8

# # Algorithmic Methods of Data Mining
# ## Homework 4
# ### Group 23: Daniele Mocavini, Alba Puy Tapia,  Marco Scordino

import itertools
import json
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

dictionary={}
authors_dict = {}
publications_dict = {}
conferences_dict = {}

def read_json(filename):
    """Returns a dictionary from the provided filename.
    Inputs:
    @filename: The name of the file
    """
    try:
        with open(filename) as data_file:
            new_dict = json.load(data_file)
    except:
        return read_json(input("So sorry. No file found. Try again."))
    return new_dict


# Let's define the function dist:
def dist(a1,a2):
    global authors_dict
    a1_pubs = authors_dict[a1]["publications"]
    a2_pubs = authors_dict[a2]["publications"]
    w = 1 - (len(set(a1_pubs) & set(a2_pubs))/len(set(a1_pubs) | set(a2_pubs)))
    return(w, a1_pubs, a2_pubs)

def create_graph(source):
    global authors_dict 
    global publications_dict
    global conferences_dict
    publications = read_json(source)
    G = nx.Graph(name='Data Scientist Network')
    # Make a dictionary for author, publications and conferences
    for publication in publications:
        try:
            pub = publications_dict[int(publication["id_publication_int"])]
        except KeyError:
            publications_dict[int(publication["id_publication_int"])] = []
            pub = publications_dict[int(publication["id_publication_int"])]
        try:
            conf = conferences_dict[int(publication["id_conference_int"])]
        except KeyError:
            conferences_dict[int(publication["id_conference_int"])] = {"Authors": [], "Pubblications": []}
            conf = conferences_dict[int(publication["id_conference_int"])]
        for author in publication["authors"]:
            try:
                author_ = authors_dict[int(author["author_id"])]
            except KeyError:
                authors_dict[int(author["author_id"])] = { "author": author["author"], "publications": [], "conferences": []}
                # For each author we add a vertex to the graph
                author_ = authors_dict[int(author["author_id"])]
            finally:
                author_["id"] = int(author["author_id"])
                author_["publications"].append(int(publication["id_publication_int"]))
                author_["conferences"].append(int(publication["id_conference_int"]))
                conf["Authors"].append(int(author["author_id"]))
                conf["Pubblications"].append(int(publication["id_publication_int"]))
                # Associate the author's object to the graph node
                G.add_node(int(author["author_id"]), author=author_)
                pub.append(int(author_["id"]))
    # Make a new dictionary for conference
    lista=[]
    for i in conferences_dict.values():
        lista.append(i['Authors'])
    id_conference=[]
    for i in conferences_dict:
        id_conference.append(i)
    global dictionary
    dictionary = dict(zip(id_conference, lista))
    # for each publication create the connection between the authors
    for pub, authors in publications_dict.items():
        if len(authors) > 1:
            edges = list(itertools.combinations(authors, 2))
            for edge in edges:
                a1 = edge[0]
                a2 = edge[1]
                w, a1_pubs, a2_pubs = dist(a1,a2)
                G.add_edge(a1, a2, weight=w, publications=list(set(a1_pubs) & set(a2_pubs)))
    return(G)

# Take a conference id and return the subgraph induced by the set of authors who
# published at the input conference at least once
def inducted_subgraph(G,conference_id):
    global dictionary
    return G.subgraph(dictionary[conference_id])
    
def centralities(subgraph):
    degree=nx.degree(subgraph)
    closeness=nx.closeness_centrality(subgraph)
    betweeness=nx.betweenness_centrality(subgraph)
    return {"degree":degree, "closeness": closeness, "betweeness":betweeness}

# Take an author id and an integer d
def subgraph_inducted_by_author(G,author,d):
    return nx.ego_graph(G, author, radius=d, center=True, undirected=False, distance=None)
    
# Shortest path algorithm: DIJKSTRA'S   
# Finding the identifier of the author
def tell_me_the_id(s):
    global authors_dict
    for i in authors_dict.keys():
        if authors_dict[i]["author"]== s:
            return(i) 
        
def tell_me_the_name(idd):
    global authors_dict
    return(authors_dict[idd]["author"])

   
def my_dijkstra(G, source, target=None):
    dist = {}
    prev = {}
    # Initialization
    for v in G.nodes():
        dist[v] = np.inf
        prev[v] = None
        
    dist[source] = 0
    # All nodes are initialy set as Unvisited
    Q = G.nodes()
    # Repeat until all nodes are visited
    while Q:
        # Create a dictionary of the neighbours
        d = G[source]
        minWeight = np.inf
        u = None
        # Select the neighbour with the minimum distance
        for k,v in d.items():
            if k in Q and v["weight"] < minWeight:
                minWeight = v["weight"]
                u = k
        # If a neighbour is selected
        if u:
            # then set it as visited 
            Q.remove(u)
            dist[u] = minWeight
            # If a target is specified and
            if u == target:
                # reached then exit
                S = []
                while prev[u]:
                    S = [u] + S
                    u = prev[u]
                S = [u] + S
                dist = dist[target]
                break
            # While in U the shortest path to v is selected
            for v in G.neighbors(u):
                alt = dist[u] + G.get_edge_data(u,v)["weight"]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        else:
            break
    return dist

def my_dijkstra_group(G,l):
    global authors_dict
    GroupNumber = {}
    GroupDist = {}
    for k in authors_dict.keys():
        GroupNumber[k] = None
        GroupDist[k] = np.inf
    # For every node in the cluster list    
    for i in l:
        print("Computing the distance between ", authors_dict[i]["author"], " and all the other authors... ")
        # The distance to each node in the graph is computed
        sol = my_dijkstra(G,i)
        for v, w in sol.items():
            # And the node is assigned to the closest
            if w < GroupDist[v]:
                # one in the given list
                GroupNumber[v] = (i,sol[v])
                GroupDist[v] = w
    return(GroupNumber)