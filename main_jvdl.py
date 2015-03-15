import time
from generator import get_graph, get_random_seq, getseed
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
from augmentor_jvdl import augment
from copy import deepcopy
from lcs import find_repeated_nodes, remove_repeated_nodes

#for i in xrange(8, 10, 2):
start_time = time.time()

#Generate a random graph or specify it
graph_size = 8
seq = get_random_seq(graph_size)
#seq = [[11,9], [12,10], [10,8], [8,10], [10,11], [9,10], [7,6], [6,7], [7,5]]
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
minimum_cycles = min_cycles(deepcopy(cycles))
smallest_cycles = small_cycles(deepcopy(cycles))
print "Min. cycles:", minimum_cycles
# print "Small cycles:", smallest_cycles
count1 = count_dummy_nodes_necessary(deepcopy(minimum_cycles), graph_size)
count2 = count_nodes_necessary(deepcopy(minimum_cycles))
print "Total dummy nodes (min. cycles):", count1
print "Total nodes (min. cycles):", count2
# count3 = count_dummy_nodes_necessary(deepcopy(smallest_cycles), graph_size)
# count4 = count_nodes_necessary(deepcopy(smallest_cycles))
# print "Total dummy nodes (small. cycles):", count3
# print "Total nodes (small. cycles):", count4

print "Repeated nodes:", find_repeated_nodes(minimum_cycles)
rem_rep = remove_repeated_nodes(deepcopy(minimum_cycles), find_repeated_nodes(minimum_cycles))
count1 = count_dummy_nodes_necessary(deepcopy(rem_rep), graph_size)
count2 = count_nodes_necessary(deepcopy(rem_rep))
print "Total nodes compressed (min. cycles):", count2
# print remove_repeated_nodes

outfile = "outputs/output_jvdl_" + str(getseed()) + "_" + str(graph_size) + ".txt"
with open(outfile, 'w') as text_file:
	text_file.write("Unique dummy nodes: \t\t\t %s \nTotal dummy nodes: \t\t\t\t %s \nTotal nodes (min. cycles): \t\t %s \nTime: \t\t\t\t\t\t\t %s" % (str(len(G) - graph_size), count1, count2, str(time.time() - start_time)))
print ""
# print "Small cycles:", small_cycles(deepcopy(cycles))
#smallest_cycles = small_cycles(deepcopy(cycles))
#print "Total dummy nodes (small cycles):", count_dummy_nodes_necessary(deepcopy(smallest_cycles), graph_size)
#print "Total nodes (small cycles):", count_nodes_necessary(deepcopy(smallest_cycles))
print "=================END=================="

# cycles = (entry_tarjan(deepcopy(G)))
# print min_cycles(cycles)
# print small_cycles(cycles)
# print count_dummy_nodes_necessary(min_cycles(cycles), graph_size)
# print count_dummy_nodes_necessary(small_cycles(cycles), graph_size)
# print count_nodes_necessary(min_cycles(cycles))
# print count_nodes_necessary(small_cycles(cycles))
# print get_graphviz_names_from_graph(G, seq, graph_size)