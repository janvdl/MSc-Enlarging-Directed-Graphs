import time
from generator import get_graph, get_random_seq, getseed
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
# from augmentor_cost2 import augment, SandersSecond
from augmentor import SandersFirst, SandersSecond
from copy import deepcopy
from rcomb import built_in_rcombs

# ======================================
def ContainsOnlySingleNodes(cycles):
	d = dict()
	for cycle in cycles:
		for node in cycle:
			if node in d:
				d[node] = d[node] + 1
				return False
			else:
				d[node] = 1

	return True
# =======================================

start_time = time.time()

#Generate a random graph or specify it
graph_size = 14
seq = get_random_seq(graph_size)
G = get_graph(seq)
#print get_graphviz_names_from_graph(G, seq, graph_size)
#print "\n\nOriginal graph:\n", G

#Find the cycles in the graph
cycles = entry_tarjan(deepcopy(G))
#print cycles
SingleNodeCycles = []
for i in xrange(1, len(cycles)):
	comb_cycles = built_in_rcombs(cycles, i)
	for cycles in comb_cycles:
		if ContainsOnlySingleNodes(cycles):
			SingleNodeCycles.append(cycles)
print sorted(SingleNodeCycles, key=len)

#Find the greedy, charity, and isolated nodes
#print "Finding CGI"
# CGI = find_all_types_nodes(G)
# greedy_nodes = CGI[1]
# charity_nodes = CGI[0]
# isolated_nodes = CGI[2]

# newGraph = SandersFirst(deepcopy(G), seq, cycles[:], isolated_nodes, charity_nodes, greedy_nodes)
# cycles = sum(entry_tarjan(deepcopy(newGraph)), [])
# new_nodes = list(xrange(0, len(newGraph)))
# no_cycles = list(set(new_nodes) - set(cycles))

# newGraph2 = SandersSecond(deepcopy(newGraph), seq, no_cycles)

# print "\n=================Compromising Algorithm==========="
# print "Number of nodes: ", graph_size
# print "Time: ", time.time() - start_time, "seconds"
# print "Dummy nodes needed:", len(newGraph2) - graph_size
# cycles = entry_tarjan(deepcopy(newGraph2))
# print ""
# minimum_cycles = min_cycles(deepcopy(cycles))
# print "Min. cycles:", minimum_cycles
# count1 = count_dummy_nodes_necessary(deepcopy(minimum_cycles), graph_size)
# count2 = count_nodes_necessary(deepcopy(minimum_cycles))
# print "Total dummy nodes (min. cycles):", count1
# print "Total nodes (min. cycles):", count2

# outfile = "outputs/output_compromising_" + str(getseed()) + "_" + str(graph_size) + ".txt"
# with open(outfile, 'w') as text_file:
# 	text_file.write("Unique dummy nodes: \t\t\t %s \nTotal dummy nodes: \t\t\t\t %s \nTotal nodes (min. cycles): \t\t %s \nTime: \t\t\t\t\t\t\t %s" % (str(len(newGraph2) - graph_size), count1, count2, str(time.time() - start_time)))
# print ""
# print "=================END======================"