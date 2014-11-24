from random import randint
from tarjan import entry_tarjan
from copy import deepcopy
from hopcroft import hopcroft
from graphviz import get_graphviz_names_from_graph

def augment(G, seq, cycles, dis, no_in, no_out):
    newGraph = G[:]
    usedNodes = []
    while len(dis) > 0 or len(no_in) > 0 or len(no_out) > 0:
        first = None
        last = None
        mid = None        
        
        components = hopcroft(newGraph)
        #print "Components:", components
        selected_component = []
        
        if len(no_out) > 0:
            first = no_out.pop(0)
            selected_component = findParentComponent(first, components)
            
            last_list = list((set(selected_component)) & (set(no_in)))
            if len(last_list) > 0:
                last = last_list.pop(0)
            else:
                last = None
                
            mid_list = list((set(selected_component)) & (set(dis)))
            if len(mid_list) > 0:
                mid = mid_list.pop(0)
            else:
                mid = None
            
            #print "1 Intermediate first,mid,last,component:", first, mid, last, selected_component
            
        elif len(no_in) > 0:
            last = no_in.pop(0)
            selected_component = findParentComponent(last, components)
            
            first_list = list((set(selected_component)) & (set(no_out)))
            if len(first_list) > 0:
                first = first_list.pop(0)
            else:
                first = None
                
            mid_list = list((set(selected_component)) & (set(dis)))
            if len(mid_list) > 0:
                mid = mid_list.pop(0)
            else:
                mid = None
            
            #print "2 Intermediate first,mid,last,component:", first, mid, last, selected_component
            
        elif len(dis) > 0:
            mid = dis.pop(0)
            selected_component = findParentComponent(mid, components)
            
            first_list = list((set(selected_component)) & (set(no_out)))
            if len(first_list) > 0:
                first = first_list.pop(0)
            else:
                first = None
            
            last_list = list((set(selected_component)) & (set(no_in)))
            if len(last_list) > 0:
                last = last_list.pop(0)
            else:
                last = None
            
            #print "3 Intermediate first,mid,last,component:", first, mid, last, selected_component                
        
        cycleNodes = selected_component
        #print "Selected first,mid,last,component:", first, mid, last, selected_component
            
        if mid != None:
            if first == None and last == None:
                #create dummy node dummy0, mirror of mid
                dummy0 = [seq[mid][1], seq[mid][0]]
                seq.append(dummy0)
                
                #create path mid -> dummy0 -> mid in newGraph
                dummy0_nodenumber = len(newGraph)
                newGraph.append([]) #append one placeholder
                newGraph[mid].append(dummy0_nodenumber)
                newGraph[dummy0_nodenumber].append(mid)
            else:
                if first == None:
                    availableNodes = list(set(cycleNodes) - set(usedNodes))
                    if len(availableNodes) > 0:
                        first = availableNodes[0]
                        usedNodes.append(first)
                    else:
                        print cycleNodes
                        first = cycleNodes[randint(0, len(cycleNodes))]
                if last == None:
                    availableNodes = list(set(cycleNodes) - set(usedNodes))
                    if len(availableNodes) > 0:
                        last = availableNodes[0]
                        usedNodes.append(last)
                    else:
                        last = cycleNodes[randint(0, len(cycleNodes))]
            
                #create nodes dummy1 and dummy2
                dummy1 = [seq[mid][1], seq[first][0]]
                dummy2 = [seq[last][1], seq[mid][0]]
                seq.append(dummy1)
                seq.append(dummy2)
                
                #create path first -> dummy1 -> mid -> dummy2 -> last in newGraph
                dummy1_nodenumber = len(newGraph)
                dummy2_nodenumber = len(newGraph) + 1
                newGraph.append([]) #append two placeholders
                newGraph.append([])
                newGraph[first].append(dummy1_nodenumber)
                newGraph[dummy1_nodenumber].append(mid)
                newGraph[mid].append(dummy2_nodenumber)
                newGraph[dummy2_nodenumber].append(last)
        else:
            if first == None:
                availableNodes = list(set(cycleNodes) - set(usedNodes))
                if len(availableNodes) > 0:
                    first = availableNodes[0]
                    usedNodes.append(first)
                else:
                    first = cycleNodes[randint(0, len(cycleNodes))]
            if last == None:
                availableNodes = list(set(cycleNodes) - set(usedNodes))
                if len(availableNodes) > 0:
                    last = availableNodes[0]
                    usedNodes.append(last)
                else:
                    last = cycleNodes[randint(0, len(cycleNodes))]
                    
            #create node dummy3
            dummy3 = [seq[last][1], seq[first][0]]
            #print "Dummy 3:", dummy3
            seq.append(dummy3)
            
            #create path first -> dummy3 -> last in newGraph
            dummy3_nodenumber = len(newGraph)
            newGraph.append([]) #append a placeholder
            newGraph[first].append(dummy3_nodenumber)
            newGraph[dummy3_nodenumber].append(last)
    #print "no_in, no_out, dis", no_in, no_out, dis
    return newGraph
    
def findParentComponent(node, components):
    for component in components:
        if node in component:
            return component