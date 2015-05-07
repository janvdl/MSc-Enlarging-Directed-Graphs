import time
from generator import get_graph, get_random_seq, get_matrix
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph, get_graphviz_from_matrix
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
from augmentor_matrix import augment
from copy import deepcopy

start_time = time.time()

# def MatrixToList(G):
#     adj = [[] for x in xrange(0, len(G))]
#     for i in xrange(0, len(G[0])):
#         for j in xrange(0, len(G[0])):
#             if G[i][j] == 1:
#                 adj[i].append(j)
#     return adj

# def CompressCycle(cyc_to_compress, length):
#     for cycle in cyc_to_compress:
#         for node in cycle:
#             if node >= length:
#                 node = node * (-1)
#     print cyc_to_compress

#Generate a random graph or specify it
graph_size = 20
seq = get_random_seq(graph_size)
#seq = [[11,9],[8,11],[10,8],[9,10],[10,11],[7,10]]
G = get_matrix(seq)
#print G
#print get_graphviz_from_matrix(G, seq, graph_size)
results = augment(deepcopy(G), seq)
G_ = results[0]
newseq = results[1]
print newseq
print len(G_), len(newseq)
#print get_graphviz_from_matrix(G_, newseq, graph_size)

print "\n=================Matrix================="
print "Number of nodes: ", graph_size
print "Time: ", time.time() - start_time, "seconds"
print "Dummy nodes needed:", len(G_) - graph_size
print "All nodes necessary:", len(G_)
print "=================END====================="
