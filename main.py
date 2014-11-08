from generator import get_graph, get_random_seq
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_isogreedy_nodes, find_greedy_nodes, find_isocharity_nodes, find_charity_nodes, find_isolated_nodes
from augmentor import SandersFirst, SandersSecond
from copy import deepcopy

#Generate a random graph or specify it
#seq = get_random_seq(8)
seq = [[11,9], [12,10], [10,8], [8,10], [10,11], [9,10], [7,6], [6,7]]
print "Original sequence:\n", seq
G = get_graph(seq)
print "\n\nOriginal graph:\n", G
#print get_graphviz_from_graph(G)

#Find the greedy, charity, and isolated nodes
#print 'Greedy nodes:', find_greedy_nodes(G)
#print 'Charity nodes:', find_charity_nodes(G)
#print 'Isolated nodes:', find_isolated_nodes(G)
greedy_nodes = find_greedy_nodes(G)
charity_nodes = find_charity_nodes(G)
isolated_nodes = find_isolated_nodes(G)

#Find the cycles in the graph
cycles = entry_tarjan(deepcopy(G))
print "\n\nCycles:\n", cycles

#Apply cycle picking to the cycles, followed by checking the spill nodes after either min_cycles or small_cycles
#print 'Large cycles:', min_cycles(cycles[:])
#print 'Spill nodes:', find_spill_nodes(seq[:])
#print 'Small cycles:', small_cycles(cycles[:])
#print 'Spill nodes:', find_spill_nodes(seq[:])

#Use the sequence to generate graphviz syntax for visualisation purposes
#print get_graphviz(seq[:])
#print get_graphviz_names(seq[:])

#Apply Sanders's first pass algorithm
newGraph = SandersFirst(G, seq, small_cycles(cycles[:]), isolated_nodes, charity_nodes, greedy_nodes)
print "\n\nGraph after 1st pass:\n", newGraph
#print get_graphviz_from_graph(newGraph)

#Before applying Sanders's second pass algorithm, find out which nodes are not in cycles after first pass
new_cycles = sum(entry_tarjan(deepcopy(newGraph)), [])
new_nodes = list(xrange(0, len(newGraph)))
no_cycles = list(set(new_nodes) - set(new_cycles))
print "\n\nNodes not in cycles:\n", no_cycles

#Apply Sanders's second pass algorithm
newGraph2 = SandersSecond(newGraph, seq, no_cycles)
print "\n\nGraph after 2nd pass:\n", newGraph2
#print get_graphviz_from_graph(newGraph2)

#Confirm there are no more nodes which are outside of cycles
new_cycles = sum(entry_tarjan(deepcopy(newGraph2)), [])
new_nodes = list(xrange(0, len(newGraph2)))
no_cycles = list(set(new_nodes) - set(new_cycles))
print "\n\nNodes not in cycles:\n", no_cycles