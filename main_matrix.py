import time
from generator import get_graph, get_random_seq, get_matrix
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph, get_graphviz_from_matrix
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
from augmentor_matrix import augment
from copy import deepcopy

start_time = time.time()

#Generate a random graph or specify it
graph_size = 8
seq = get_random_seq(graph_size)
G = get_matrix(seq)
#print G
G_ = augment(deepcopy(G))
#print G_
#print get_graphviz_from_matrix(G_)

print "\n=================Matrix================="
print "Number of nodes: ", graph_size
#print "Number of cycles: ", len(remove)
print "Time: ", time.time() - start_time, "seconds"
print "Dummy nodes needed:", len(G_) - graph_size
print "All nodes necessary:", len(G_)
print "=================END====================="