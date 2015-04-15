import time
from generator import get_graph, get_random_seq, getseed
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes
from augmentor import SandersFirst, SandersSecond
from copy import deepcopy

# for i in xrange(8, 20):
# 	graph_size = i
# 	seq = get_random_seq(graph_size)
# 	G = get_graph(seq)
# 	cycles = entry_tarjan(deepcopy(G))
#  	print i, len(cycles)#, seq


i = 27
graph_size = i
seq = get_random_seq(graph_size)
G = get_graph(seq)
cycles = entry_tarjan(deepcopy(G))
print i, len(cycles)#, seq
