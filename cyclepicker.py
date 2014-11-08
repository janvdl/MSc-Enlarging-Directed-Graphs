cycles          = []    #all cycles of nodes
picked_cycles   = []
contained_nodes = []
spill_nodes     = []

def min_cycles(cycles_):
    global cycles, picked_cycles, spill_nodes
    cycles = cycles_
    picked_cycles = cycles[:]

    for cycle1 in cycles_[:]:
        for cycle2 in cycles_[:]:
            if cycle1 != cycle2 and (set(cycle2)).issubset(set(cycle1)):
                if cycle2 in picked_cycles:
                    picked_cycles.remove(cycle2)

    return picked_cycles

def small_cycles(cycles_):
    global cycles, picked_cycles, spill_nodes
    cycles = cycles_
    picked_cycles = cycles[:]

    for cycle1 in cycles_[:]:
        for cycle2 in cycles_[:]:
            if cycle1 != cycle2 and (set(cycle2)).issuperset(set(cycle1)):
                if cycle2 in picked_cycles:
                    picked_cycles.remove(cycle2)

    return picked_cycles

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