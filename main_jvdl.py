import time
from generator import get_graph, get_random_seq
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
from augmentor_jvdl import augment
from copy import deepcopy

#for i in xrange(8, 10, 2):
start_time = time.time()

#Generate a random graph or specify it
graph_size = 18
seq = get_random_seq(graph_size)
#seq.append([5,12])
#seq = [[11,9], [12,10], [10,8], [8,10], [10,11], [9,10], [7,6], [6,7]]
#seq.append([7,5])
#seq.append([1,2])
#print "Original sequence:\n", seq
G = get_graph(seq)
#print "\n\nOriginal graph:\n", G
#print get_graphviz_names_from_graph(G, seq, graph_size)

#Find the greedy, charity, and isolated nodes
#print "Finding CGI"
#    greedy_nodes = find_greedy_nodes(G)
#    charity_nodes = find_charity_nodes(G)
#    isolated_nodes = find_isolated_nodes(G)

#Find the cycles in the graph
#print "Finding Cycles"
cycles = entry_tarjan(deepcopy(G))
#print "\n\nCycles:\n", cycles

#print "Augmenting 1"
augment(G, seq, cycles)
#print "Final graph:", G
#print get_graphviz_names_from_graph(G, seq, graph_size)

print "\n=================JvdL================="
print "Number of nodes: ", graph_size
print "Time: ", time.time() - start_time, "seconds"
print "Unique dummy nodes:", len(G) - graph_size
#print newGraph2
cycles = entry_tarjan(deepcopy(G))
print ""
# print "Min. cycles:", min_cycles(deepcopy(cycles))
minimum_cycles = min_cycles(deepcopy(cycles))
print "Total dummy nodes (min. cycles):", count_dummy_nodes_necessary(deepcopy(minimum_cycles), graph_size)
print "Total nodes (min. cycles):", count_nodes_necessary(deepcopy(minimum_cycles))
print ""
# print "Small cycles:", small_cycles(deepcopy(cycles))
smallest_cycles = small_cycles(deepcopy(cycles))
print "Total dummy nodes (small cycles):", count_dummy_nodes_necessary(deepcopy(smallest_cycles), graph_size)
print "Total nodes (small cycles):", count_nodes_necessary(deepcopy(smallest_cycles))
print "=================END=================="

# cycles = (entry_tarjan(deepcopy(G)))
# print min_cycles(cycles)
# print small_cycles(cycles)
# print count_dummy_nodes_necessary(min_cycles(cycles), graph_size)
# print count_dummy_nodes_necessary(small_cycles(cycles), graph_size)
# print count_nodes_necessary(min_cycles(cycles))
# print count_nodes_necessary(small_cycles(cycles))