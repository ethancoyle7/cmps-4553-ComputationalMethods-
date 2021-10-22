
##################################################
#Name      : Ethan Coyle                         #
#Instructor: Dr. StringFellow                    #
#Class     : CMPS 4553 Computational Methods     #
#Assignment: in class assignment for 10/21/21    #
#                                                #
# in this program we are doing an in class       #
# assignment related to a graph printing out     #
# various partitions relaining to a graph and    #
# centralitys                                    #
##################################################
#Fill in the code sections below in accordance with the comments.
#Label your output


# creating out imports for program
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from random import randint

#create a little graph, use picture on the board
graph_obj = nx.Graph()
graph_obj.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8]) 
graph_obj.add_edges_from([(1,2),(3,4), (4,5), (5,8), (6,7)])


#print number of nodes in little graph
print ("Number of nodes is ", graph_obj.number_of_nodes())

#print the list of nodes and the list of edges
print ("The nodes ae :", graph_obj.nodes())
print ("The edges are :", graph_obj.edges())

#print degree of node 5 and the degrees of all nodes
print("The degree of the Node  Five is:", graph_obj.degree(5))

print("The Degrees of all the nodes are :", graph_obj.degree())

#create a dataframe called degrees to get the degrees of all the nodes
degrees = pd.DataFrame(list(graph_obj.degree()), columns = ("index_name", "degree")).set_index("index_name")
# getting error here panda not have attribute dataframe 

#sort the dataframe on it values in descending order, in place
degrees.sort_values("degree", ascending = False, inplace = True)

#print out node with highest degree
print("the node with the highest degree is: ", degrees[0:1])

#print out the neighbors of node 4, note function will return an iterator
print("Node 4 has neighbors:", graph_obj.neighbors(4))

#randomly generate more nodes, so you have n=15 nodes
n=15
for x in range(9,n+1):
  graph_obj.add_node(x)
 

#randomly try to generate 20 more edges - it won't store duplicates
for x in range(20):
  RandNum1 = randint(0, n)
  RandNum2 = randint(0, n)
  #adding edges random number 1 and 2
  graph_obj.add_edge(RandNum1, RandNum2)
  

#print the edges and their degrees
print ("The Num of  all edges are  : " , graph_obj.number_of_edges())
print ("The Degrees of the edges are", graph_obj.degree())

#print the clustering value of all the nodes
print("The clustering vals  of all nodes are are :", nx.clustering(graph_obj))

#find and print a list of the connected components in the graph
connections = list(nx.connected_components(graph_obj))
print("The clustering value of all the nodes is:", nx.clustering(graph_obj),"\n")

connections = list(nx.connected_components(graph_obj))
#then find the lengths of these connected components using list 


lengths = [len(x) for x in nx.connected_components(graph_obj)]
#print the lengths
print ("The ELngths sof the subgraohs are : ", lengths)

#compute and save to dictionaries  c1 and c2 the two different centrality measures 
c1_dict= dict(nx.degree_centrality(graph_obj))
c2_dict= dict(nx.closeness_centrality(graph_obj))

#determine node with the two highest centrality measures
max_c1_node = max(c1_dict, key=c1_dict.get)  #I got one of them here
max_c2_node = max(c2_dict, key=c2_dict.get)
print("The node with highest centrality is :", max_c1_node)
print("The node with highest closeness centrality is :", max_c2_node)

#find and print the cliques in your little graph
GraphClique = list(nx.find_cliques(graph_obj))
print("Our Cliques inside of our graphs is:\n", GraphClique)



#find any isolated nodes -  run a few times to get a graph with isolated nodes.
print("Our isolated Nodes are :", nx.isolates(graph_obj))

nx.draw(graph_obj, labels = True)
plt.show()
#print this program and your output  and draw the graph from your last run
#you can print the console, by selecting all the text and copying & pasting
#to notepad++
