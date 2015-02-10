import time
from generator import get_graph, get_random_seq, getseed
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
from augmentor import SandersFirst, SandersSecond
from copy import deepcopy

start_time = time.time()

#Generate a random graph or specify it
graph_size = 16
seq = get_random_seq(graph_size)
#print "Original sequence:\n", seq
G = get_graph(seq)

#print "Finding CGI"
CGI = find_all_types_nodes(G)
greedy_nodes = CGI[1]
charity_nodes = CGI[0]
isolated_nodes = CGI[2]
# greedy_nodes = find_greedy_nodes(G)
# charity_nodes = find_charity_nodes(G)
# isolated_nodes = find_isolated_nodes(G)

#Find the cycles in the graph
#print "Finding cycles"
cycles = entry_tarjan(deepcopy(G))
#print "\n\nCycles:\n", cycles

#Apply Sanders's first pass algorithm
#print "Augment 1"
newGraph = SandersFirst(deepcopy(G), seq, cycles[:], isolated_nodes, charity_nodes, greedy_nodes)
#print "\n\nGraph after 1st pass:\n", newGraph
#print get_graphviz_names_from_graph(newGraph, seq)
#print get_graphviz_from_graph(newGraph)

#Before applying Sanders's second pass algorithm, find out which nodes are not in cycles after first pass
#print "Finding cycles"
cycles = sum(entry_tarjan(deepcopy(newGraph)), [])
#print "\n\nNew cycles:\n", entry_tarjan(deepcopy(newGraph))
new_nodes = list(xrange(0, len(newGraph)))
no_cycles = list(set(new_nodes) - set(cycles))

#Apply Sanders's second pass algorithm
#print "Augment 2"
newGraph2 = SandersSecond(deepcopy(newGraph), seq, no_cycles)

#Confirm there are no more nodes which are outside of cycles
#print "Finding cycles"
#new_cycles = sum(entry_tarjan(deepcopy(newGraph2)), [])
#new_nodes = list(xrange(0, len(newGraph2)))
#no_cycles = list(set(new_nodes) - set(new_cycles))
#print "\n\nNodes not in cycles:\n", no_cycles

#remove = entry_tarjan(deepcopy(newGraph2))
print "\n=================Sanders================="
print "Number of nodes: ", graph_size
#print "Number of cycles: ", len(remove)
print "Dummy nodes needed:", len(newGraph2) - graph_size
#print newGraph2
cycles = entry_tarjan(deepcopy(newGraph2))
print ""
# print "Min. cycles:", min_cycles(deepcopy(cycles))
minimum_cycles = min_cycles(deepcopy(cycles))
count1 = count_dummy_nodes_necessary(deepcopy(minimum_cycles), graph_size)
count2 = count_nodes_necessary(deepcopy(minimum_cycles))
print "Total dummy nodes (min. cycles):", count1
print "Total nodes (min. cycles):", count2

outfile = "outputs/output_sanders_" + str(getseed()) + "_" + str(graph_size) + ".txt"
with open(outfile, 'w') as text_file:
	text_file.write("Unique dummy nodes: \t\t\t %s \nTotal dummy nodes: \t\t\t\t %s \nTotal nodes (min. cycles): \t\t %s \nTime: \t\t\t\t\t\t\t %s" % (str(len(newGraph2) - graph_size), count1, count2, str(time.time() - start_time)))
print ""
# smallest_cycles = small_cycles(deepcopy(cycles))
# print "Total dummy nodes (small cycles):", count_dummy_nodes_necessary(deepcopy(smallest_cycles), graph_size)
# print "Total nodes (small cycles):", count_nodes_necessary(deepcopy(smallest_cycles))
# print "Time: ", time.time() - start_time, "seconds"
print "=================END====================="
#print get_graphviz_names_from_graph(newGraph2, seq, graph_size)