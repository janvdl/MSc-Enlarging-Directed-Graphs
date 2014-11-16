#The source code given below is a modified version of the implementation by Johannes Schauer.
#https://github.com/josch/cycles_tarjan/blob/master/cycles.py

from copy import deepcopy

G = []
cycles = []

point_stack = list()
marked = dict()
marked_stack = list()

def tarjan(s, v):
    global cycles
    f = False
    point_stack.append(v)
    marked[v] = True
    marked_stack.append(v)
    for w in G[v]:
        if w<s:
            G[w] = 0
        elif w==s:
            cycles.append(list(deepcopy(point_stack)))
            f = True
        elif not marked[w]:
            f = tarjan(s,w) or f
            
    if f == True:
        while marked_stack[-1] != v:
            u = marked_stack.pop()
            marked[u] = False
        marked_stack.pop()
        marked[v] = False
        
    point_stack.pop()
    return f
        
def entry_tarjan(G_):
    global G, cycles
    G = deepcopy(G_)

    for i in range(len(G)):
        marked[i] = False
    
    for i in range(len(G)):
        tarjan(i, i)
        while marked_stack:
            u = marked_stack.pop()
            marked[u] = False
    
    return cycles