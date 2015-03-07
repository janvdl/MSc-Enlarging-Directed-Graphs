import time
from generator import get_graph, get_random_seq, getseed
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
# from augmentor_cost2 import augment, SandersSecond
from augmentor import SandersFirst, SandersSecond
from copy import deepcopy

start_time = time.time()

#Generate a random graph or specify it
graph_size = 12
seq = get_random_seq(graph_size)
G = get_graph(seq)
#print get_graphviz_names_from_graph(G, seq, graph_size)
#print "\n\nOriginal graph:\n", G

#Find the cycles in the graph
#print "Finding cycles"
cycles = entry_tarjan(deepcopy(G))
#print "\n\nCycles:\n", cycles

d = dict()
r = [] #array for nodes to be removed, hence r
for cycle in cycles:
	for node in cycle:
		if node in d:
			d[node] = d[node] + 1
			if node not in r:
				r.append(node)
		else:
			d[node] = 1
#print d
#print r

#print G
for node in r:
	first = True
	for adj in G:
		if node in adj:
			if first:
				first = False
			else:
				adj.remove(node)

#Find the greedy, charity, and isolated nodes
#print "Finding CGI"
CGI = find_all_types_nodes(G)
greedy_nodes = CGI[1]
charity_nodes = CGI[0]
isolated_nodes = CGI[2]

#Apply Sanders's first pass algorithm
#print "Augment 1"
# newGraph = augment(deepcopy(G), seq, cycles[:], isolated_nodes, charity_nodes, greedy_nodes)
newGraph = SandersFirst(deepcopy(G), seq, cycles[:], isolated_nodes, charity_nodes, greedy_nodes)
#print "\n\nGraph after 1st pass:\n", newGraph
#print get_graphviz_names_from_graph(newGraph, seq)

#Before applying Sanders's second pass algorithm, find out which nodes are not in cycles after first pass
#print "Finding cycles"
cycles = sum(entry_tarjan(deepcopy(newGraph)), [])
#print "\n\nNew cycles:\n", entry_tarjan(deepcopy(newGraph))
new_nodes = list(xrange(0, len(newGraph)))
no_cycles = list(set(new_nodes) - set(cycles))
# print "\n\nNodes not in cycles:\n", no_cycles

#Apply Sanders's second pass algorithm
#print "Augment 2"
newGraph2 = SandersSecond(deepcopy(newGraph), seq, no_cycles)
#print "\n\nGraph after 2nd pass:\n", newGraph2
#print get_graphviz_names_from_graph(newGraph2, seq, graph_size)

print "\n=================Compromising Algorithm==========="
print "Number of nodes: ", graph_size
print "Time: ", time.time() - start_time, "seconds"
print "Dummy nodes needed:", len(newGraph2) - graph_size
#print newGraph2
cycles = entry_tarjan(deepcopy(newGraph2))
print ""
minimum_cycles = min_cycles(deepcopy(cycles))
print "Min. cycles:", minimum_cycles
count1 = count_dummy_nodes_necessary(deepcopy(minimum_cycles), graph_size)
count2 = count_nodes_necessary(deepcopy(minimum_cycles))
print "Total dummy nodes (min. cycles):", count1
print "Total nodes (min. cycles):", count2

outfile = "outputs/output_compromising_" + str(getseed()) + "_" + str(graph_size) + ".txt"
with open(outfile, 'w') as text_file:
	text_file.write("Unique dummy nodes: \t\t\t %s \nTotal dummy nodes: \t\t\t\t %s \nTotal nodes (min. cycles): \t\t %s \nTime: \t\t\t\t\t\t\t %s" % (str(len(newGraph2) - graph_size), count1, count2, str(time.time() - start_time)))
print ""
# print ""
# print "Small cycles:", small_cycles(deepcopy(cycles))
# smallest_cycles = small_cycles(deepcopy(cycles))
# print "Total dummy nodes (small cycles):", count_dummy_nodes_necessary(deepcopy(smallest_cycles), graph_size)
# print "Total nodes (small cycles):", count_nodes_necessary(deepcopy(smallest_cycles))
print "=================END======================"
