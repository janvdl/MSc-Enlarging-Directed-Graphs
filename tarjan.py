from copy import deepcopy

G = []
cycles = []

point_stack = []
marked = []
marked_stack = []

def tarjan(s, v):
    global cycles
    f = False
    point_stack.append(v)
    marked[v] = True
    marked_stack.append(v)
    for w in G[v]:
        if w < s:
            G[w] = []
        elif w == s:
            points_keeper = list(deepcopy(point_stack))
            if points_keeper not in cycles:
                cycles.append(points_keeper)
            f = True
        elif marked[w] == False:
            g = tarjan(s,w)
            f = f or g

    if f == True:
        while marked_stack[len(marked_stack) - 1] != v:
            u = marked_stack.pop()
            marked[u] = False
        marked_stack.pop()
        marked[v] = False

    point_stack.pop()
    return f

def entry_tarjan(G_):
    global G, cycles, marked, marked_stack, point_stack
    G = []
    cycles = []

    point_stack = []
    marked = []
    marked_stack = []

    G = deepcopy(G_)

    marked = [False for x in xrange(0, len(G_))]

    for i in range(len(G)):
        tarjan(i, i)
        while marked_stack:
            u = marked_stack.pop()
            marked[u] = False

    return cycles
