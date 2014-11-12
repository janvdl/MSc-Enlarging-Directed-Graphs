components = []
visited = []

def dfs(G, v):
    S = []
    component = []
    
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
    visited = [False for x in xrange(len(G))]
    for i in xrange(0, len(G)):
        if visited[i] == False:
            dfs(G, i)
    
    return components