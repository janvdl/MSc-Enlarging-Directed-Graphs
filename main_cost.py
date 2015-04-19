import time
from generator import get_graph, get_random_seq
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
from augmentor_cost import augment, SandersSecond
from copy import deepcopy

start_time = time.time()

#Generate a random graph or specify it
graph_size = 8
seq = get_random_seq(graph_size)
G = get_graph(seq)
print get_graphviz_names_from_graph(G, seq, graph_size)

#Find the greedy, charity, and isolated nodes
CGI = find_all_types_nodes(G)
greedy_nodes = CGI[1]
charity_nodes = CGI[0]
isolated_nodes = CGI[2]

#Find the cycles in the graph
cycles = entry_tarjan(deepcopy(G))

#Apply Sanders's first pass algorithm
newGraph = augment(deepcopy(G), seq, cycles[:], isolated_nodes, charity_nodes, greedy_nodes)

#Before applying Sanders's second pass algorithm, find out which nodes are not in cycles after first pass
cycles = sum(entry_tarjan(deepcopy(newGraph)), [])
new_nodes = list(xrange(0, len(newGraph)))
no_cycles = list(set(new_nodes) - set(cycles))

#Apply Sanders's second pass algorithm
newGraph2 = SandersSecond(deepcopy(newGraph), seq, no_cycles)
print get_graphviz_names_from_graph(newGraph2, seq, graph_size)

print "\n=================Cost Optimised==========="
print "Number of nodes: ", graph_size
print "Time: ", time.time() - start_time, "seconds"
print "Dummy nodes needed:", len(newGraph2) - graph_size
cycles = entry_tarjan(deepcopy(newGraph2))
minimum_cycles = min_cycles(deepcopy(cycles))
print "Total dummy nodes (min. cycles):", count_dummy_nodes_necessary(deepcopy(minimum_cycles), graph_size)
print "Total nodes (min. cycles):", count_nodes_necessary(deepcopy(minimum_cycles))
print ""
smallest_cycles = small_cycles(deepcopy(cycles))
print "Total dummy nodes (small cycles):", count_dummy_nodes_necessary(deepcopy(smallest_cycles), graph_size)
print "Total nodes (small cycles):", count_nodes_necessary(deepcopy(smallest_cycles))
print "=================END======================"
