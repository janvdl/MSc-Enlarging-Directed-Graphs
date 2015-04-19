from copy import deepcopy
from collections import defaultdict

components = []
visited = []

def dfs(G, v):
    S = []
    component = []
    nodes_in_components = sum(components, [])

    if v not in nodes_in_components:
        S.append(v)
        while (len(S) > 0):
            u = S.pop()
            if visited[u] == False:
                visited[u] = True
                component.append(u)
                for w in G[u]:
                    S.append(w)

        components.append(component)

def hopcroft(G):
    global visited
    for i in xrange(0, len(G)):
        visited = [False for x in xrange(len(G))]
        if visited[i] == False:
            dfs(G, i)

    return connected_components(components)

def connected_components(l):
    out = []
    while len(l)>0:
        first, rest = l[0], l[1:]
        first = set(first)

        lf = -1
        while len(first)>lf:
            lf = len(first)

            rest2 = []
            for r in rest:
                if len(first.intersection(set(r)))>0:
                    first |= set(r)
                else:
                    rest2.append(r)
            rest = rest2

        out.append(list(first))
        l = rest
    return out
