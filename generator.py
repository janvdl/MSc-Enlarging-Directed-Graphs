import random
from random import randint
#random.seed(123789456)
random.seed(123789465)

number_of_nodes = 0
avg_min = 9
avg_max = 11
sd_min = -2
sd_max = 2
shoes = []

##Generate Single Shoe Pair
def get_shoe_pair():
    #Assume average foot size is between 9-11
    #Add +-2 for standard deviation
    sd = 0
    while sd == 0:
        sd = randint(sd_min,sd_max);
    left = randint(avg_min,avg_max) + sd

    #Make the right foot bigger/smaller than the left by 1-2 sizes
    sd = 0
    while sd == 0:
        sd = randint(sd_min,sd_max);
    right = left + sd

    return [left, right]

##Generate some number of random shoe pairs
def get_random_seq(nodes_):
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