import time
from generator import get_graph, get_random_seq, getseed
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph, get_cycle_latex
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
from augmentor import SandersFirst, SandersSecond
from copy import deepcopy

for i in xrange(8, 20, 2):
	start_time = time.time()

	#Generate a random graph or specify it
	graph_size = i
	seq = get_random_seq(graph_size)
	#seq = [[11,9],[8,11],[10,8],[9,10],[10,11],[7,10]]
	G = get_graph(seq)
	#print get_graphviz_names_from_graph(G, seq, graph_size)

	#print "Finding CGI"
	CGI = find_all_types_nodes(G)
	greedy_nodes = CGI[1]
	charity_nodes = CGI[0]
	isolated_nodes = CGI[2]

	cycles = entry_tarjan(deepcopy(G))
	#print get_cycle_latex(deepcopy(cycles))

	#Apply Sanders's first pass algorithm
	newGraph = SandersFirst(deepcopy(G), seq, cycles[:], isolated_nodes, charity_nodes, greedy_nodes)

	#Before applying Sanders's second pass algorithm, find out which nodes are not in cycles after first pass
	cycles = sum(entry_tarjan(deepcopy(newGraph)), [])
	new_nodes = list(xrange(0, len(newGraph)))
	no_cycles = list(set(new_nodes) - set(cycles))

	#Apply Sanders's second pass algorithm
	newGraph2 = SandersSecond(deepcopy(newGraph), seq, no_cycles)
	#print get_graphviz_names_from_graph(G, seq, graph_size)

	print "\n=================Sanders================="
	print "Number of nodes: ", graph_size
	print "Dummy nodes needed:", len(newGraph2) - graph_size
	cycles = entry_tarjan(deepcopy(newGraph2))
	print ""
	minimum_cycles = min_cycles(deepcopy(cycles))
	print "Min. cycles:", minimum_cycles
	count1 = count_dummy_nodes_necessary(deepcopy(minimum_cycles), graph_size)
	count2 = count_nodes_necessary(deepcopy(minimum_cycles))
	print "Total dummy nodes (min. cycles):", count1
	print "Total nodes (min. cycles):", count2

	outfile = "outputs/output_sanders_" + str(getseed()) + "_" + str(graph_size) + ".txt"
	with open(outfile, 'w') as text_file:
		text_file.write("Unique dummy nodes: \t\t\t %s \nTotal dummy nodes: \t\t\t\t %s \nTotal nodes (min. cycles): \t\t %s \nTime: \t\t\t\t\t\t\t %s" % (str(len(newGraph2) - graph_size), count1, count2, str(time.time() - start_time)))
	print "=================END====================="
