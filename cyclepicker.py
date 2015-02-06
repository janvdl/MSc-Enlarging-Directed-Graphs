from copy import deepcopy

cycles          = []    #all cycles of nodes
picked_cycles   = []
contained_nodes = []
spill_nodes     = []

def min_cycles(cycles_):
    global cycles, picked_cycles, spill_nodes
    cycles = cycles_
    picked_cycles = deepcopy(cycles)    
    nodes_in_cycles = set(sum(cycles_, []))

    # for cycle1 in cycles_[:]:
    #     for cycle2 in cycles_[:]:
    #         if sorted(cycle1) != sorted(cycle2) and (set(cycle2)).issubset(set(cycle1)):
    #             if cycle2 in picked_cycles:
    #                 picked_cycles.remove(cycle2)
    #         if sorted(cycle1) == sorted(cycle2):
    #             if cycles_.index(cycle1) < cycles_.index(cycle2) and cycle2 in picked_cycles:
    #                 picked_cycles.remove(cycle2)

    for cycle1 in cycles_[:]:
        for cycle2 in cycles_[:]:
            if cycle1 != cycle2:
                copy = deepcopy(picked_cycles)
                if cycle2 in copy:
                    copy.remove(cycle2)
                post_nodes_in_cycles = set(sum(copy, []))
                if len(nodes_in_cycles) == len(post_nodes_in_cycles) and cycle2 in picked_cycles:
                    picked_cycles.remove(cycle2)

    return picked_cycles

def small_cycles(cycles_):
    global cycles, picked_cycles, spill_nodes
    cycles = cycles_
    picked_cycles = deepcopy(cycles)

    #Keep track of nodes in cycles. We cannot lose any nodes by dropping supersets.
    nodes_in_cycles = set(sum(cycles_, []))

    # for cycle1 in cycles_[:]:
    #     for cycle2 in cycles_[:]:
    #         if sorted(cycle1) != sorted(cycle2) and (set(cycle2)).issuperset(set(cycle1)):
    #             if cycle2 in picked_cycles:
    #                 #Check if we're losing nodes by dropping the superset
    #                 copy = deepcopy(picked_cycles)
    #                 copy.remove(cycle2)
    #                 post_nodes_in_cycles = set(sum(copy, []))
    #                 if len(nodes_in_cycles) == len(post_nodes_in_cycles):
    #                     picked_cycles.remove(cycle2)
    #                 # else:
    #                 #     print 'removing', cycle2, 'would cause', sorted(nodes_in_cycles), 'to become', sorted(post_nodes_in_cycles)
    #         if sorted(cycle1) == sorted(cycle2):
    #             if cycles_.index(cycle1) < cycles_.index(cycle2) and cycle2 in picked_cycles:
    #                 #Check if we're losing nodes by dropping the superset
    #                 copy = deepcopy(picked_cycles)
    #                 copy.remove(cycle2)
    #                 post_nodes_in_cycles = set(sum(copy, []))
    #                 if len(nodes_in_cycles) == len(post_nodes_in_cycles):
    #                     picked_cycles.remove(cycle2)
    #                 # else:
    #                 #     print 'removing', cycle2, 'would cause', sorted(nodes_in_cycles), 'to become', sorted(post_nodes_in_cycles)

    for cycle1 in cycles_[:]:
        for cycle2 in cycles_[:]:
            if cycle1 != cycle2:
                copy = deepcopy(picked_cycles)
                if cycle2 in copy:
                    copy.remove(cycle2)
                post_nodes_in_cycles = set(sum(copy, []))
                if len(nodes_in_cycles) == len(post_nodes_in_cycles) and cycle2 in picked_cycles:
                    picked_cycles.remove(cycle2)

    return picked_cycles

#This method counts the frequency of nodes
#Every time a node is found in a cycle, the count is increased
def count_nodes(cycles_):
    d = dict()

    for c in cycles_:
        for node in c:
            if node in d:
                d[node] = d[node] + 1
            else:
                d[node] = 1

    return d

def count_nodes_necessary(cycles_):
    d = count_nodes(cycles_)
    nodes_necessary = 0

    for node in d:
            nodes_necessary = nodes_necessary + d[node]

    return nodes_necessary

def count_dummy_nodes_necessary(cycles_, graph_size):
    d = count_nodes(cycles_)
    dummy_nodes_necessary = 0

    for node in d:
        if node >= graph_size:
            dummy_nodes_necessary = dummy_nodes_necessary + d[node]

    return dummy_nodes_necessary

def find_spill_nodes(seq_):
    global spill_nodes, picked_cycles
    spill_nodes = list(xrange(0, len(seq_[:])))

    for cycle in picked_cycles:
        for i in xrange(0, len(seq_)):
            if i in cycle[:] and i in spill_nodes:
                spill_nodes.pop(spill_nodes.index(i))

    return spill_nodes

def find_isogreedy_nodes(G_):
    greedy_nodes = []
    for i in xrange(0, len(G_)):
        if len(G_[i]) == 0:
            greedy_nodes.append(i)
    
    return greedy_nodes

def find_isocharity_nodes(G_):
    charity_nodes = list(xrange(0, len(G_)))
    for node in G_:
        for adjacency in node:
            if adjacency in charity_nodes:
                charity_nodes.remove(adjacency)
    
    return charity_nodes
    
def find_greedy_nodes(G_):
    isogreedy_nodes = find_isogreedy_nodes(G_)
    isolated_nodes = find_isolated_nodes(G_)
    
    return list(set(isogreedy_nodes) - set(isolated_nodes))
    
def find_charity_nodes(G_):
    isocharity_nodes = find_isocharity_nodes(G_)
    isolated_nodes = find_isolated_nodes(G_)
    
    return list(set(isocharity_nodes) - set(isolated_nodes))
        
def find_isolated_nodes(G_):
    isolated_nodes = []
    greedy_nodes = find_isogreedy_nodes(G_)
    charity_nodes = find_isocharity_nodes(G_)
    for node in greedy_nodes:
        if node in charity_nodes:
            isolated_nodes.append(node)
            
    return isolated_nodes

# Runs in O(n^2)
def find_all_types_nodes(G_):
    isolated_nodes = []
    temp_greedy = find_isogreedy_nodes(G_)
    temp_charity = find_isocharity_nodes(G_) # This is O(n^2)

    for node in temp_greedy:
        if node in temp_charity:
            isolated_nodes.append(node)

    greedy_nodes = list(set(temp_greedy) - set(isolated_nodes))
    charity_nodes = list(set(temp_charity) - set(isolated_nodes))

    return [charity_nodes, greedy_nodes, isolated_nodes]