from tarjan import entry_tarjan
from hopcroft import hopcroft
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_isogreedy_nodes, find_greedy_nodes, find_isocharity_nodes, find_charity_nodes, find_isolated_nodes
from copy import deepcopy

def augment(G, seq):
    while (situation_matrix(G) != [0, 0, 0, 0]):        
        matrix = situation_matrix(G)
        components = hopcroft(G)
     
        greedy_nodes = find_greedy_nodes(G)
        charity_nodes = find_charity_nodes(G)
        isolated_nodes = find_isolated_nodes(G)
    
        cycles = sum(entry_tarjan(deepcopy(G)), [])
        nodes = list(xrange(0, len(G)))
        no_cycles = list(set(nodes) - set(cycles))
    
        for component in components:
            print "Current component:", component
            C_ = matrix[0]
            G_ = matrix[1]
            I_ = matrix[2]
            N_ = matrix[3]
            
            component_matrix = [0, 0, 0, 0]
            
            greedy_component = []
            charity_component = []
            isolated_component = []
            nocycles_component = []
            
            for node in charity_nodes:
                if node in component:
                    charity_component.append(node)
                    component_matrix[0] = 1
            
            for node in greedy_nodes:
                if node in component:
                    greedy_component.append(node)
                    component_matrix[1] = 1
            
            #Any isolated nodes are available for use
            isolated_component = isolated_nodes
            component_matrix[2] = matrix[2]
            
            for node in no_cycles:
                if node in component:
                    nocycles_component.append(node)
                    component_matrix[3] = 1
                    
            sub_matrix = component_matrix[0:3]
            
            if sub_matrix == [0, 0, 1]:
                print "Case 1 - Isolated node only"
                iso_node = isolated_component.pop()
                iso_seq = seq[iso_node]
                
                dummy = [iso_seq[1], iso_seq[0]]
                dummy_node = len(G)
                seq.append(dummy)
                
                G.append([])
                G[dummy_node].append(iso_node)
                G[iso_node].append(dummy_node)
                print G
            elif sub_matrix == [0, 1, 0]:
                print "Case 2 - Greedy node only"
                greedy_node = greedy_component.pop()
                greedy_seq = seq[greedy_node]

                some_node = list(set(component) - (set(greedy_component)))[0]
                some_seq = seq[some_node]
                
                dummy = [some_seq[1], greedy_seq[0]]
                dummy_node = len(G)
                seq.append(dummy)
                
                G.append([])
                G[greedy_node].append(dummy_node)
                G[dummy_node].append(some_node)
            elif sub_matrix == [1, 0, 0]:
                print "Case 3 - Charity node only"
                charity_node = charity_component.pop()
                charity_seq = seq[charity_node]

                some_node = list(set(component) - (set(charity_component)))[0]
                some_seq = seq[some_node]
                
                dummy = [charity_seq[1], some_seq[0]]
                dummy_node = len(G)
                seq.append(dummy)
                
                G.append([])
                G[some_node].append(dummy_node)
                G[dummy_node].append(charity_node)
            elif sub_matrix == [0, 1, 1]:
                print "Case 4 - Iso + Greedy"
            elif sub_matrix == [1, 0, 1]:
                print "Case 5 - Iso + Charity"
            elif sub_matrix == [1, 1, 0]:
                print "Case 6 - Charity + Greedy"
            elif sub_matrix == [1, 1, 1]:
                print "Case 7 - Charity + Greedy + Iso"
        break
    
def situation_matrix(G):
    #return matrix [C G I N] -> charity, greedy, isolated, no cycle
     
    greedy_nodes = find_greedy_nodes(G)
    charity_nodes = find_charity_nodes(G)
    isolated_nodes = find_isolated_nodes(G)
    
    cycles = sum(entry_tarjan(deepcopy(G)), [])
    nodes = list(xrange(0, len(G)))
    no_cycles = list(set(nodes) - set(cycles))
    
    C_ = 0
    G_ = 0
    I_ = 0
    N_ = 0
    if len(charity_nodes) > 0:
        C_ = 1
    if len(greedy_nodes) > 0:
        G_ = 1
    if len(isolated_nodes) > 0:
        I_ = 1
    if len(no_cycles) > 0:
        N_ = 1
        
    matrix = []
    matrix.append(C_)
    matrix.append(G_)
    matrix.append(I_)
    matrix.append(N_)
        
    return matrix