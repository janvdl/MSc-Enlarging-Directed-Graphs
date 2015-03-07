from copy import deepcopy
from rcomb import combination

cycles          = []    #all cycles of nodes
picked_cycles   = []
contained_nodes = []
spill_nodes     = []

def small_cycles(cycles_):
    r = len(cycles_)
    all_picked_cycles = combination(cycles_, r)

    while (len(all_picked_cycles) < 1 and r >= 1):
        try:
            #try except needed for 
            r = r - 1
            all_picked_cycles = combination(cycles_, r)
        except:
            r = r - 1

    #Determine smallest number of nodes
    index = 0
    max_ = 999999999999999999
    for i in xrange(0, len(all_picked_cycles)):
        count_ = count_nodes_necessary(all_picked_cycles[i])
        if count_ <= max_:
            max_ = count_
            index = i
    return all_picked_cycles[index]

# def rcombs(cycles_, r):

#print min_cycles([[0, 1], [0, 1, 8, 4], [0, 1, 8, 5], [0, 1, 8, 7, 2], [0, 1, 8, 7, 3], [0, 1, 8, 7, 9, 4], [0, 1, 8, 7, 9, 5], [0, 6, 2], [0, 6, 2, 8, 4], [0, 6, 2, 8, 5], [0, 6, 2, 8, 7, 3], [0, 6, 2, 8, 7, 9, 4], [0, 6, 2, 8, 7, 9, 5], [0, 6, 3], [0, 6, 3, 8, 4], [0, 6, 3, 8, 5], [0, 6, 3, 8, 7, 2], [0, 6, 3, 8, 7, 9, 4], [0, 6, 3, 8, 7, 9, 5], [0, 6, 9, 4], [0, 6, 9, 4, 8, 5], [0, 6, 9, 4, 8, 7, 2], [0, 6, 9, 4, 8, 7, 3], [0, 6, 9, 5], [0, 6, 9, 5, 8, 4], [0, 6, 9, 5, 8, 7, 2], [0, 6, 9, 5, 8, 7, 3], [0, 6, 9, 7, 2], [0, 6, 9, 7, 2, 8, 4], [0, 6, 9, 7, 2, 8, 5], [0, 6, 9, 7, 3], [0, 6, 9, 7, 3, 8, 4], [0, 6, 9, 7, 3, 8, 5], [2, 8, 7], [3, 8, 7], [4, 8], [4, 8, 7, 9], [5, 8], [5, 8, 7, 9], [7, 9], [11, 14]])

def min_cycles(cycles_):
    r = 0
    all_picked_cycles = combination(cycles_, r)

    while (len(all_picked_cycles) < 1 and r <= len(cycles_)):
        try:
            #try except needed for 
            r = r + 1
            all_picked_cycles = combination(cycles_, r)
        except:
            r = r + 1

    #Determine smallest number of nodes
    index = 0
    max_ = 999999999999999999
    for i in xrange(0, len(all_picked_cycles)):
        count_ = count_nodes_necessary(all_picked_cycles[i])
        if count_ <= max_:
            max_ = count_
            index = i
    return all_picked_cycles[index]

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