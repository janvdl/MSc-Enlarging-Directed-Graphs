from random import randint
from tarjan import entry_tarjan
from copy import deepcopy
from graphviz import get_graphviz_names_from_graph
from cyclepicker import min_cycles, small_cycles, find_spill_nodes, find_all_types_nodes

def SandersFirst(G, seq, cycles, dis, no_in, no_out):
    newGraph = G[:]
    usedNodes = []
    cycleNodes = sum(cycles, [])
    while len(dis) > 0 or len(no_in) > 0 or len(no_out) > 0:
        first = None
        last = None
        mid = None

        if len(no_out) > 0:
            first = no_out.pop(0)

        if len(no_in) > 0:
            last = no_in.pop(0)

        if len(dis) > 0:
            mid = dis.pop(0)

        if mid != None:
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
            seq.append(dummy3)

            dummy3_nodenumber = len(newGraph)
            newGraph.append([])
            newGraph[first].append(dummy3_nodenumber)
            newGraph[dummy3_nodenumber].append(last)
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
