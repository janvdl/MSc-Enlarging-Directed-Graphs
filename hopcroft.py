from copy import deepcopy

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

    comp_ = deepcopy(components)
            
    for i in xrange(0, len(comp_)):
        for j in xrange(0, len(comp_)):
            if i > j and (set(comp_[i]) >= set(comp_[j])):
                if comp_[j] in components:
                    components.remove(comp_[j])
        
    return components