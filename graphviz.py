from math import *
from copy import deepcopy

names_us = ['Adam', 'Bob', 'Carol', 'David', 'Eddie', 'Frank', 'George', 'Harry',
         'Ike', 'Jim', 'Kenny', 'Larry', 'Mary', 'Nancy', 'Oliver', 'Peter',
         'Quincy', 'Roger', 'Sam', 'Thomas', 'Uwe', 'Vincent', 'William',
         'Xavier', 'Yogi', 'Zachary', 'Dummy', 'Dummy', 'Dummy', 'Dummy', 'Dummy',' Dummy', 'Dummy', 'Dummy', 'Dummy', 'Dummy']
names_za = ['Monde', 'John', 'Hendrik', 'Kefentse', 'David', 'Yoosuf', 'Kopano', 'Mark',
         'Maheshini', 'Ian', 'Sipho', 'Thabo', 'Mary', 'Nancy', 'Oliver', 'Peter',
         'Quinton', 'Roger', 'Sam', 'Thomas', 'Uwe', 'Vincent', 'William',
         'Xavier', 'Yogi', 'Zachary']
numbers = ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9',
            'v10', 'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'v17',
            'v18', 'v19', 'v20', 'v21', 'v22', 'v23', 'v24', 'v25']

def get_graphviz_names(seq):
    names = names_us
    number_of_nodes = len(seq)
    s = 'digraph G {size="5"; center=true;{'
    for i in range(0, number_of_nodes):
        s = s + '"' + str(i + 1) + ": " + names[i] + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']";\n'
        for j in range(0, number_of_nodes):
                if seq[i][0] == seq[j][1]:
                    s = s + '"' + str(i + 1) + ": " + names[i] + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']"' \
                    + '->' + '"' + str(j + 1) + ": " + names[j] + ' [' + str(seq[j][0])+ ',' + str(seq[j][1]) + ']";\n'
    s = s + '}}}'
    return s

def get_graphviz(seq):
    number_of_nodes = len(seq)
    s = 'digraph G {'
    for i in range(0, number_of_nodes):
        s = s + 'v' + str(i) + ';'
        for j in range(0, number_of_nodes):
                if seq[i][0] == seq[j][1]:
                    s = s + 'v' + str(i) + '->' + 'v' + str(j) + ';'
    s = s + '}'
    return s

def get_graphviz_from_graph(G):
    s = 'digraph G {'
    for i in xrange(0, len(G)):
        s = s + 'v' + str(i) + ';'
        if len(G[i]) > 0:
            for j in G[i]:
                s = s + 'v' + str(i) + '->' + 'v' + str(j) + ';'
    s = s + '}'

    return s

def get_graphviz_from_matrix(G, seq, length):
    names = deepcopy(names_us)
    s = 'digraph G {'
    for i in xrange(0, len(G)):
        name_i = names[i]
        if i >= length:
            name_i = "Dummy"

        s = s + '"' + str(i + 1) + ": " + name_i + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']";\n'

        for j in xrange(0, len(G)):
            name_j = names[j]
            if j >= length:
                name_j = "Dummy"
            if G[i][j] == 1:
                s = s + '"' + str(i + 1) + ": " + name_i + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']"' \
                + '->' + '"' + str(j + 1) + ": " + name_j + ' [' + str(seq[j][0])+ ',' + str(seq[j][1]) + ']";\n'

    s = s + '}'

    return s

def get_graphviz_names_from_graph(G, seq, length):
    names = names_us
    s = 'digraph G {center=true;{'
    for i in xrange(0, len(G)):
        name_i = names[i]
        if i >= length:
            name_i = "Dummy"
        s = s + '"' + str(i + 1) + ": " + name_i + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']";\n'
        if len(G[i]) > 0:
            for j in G[i]:
                name_j = names[j]
                if j >= length:
                    name_j = "Dummy"

                s = s + '"' + str(i + 1) + ": " + name_i + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']"' \
                + '->' + '"' + str(j + 1) + ": " + name_j + ' [' + str(seq[j][0])+ ',' + str(seq[j][1]) + ']";\n'
    #Rank nodes
    for i in xrange(0, len(G)):
        name_i = names[i]
        if i >= length:
            name_i = "Dummy"
        if float(i) % 2 == 0:
            s = s + "{rank=same;" + '"' + str(i + 1) + ": " + name_i + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']";'
        else:
            s = s + '"' + str(i + 1) + ": " + name_i + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']"}\n'
    #END Rank nodes
    s = s + '}}}'
    return s

def get_graphviz_names_from_graph_compromising(G, seq, length, other_nodes):
    names = deepcopy(names_us)
    names_2 = names
    for i in xrange(0, len(other_nodes)):
        names_2[i] = names[other_nodes[i]]
    names = names_2
    print "Names:", names
    s = 'digraph G {center=true;{'
    for i in xrange(0, len(G)):
        name_i = names[i]
        if i >= length:
            name_i = "Dummy"
        s = s + '"' + str(i + 1) + ": " + name_i + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']";\n'
        if len(G[i]) > 0:
            for j in G[i]:
                name_j = names[j]
                if j >= length:
                    name_j = "Dummy"

                s = s + '"' + str(i + 1) + ": " + name_i + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']"' \
                + '->' + '"' + str(j + 1) + ": " + name_j + ' [' + str(seq[j][0])+ ',' + str(seq[j][1]) + ']";\n'
    #Rank nodes
    for i in xrange(0, len(G)):
        name_i = names[i]
        if i >= length:
            name_i = "Dummy"
        if float(i) % 2 == 0:
            s = s + "{rank=same;" + '"' + str(i + 1) + ": " + name_i + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']";'
        else:
            s = s + '"' + str(i + 1) + ": " + name_i + ' [' + str(seq[i][0])+ ',' + str(seq[i][1]) + ']"}\n'
    #END Rank nodes
    s = s + '}}}'
    return s

def get_cycle_latex(cycles):
    names = deepcopy(names_us)
    for cycle in cycles:
        s = "\\item{"
        for node in cycle:
            if cycle.index(node) == len(cycle) - 1:
                s = s + "(" + str(node + 1) + ": " + names[node] + ")"
            else:
                s = s + "(" + str(node + 1) + ": " + names[node] + ")" + " $\\rightarrow$ "
        s = s + "}"
        print s
