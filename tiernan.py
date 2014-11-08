G = []; N = 0; P = []; H = []; k = 0
P.append(k)

def EC1(seq):
    global G,N,H
    G = seq
    N = len(G)
    H = [[] for x in xrange(N)]
    EC2()

def EC2():
    global k
    canExpand = True
    while (canExpand == True):
        possible_expansions = []
        for j in xrange(0, len(G[P[k]])):
            if ((G[P[k]][j] not in P) and (G[P[k]][j] not in H[P[k]]) and (G[P[k]][j] > P[0]) and (G[P[k]][j] not in possible_expansions)):
                possible_expansions.append(G[P[k]][j])
        if len(possible_expansions) == 0:
            canExpand = False
            EC3()
        else:
            P.append(possible_expansions[0])
            k = k + 1

def EC3():
    if P[0] in G[P[k]]:
        print "Cycle in", P
    EC4()

def EC4():
    global k
    if k == 0:
        EC5()
    else:
        H[P[k]] = []
        H[P[k - 1]].append(P[k])
        P.pop()
        k = k - 1;
        EC2()

def EC5():
    if P[0] != N - 1:
        P[0] = P[0] + 1
        k = 0
        H = [[] for x in xrange(N)]
        EC2()