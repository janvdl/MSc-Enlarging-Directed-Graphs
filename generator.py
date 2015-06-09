import random
from random import randint

number_of_nodes = 0
avg_min = 9
avg_max = 11
sd_min = -2
sd_max = 2
shoes = []

def getseed():
    #return 123789456
    #return 170888264
    #return 923462908
    #return 482367498
    #return 532499987
    #=====For appendices=====
    #return 586015916
    #return 273100389
    #return 513577387
    # return 912644420
    return 422223344
    # return 550095080
    # return 444662587
    # return 664788481
    # return 461731130
    # return 735161101
    # return 475887106
    # return 664469990
    # return 965309708
    # return 456777039
    # return 222892396
    # return 809723839
    # return 508456853
    # return 393236722
    # return 568828692
    # return 346854015

##Generate Single Shoe Pair
def get_shoe_pair():
    #Assume average foot size is between 9-11
    #Add +-2 for standard deviation
    sd = 0
    while sd == 0:
        sd = randint(sd_min,sd_max)
    left = randint(avg_min,avg_max) + sd

    #Make the right foot bigger/smaller than the left by 1-2 sizes
    sd = 0
    while sd == 0:
        sd = randint(sd_min,sd_max)
    right = left + sd

    return [left, right]

##Generate some number of random shoe pairs
def get_random_seq(nodes_):
    random.seed(getseed())
    temp_shoes = []
    for i in range(0, nodes_):
        temp_shoes.append(get_shoe_pair())
    return sorted(temp_shoes)

##Generate Adjacency List
def get_graph(seq):
    N = len(seq)
    G = [[] for x in xrange(N)]
    for i in range(0, N):
        for j in range(0, N):
            if seq[i] != None and seq[j] != None:
                if seq[i][0] == seq[j][1]:
                    G[i].append(j)
    return G

def get_matrix(seq):
    N = len(seq)
    G = [[0 for x in xrange(N)] for x in xrange(N)]
    for i in range(0, N):
        for j in range(0, N):
            if seq[i] != None and seq[j] != None:
                if seq[i][0] == seq[j][1]:
                    G[i][j] = 1
    return G
