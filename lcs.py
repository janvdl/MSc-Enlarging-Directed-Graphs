from copy import deepcopy

# Longest common substring -> takes 2 cycles, compares the longest common node sequence
# http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring
def lcs(c1, c2):
    m = [[0] * (1 + len(c2)) for i in xrange(1 + len(c1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(c1)):
        for y in xrange(1, 1 + len(c2)):
            if c1[x - 1] == c2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return c1[x_longest - longest: x_longest]

def find_repeated_nodes(cycles):
    AnyFound = False
    repeated_nodes = []    
    for i in xrange(0, len(cycles)):
        for j in xrange(i, len(cycles)):
            if i != j:
                lcs_ = lcs(cycles[i], cycles[j])
                if len(lcs_) > 1 and lcs_ not in repeated_nodes:
                    repeated_nodes.append(lcs_)
                    AnyFound = True

    return sorted(repeated_nodes, key=len)

def remove_repeated_nodes(cycles, repeated_nodes):
    dict_val = 0;
    d = dict()
    for rep in repeated_nodes:
        firstOccur = True
        for cycle in cycles:
            if set(rep).issubset(set(cycle)):
                if firstOccur:
                    firstOccur = False
                else:
                    firstindex = cycle.index(rep[0])
                    dict_val = dict_val - 1
                    d[dict_val] = rep
                    cycle[firstindex] = dict_val
                    for node in rep:
                        if node in cycle:
                            cycle.remove(node)
    return cycles