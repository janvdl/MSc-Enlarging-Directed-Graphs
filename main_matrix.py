import time
from generator import get_graph, get_random_seq, get_matrix
from graphviz import get_graphviz, get_graphviz_names, get_graphviz_from_graph, get_graphviz_names_from_graph, get_graphviz_from_matrix
from tarjan import entry_tarjan
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes, count_nodes, count_dummy_nodes_necessary, count_nodes_necessary
from augmentor_matrix import augment
from copy import deepcopy

for i in xrange(8, 20, 2):
    start_time = time.time()

    #Generate a random graph or specify it
    graph_size = i
    seq = get_random_seq(graph_size)
    #seq = [[11,9],[12,10],[10,8],[8,10],[10,11],[9,10],[7,6],[6,7]]
    G = get_matrix(seq)
    #print G
    #print get_graphviz_from_matrix(G, seq, graph_size)
    results = augment(deepcopy(G), seq)
    G_ = results[0]
    newseq = results[1]
    #print get_graphviz_from_matrix(G_, newseq, graph_size)

    redundant_count = 0
    for node in newseq:
        if node[0] == node[1]:
            redundant_count = redundant_count + 1

    print "\n=================Matrix================="
    print "Number of nodes: ", graph_size
    print "Time: ", time.time() - start_time, "seconds"
    print "Dummy nodes needed:", (len(G_) - graph_size) - redundant_count
    print "All nodes necessary:", len(G_) - redundant_count
    print "=================END====================="
