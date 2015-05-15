import time
from generator import get_graph, get_random_seq, getseed
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph, get_graphviz_names_from_graph_compromising, get_cycle_latex
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
from augmentor_jvdl import augment
from copy import deepcopy
from rcomb import built_in_rcombs, custom_rcomb

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

for i in xrange(8, 10, 2):
	start_time = time.time()

	#Generate a random graph or specify it
	graph_size = 18
	seq = get_random_seq(graph_size)
	#print seq
	G = get_graph(seq)

	#Find the cycles in the graph
	cycles = entry_tarjan(deepcopy(G))
	#print "All cycles: \n", get_cycle_latex(cycles)

	#Find the cycle combinations containing each node only once
	SingleNodeCycles = []
	Continue_ = True
	for i in xrange(1, len(cycles)):
		Continue_ = False
		comb_cycles = custom_rcomb(cycles, i)
		for cycles_ in comb_cycles:
			if ContainsOnlySingleNodes(cycles_):
				Continue_ = True
				SingleNodeCycles.append(cycles_)
		if not Continue_:
			break

	#Select some combination to continue with
	other_nodes = set([]) #Initialise other_nodes for later use
	if len(SingleNodeCycles) != 0:
		selected_comb = list((sorted(SingleNodeCycles, key=len))[-1])
		print "Selected combination:", selected_comb
		original_cycles = deepcopy(selected_comb)
		nodes_in_selected_comb = (set(sum(selected_comb, [])))
		other_nodes = set(xrange(0, graph_size)) - nodes_in_selected_comb
		print "Other nodes:", other_nodes
		subseq = [seq[k] for k in other_nodes]
		subG = get_graph(subseq)
		subcycles = entry_tarjan(deepcopy(subG))
	else:
		print "No single node cycles!"
		subseq = seq
		subG = G
		subcycles = cycles

	#Find the greedy, charity, and isolated nodes
	CGI = find_all_types_nodes(subG)
	greedy_nodes = CGI[1]
	charity_nodes = CGI[0]
	isolated_nodes = CGI[2]

	newGraph = augment(deepcopy(subG), subseq, subcycles[:])
	newGraph2 = newGraph

	if len(SingleNodeCycles) != 0:
		print "\n=================Compromising Algorithm==========="
		print "Number of nodes: ", graph_size
		print "Time: ", time.time() - start_time, "seconds"
		print "Dummy nodes needed:", (len(newGraph2) + len(nodes_in_selected_comb)) - graph_size
		original_cycles = original_cycles
		subcycles = entry_tarjan(deepcopy(newGraph2))
		print ""
		minimum_cycles = min_cycles(deepcopy(subcycles))
		print "Min. cycles:", original_cycles, " + ", minimum_cycles
		count1 = count_dummy_nodes_necessary(deepcopy(minimum_cycles), len(subG))
		count2 = count_nodes_necessary(deepcopy(minimum_cycles)) + count_nodes_necessary(deepcopy(original_cycles))
		print "Total dummy nodes (min. cycles):", count1
		print "Total nodes (min. cycles):", count2

		outfile = "outputs/output_compromising_" + str(getseed()) + "_" + str(graph_size) + ".txt"
		with open(outfile, 'w') as text_file:
			text_file.write("Unique dummy nodes: \t\t\t %s \nTotal dummy nodes: \t\t\t\t %s \nTotal nodes (min. cycles): \t\t %s \nTime: \t\t\t\t\t\t\t %s" % (str(len(newGraph2) - len(subG)), count1, count2, str(time.time() - start_time)))
		print ""
		print "=================END======================"
	else:
		print "No single node cycles!"
