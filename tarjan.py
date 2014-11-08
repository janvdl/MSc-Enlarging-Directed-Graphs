G = []
N = 0
cycles = []
points = []
marked_stack = []
marked = []

g = None
def tarjan(s, v, f):
    global g
    points.append(v)
    marked_stack.append(v)
    marked[v] = True

    for w in G[v][:]:
        if w < s:
            G[v].pop(G[v].index(w))
        elif w == s:
            cycles.append(points[:])
            f = True
        elif marked[w] == False:
            if f == g and f == False:
                f = False
            else:
                f = True
            tarjan(s, w, g)

    g = f
    if f == True:
        u = marked_stack.pop()
        while (u != v):
            marked[u] = False
            u = marked_stack.pop()
        marked[u] = False
    points.pop(points.index(v))

def entry_tarjan(G_):
    global G, N, marked, points
    G = G_
    N = len(G_)
    marked = [False for x in xrange(0,N)]
    for i in xrange(0,N):
        marked[i] = False
    for i in xrange(0,N):
        points = []
        tarjan(i,i, False)
        while (len(marked_stack) > 0):
            u = marked_stack.pop()
            marked[u] = False
    return cycles
