from random import randint
from tarjan import entry_tarjan
from copy import deepcopy
from hopcroft import hopcroft
from graphviz import get_graphviz_names_from_graph
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes

def augment(G, seq, cycles, dis, no_in, no_out):
    newGraph = G[:]
    usedNodes = []
    cycleNodesKeeper = sum(cycles, [])

    print "Graph:", newGraph
    components = hopcroft(deepcopy(newGraph))
    print "Components:", components

    while len(dis) > 0 or len(no_in) > 0 or len(no_out) > 0:
        first = None
        last = None
        mid = None

        selected_component = []

        if len(no_out) > 0:
            first = no_out.pop(0)
            selected_component = findParentComponent(first, components)

            last_list = list((set(selected_component)) & (set(no_in)))
            if first in last_list:
                last_list.remove(first)

            if len(last_list) > 0:
                last = last_list.pop(0)
            else:
                last = None

            mid_list = list((set(selected_component)) & (set(dis)))
            if first in mid_list:
                mid_list.remove(first)

            if len(mid_list) > 0:
                mid = mid_list.pop(0)
            else:
                mid = None

            print "1 Intermediate first,mid,last,component:", first, mid, last, selected_component

        elif len(no_in) > 0:
            last = no_in.pop(0)
            selected_component = findParentComponent(last, components)

            first_list = list((set(selected_component)) & (set(no_out)))
            if last in first_list:
                first_list.remove(last)

            if len(first_list) > 0:
                first = first_list.pop(0)
            else:
                first = None

            mid_list = list((set(selected_component)) & (set(dis)))
            if last in mid_list:
                mid_list.remove(last)

            if len(mid_list) > 0:
                mid = mid_list.pop(0)
            else:
                mid = None

            print "2 Intermediate first,mid,last,component:", first, mid, last, selected_component

        elif len(dis) > 0:
            mid = dis.pop(0)
            selected_component = findParentComponent(mid, components)

            first_list = list((set(selected_component)) & (set(no_out)))
            if mid in first_list:
                first_list.remove(mid)

            if len(first_list) > 0:
                first = first_list.pop(0)
            else:
                first = None

            last_list = list((set(selected_component)) & (set(no_in)))
            if mid in last_list:
                last_list.remove(mid)

            if len(last_list) > 0:
                last = last_list.pop(0)
            else:
                last = None

            print "3 Intermediate first,mid,last,component:", first, mid, last, selected_component

        cycleNodes = selected_component
        combined = list(set(cycleNodesKeeper) & set(cycleNodes))
        if len(combined) > 0:
            cycleNodes = combined
        print "Selected first,mid,last,component:", first, mid, last, selected_component

        if mid != None:
            if first == None and last == None:
                dummy0 = [seq[mid][1], seq[mid][0]]
                seq.append(dummy0)

                dummy0_nodenumber = len(newGraph)
                newGraph[mid].append(dummy0_nodenumber)
                newGraph[dummy0_nodenumber].append(mid)
                print "Isolated only:", mid, dummy0_nodenumber
            else:
                if first == None:
                    availableNodes = list(set(cycleNodes) - set(usedNodes))
                    if last in availableNodes:
                        availableNodes.remove(last)
                    if len(availableNodes) > 0:
                        first = availableNodes[0]
                        usedNodes.append(first)
                    else:
                        first = cycleNodes[0]
                if last == None:
                    availableNodes = list(set(cycleNodes) - set(usedNodes))
                    if first in availableNodes:
                        availableNodes.remove(first)
                    if len(availableNodes) > 0:
                        last = availableNodes[0]
                        usedNodes.append(last)
                    else:
                        last = cycleNodes[0]

                dummy1 = [seq[mid][1], seq[first][0]]
                dummy2 = [seq[last][1], seq[mid][0]]
                seq.append(dummy1)
                seq.append(dummy2)

                dummy1_nodenumber = len(newGraph)
                dummy2_nodenumber = len(newGraph) + 1
                newGraph.append([])
                newGraph.append([])
                newGraph[first].append(dummy1_nodenumber)
                newGraph[dummy1_nodenumber].append(mid)
                newGraph[mid].append(dummy2_nodenumber)
                newGraph[dummy2_nodenumber].append(last)
                print first, mid, last, " & dummies:", dummy1_nodenumber, dummy2_nodenumber
        else:
            if first == None:
                availableNodes = list(set(cycleNodes) - set(usedNodes))
                if last in availableNodes:
                    availableNodes.remove(last)
                if len(availableNodes) > 0:
                    first = availableNodes[0]
                    usedNodes.append(first)
                else:
                    first = cycleNodes[0]
            if last == None:
                availableNodes = list(set(cycleNodes) - set(usedNodes))
                if first in availableNodes:
                    availableNodes.remove(first)
                if len(availableNodes) > 0:
                    last = availableNodes[0]
                    usedNodes.append(last)
                else:
                    last = cycleNodes[0]

            dummy3 = [seq[last][1], seq[first][0]]
            print "Dummy 3:", dummy3
            seq.append(dummy3)

            dummy3_nodenumber = len(newGraph)
            newGraph.append([])
            newGraph[first].append(dummy3_nodenumber)
            newGraph[dummy3_nodenumber].append(last)
            print first, mid, last, " & dummy:", dummy3_nodenumber
    return newGraph

def SandersSecond(G, seq, no_cycles):
    newGraph = G[:]
    while len(no_cycles) > 0:
        x = no_cycles[0]
        B = x
        E = None
        while (B in no_cycles):
            for adjacency in newGraph[B]:
                if adjacency not in no_cycles:
                    B = adjacency
                    break
            break

        for i in xrange(0, len(newGraph)):
            if x in newGraph[i]:
                E = i

        while (E in no_cycles):
            for i in xrange(0, len(newGraph)):
                if newGraph[i] == E and newGraph[i] not in no_cycles:
                    E = newGraph[i]
                    break
            break

        D = [seq[E][1], seq[B][0]]
        seq.append(D)
        D_nodenumber = len(newGraph)
        newGraph.append([])
        newGraph[B].append(D_nodenumber)
        newGraph[D_nodenumber].append(E)
        no_cycles.pop(0)

    return newGraph

def findParentComponent(node, components):
    for component in components:
        if node in component:
            return component
