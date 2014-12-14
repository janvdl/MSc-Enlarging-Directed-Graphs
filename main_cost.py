import time
from generator import get_graph, get_random_seq
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_isogreedy_nodes, find_greedy_nodes, find_isocharity_nodes, find_charity_nodes, find_isolated_nodes
from augmentor_cost import augment, SandersSecond
from copy import deepcopy

#for i in xrange(8, 24, 2):
start_time = time.time()

#Generate a random graph or specify it
graph_size = 24
seq = get_random_seq(graph_size)
#seq.append([5,12])
#seq = [[11,9], [12,10], [10,8], [8,10], [10,11], [9,10], [7,6], [6,7]]
#seq.append([7,5])
#seq.append([1,2])
#print "Original sequence:\n", seq
G = get_graph(seq)
#print "\n\nOriginal graph:\n", G

#Find the greedy, charity, and isolated nodes
#print "Finding CGI"
greedy_nodes = find_greedy_nodes(G)
charity_nodes = find_charity_nodes(G)
isolated_nodes = find_isolated_nodes(G)

#Find the cycles in the graph
#print "Finding cycles"
cycles = entry_tarjan(deepcopy(G))
#print "\n\nCycles:\n", cycles

#Apply Sanders's first pass algorithm
#print "Augment 1"
newGraph = augment(deepcopy(G), seq, cycles[:], isolated_nodes, charity_nodes, greedy_nodes)
#print "\n\nGraph after 1st pass:\n", newGraph
#print get_graphviz_names_from_graph(newGraph, seq)

#Before applying Sanders's second pass algorithm, find out which nodes are not in cycles after first pass
#print "Finding cycles"
cycles = sum(entry_tarjan(deepcopy(newGraph)), [])
#print "\n\nNew cycles:\n", entry_tarjan(deepcopy(newGraph))
new_nodes = list(xrange(0, len(newGraph)))
no_cycles = list(set(new_nodes) - set(cycles))
#print "\n\nNodes not in cycles:\n", no_cycles

#Apply Sanders's second pass algorithm
#print "Augment 2"
newGraph2 = SandersSecond(deepcopy(newGraph), seq, no_cycles)
#print "\n\nGraph after 2nd pass:\n", newGraph2
#print get_graphviz_names_from_graph(newGraph2, seq)

print "\n================="
print "Number of nodes: ", graph_size
print "Sanders's original: ", time.time() - start_time, "seconds"
print "Dummy nodes added:", len(newGraph2) - graph_size
print "================="
#print get_graphviz_names_from_graph(newGraph2, seq)