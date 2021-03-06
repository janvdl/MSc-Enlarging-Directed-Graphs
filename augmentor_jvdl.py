from tarjan import entry_tarjan
from hopcroft import hopcroft
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes
from node_evaluator import evaluate
import operator
from copy import deepcopy

def augment(G, seq, cycles):
    cycleNodesKeeper = sum(cycles, [])
    node_scores = evaluate(G, cycles)
    while (situation_matrix(find_all_types_nodes(G)) != [0, 0, 0, 0]):
        components = hopcroft(G)
        for component in components:
            #Update the situation matrix after every component has been updated
            #It's possible that some isolated nodes were already taken care of, etc.
            CGI_nodes = find_all_types_nodes(G)
            greedy_nodes = CGI_nodes[1]
            charity_nodes = CGI_nodes[0]
            isolated_nodes = CGI_nodes[2]
            matrix = situation_matrix(CGI_nodes)

            component_matrix = [0, 0, 0, 0]

            greedy_component = []
            charity_component = []
            isolated_component = []

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

            sub_matrix = component_matrix[0:3]

            if sub_matrix == [0, 0, 1]:
                #print "Case 1 - Isolated node only"
                iso_node = isolated_component.pop()
                iso_seq = seq[iso_node]

                dummy = [iso_seq[1], iso_seq[0]]
                dummy_node = len(G)
                seq.append(dummy)

                G.append([])
                G[dummy_node].append(iso_node)
                G[iso_node].append(dummy_node)
            elif sub_matrix == [0, 1, 0]:
                #print "Case 2 - Greedy node only"
                greedy_node = greedy_component.pop()
                greedy_seq = seq[greedy_node]

                some_nodes = (set(component) - (set(greedy_component) | set([greedy_node])))
                combined = list(set(cycleNodesKeeper) & some_nodes)

                if len(combined) > 0:
                    some_node = combined[0]
                    #Node scoring implemented here
                    for scored_node in node_scores:
                        if scored_node in combined:
                            some_node = scored_node
                    #END Node scoring
                else:
                    some_node = list(some_nodes)[0]
                    #Node scoring implemented here
                    for scored_node in node_scores:
                        if scored_node in some_nodes:
                            some_node = scored_node
                    #END Node scoring

                some_seq = seq[some_node]

                dummy = [some_seq[1], greedy_seq[0]]
                dummy_node = len(G)
                seq.append(dummy)

                G.append([])
                G[greedy_node].append(dummy_node)
                G[dummy_node].append(some_node)
            elif sub_matrix == [1, 0, 0]:
                #print "Case 3 - Charity node only"
                charity_node = charity_component.pop()
                charity_seq = seq[charity_node]

                some_nodes = (set(component) - (set(charity_component) | set([charity_node])))
                combined = list(set(cycleNodesKeeper) & some_nodes)

                if len(combined) > 0:
                    some_node = combined[0]
                    #Node scoring implemented here
                    for scored_node in node_scores:
                        if scored_node in combined:
                            some_node = scored_node
                    #END Node scoring
                else:
                    some_node = list(some_nodes)[0]
                    #Node scoring implemented here
                    for scored_node in node_scores:
                        if scored_node in some_nodes:
                            some_node = scored_node
                    #END Node scoring

                some_seq = seq[some_node]

                dummy = [charity_seq[1], some_seq[0]]
                dummy_node = len(G)
                seq.append(dummy)

                G.append([])
                G[some_node].append(dummy_node)
                G[dummy_node].append(charity_node)
            elif sub_matrix == [0, 1, 1]:
                #print "Case 4 - Iso + Greedy"
                iso_node = isolated_component.pop()
                iso_seq = seq[iso_node]

                greedy_node = greedy_component.pop()
                greedy_seq = seq[greedy_node]

                some_nodes = (set(component) - (set(greedy_component) | set(isolated_component) | set([greedy_node]) | set([iso_node])))
                combined = list(set(cycleNodesKeeper) & some_nodes)

                if len(combined) > 0:
                    some_node = combined[0]
                    #Node scoring implemented here
                    for scored_node in node_scores:
                        if scored_node in combined:
                            some_node = scored_node
                    #END Node scoring
                else:
                    some_node = list(some_nodes)[0]
                    #Node scoring implemented here
                    for scored_node in node_scores:
                        if scored_node in some_nodes:
                            some_node = scored_node
                    #END Node scoring

                some_seq = seq[some_node]

                dummy1 = [iso_seq[1], greedy_seq[0]]
                dummy1_node = len(G)
                seq.append(dummy1)

                dummy2 = [some_seq[1], iso_seq[0]]
                dummy2_node = len(G) + 1
                seq.append(dummy2)

                G.append([])
                G.append([])
                G[greedy_node].append(dummy1_node)
                G[dummy1_node].append(iso_node)
                G[iso_node].append(dummy2_node)
                G[dummy2_node].append(some_node)
            elif sub_matrix == [1, 0, 1]:
                #print "Case 5 - Iso + Charity"
                iso_node = isolated_component.pop()
                iso_seq = seq[iso_node]

                charity_node = charity_component.pop()
                charity_seq = seq[charity_node]

                some_nodes = set(component) - (set(charity_component) | set(isolated_component) | set([charity_node]) | set([iso_node]))
                combined = list(set(cycleNodesKeeper) & some_nodes)

                if len(combined) > 0:
                    some_node = combined[0]
                    #Node scoring implemented here
                    for scored_node in node_scores:
                        if scored_node in combined:
                            some_node = scored_node
                    #END Node scoring
                else:
                    some_node = list(some_nodes)[0]
                    #Node scoring implemented here
                    for scored_node in node_scores:
                        if scored_node in some_nodes:
                            some_node = scored_node
                    #END Node scoring

                some_seq = seq[some_node]

                dummy1 = [iso_seq[1], some_seq[0]]
                dummy1_node = len(G)
                seq.append(dummy1)

                dummy2 = [charity_seq[1], iso_seq[0]]
                dummy2_node = len(G) + 1
                seq.append(dummy2)

                G.append([])
                G.append([])
                G[some_node].append(dummy1_node)
                G[dummy1_node].append(iso_node)
                G[iso_node].append(dummy2_node)
                G[dummy2_node].append(charity_node)
            elif sub_matrix == [1, 1, 0]:
                #print "Case 6 - Charity + Greedy"
                charity_node = charity_component.pop()
                charity_seq = seq[charity_node]

                greedy_node = greedy_component.pop()
                greedy_seq = seq[greedy_node]

                dummy = [charity_seq[1], greedy_seq[0]]
                dummy_node = len(G)
                seq.append(dummy)

                G.append([])
                G[greedy_node].append(dummy_node)
                G[dummy_node].append(charity_node)
            elif sub_matrix == [1, 1, 1]:
                #print "Case 7 - Charity + Greedy + Iso"
                iso_node = isolated_component.pop()
                iso_seq = seq[iso_node]

                charity_node = charity_component.pop()
                charity_seq = seq[charity_node]

                greedy_node = greedy_component.pop()
                greedy_seq = seq[greedy_node]

                dummy1 = [iso_seq[1], greedy_seq[0]]
                dummy1_node = len(G)
                seq.append(dummy1)

                dummy2 = [charity_seq[1], iso_seq[0]]
                dummy2_node = len(G) + 1
                seq.append(dummy2)

                G.append([])
                G.append([])
                G[greedy_node].append(dummy1_node)
                G[dummy1_node].append(iso_node)
                G[iso_node].append(dummy2_node)
                G[dummy2_node].append(charity_node)

    #Handle bridge nodes, if any
    cycles = sum(entry_tarjan(deepcopy(G)), [])
    nodes = list(xrange(0, len(G)))
    no_cycles = list(set(nodes) - set(cycles))

    while len(no_cycles) > 0:
        x = no_cycles[0]
        B = x
        E = None
        while (B in no_cycles):
            for adjacency in G[B]:
                if adjacency not in no_cycles:
                    B = adjacency
                    break
            break

        for i in xrange(0, len(G)):
            if x in G[i]:
                E = i

        while (E in no_cycles):
            for i in xrange(0, len(G)):
                if G[i] == E and G[i] not in no_cycles:
                    E = G[i]
                    break
            break

        D = [seq[E][1], seq[B][0]]
        seq.append(D)
        D_nodenumber = len(G)
        G.append([])
        G[B].append(D_nodenumber)
        G[D_nodenumber].append(E)
        no_cycles.pop(0)

        cycles = sum(entry_tarjan(deepcopy(G)), [])
        nodes = list(xrange(0, len(G)))
        no_cycles = list(set(nodes) - set(cycles))

    return G

def situation_matrix(CGI_nodes):
    #return matrix [C G I N] -> charity, greedy, isolated, no cycle
    greedy_nodes = CGI_nodes[1]
    charity_nodes = CGI_nodes[0]
    isolated_nodes = CGI_nodes[2]

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
    N_ = 0

    matrix = []
    matrix.append(C_)
    matrix.append(G_)
    matrix.append(I_)
    matrix.append(N_)

    return matrix
