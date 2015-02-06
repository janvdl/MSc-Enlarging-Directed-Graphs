import time
from generator import get_graph, get_random_seq
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
from augmentor import SandersFirst, SandersSecond
from copy import deepcopy

print "Debugging"
new_G = [[1], [2], [3,6], [0,4], [0,5], [6], [4]]
print new_G
cycles = entry_tarjan(deepcopy(new_G))
minimum_cycles = min_cycles(deepcopy(cycles))
smallest_cycles = small_cycles(deepcopy(cycles))

print "Cycles:", cycles
print "Min:", minimum_cycles
print "Small:", smallest_cycles