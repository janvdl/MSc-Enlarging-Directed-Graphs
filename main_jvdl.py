from generator import get_graph, get_random_seq
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_isogreedy_nodes, find_greedy_nodes, find_isocharity_nodes, find_charity_nodes, find_isolated_nodes
from augmentor_jvdl import augment
from copy import deepcopy

#Generate a random graph or specify it
#seq = get_random_seq(8)
#seq.append([5,12])
seq = [[11,9], [12,10], [10,8], [8,10], [10,11], [9,10], [7,6], [6,7]]
seq.append([7,5])
seq.append([1,2])
#print "Original sequence:\n", seq
G = get_graph(seq)
print "\n\nOriginal graph:\n", G
print get_graphviz_names_from_graph(G, seq)

#Find the greedy, charity, and isolated nodes
greedy_nodes = find_greedy_nodes(G)
charity_nodes = find_charity_nodes(G)
isolated_nodes = find_isolated_nodes(G)

#Find the cycles in the graph
cycles = entry_tarjan(deepcopy(G))
#print "\n\nCycles:\n", cycles

augment(G, seq)
print "Final graph:", G
print get_graphviz_names_from_graph(G, seq)
    
cycles = sum(entry_tarjan(deepcopy(G)), [])
nodes = list(xrange(0, len(G)))
no_cycles = list(set(nodes) - set(cycles))
print "Nodes not in cycles:", no_cycles