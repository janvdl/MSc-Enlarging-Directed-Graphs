names_us = ['Adam', 'Bob', 'Carol', 'David', 'Eddie', 'Frank', 'George', 'Harry',
         'Ike', 'Jim', 'Kenny', 'Larry', 'Mary', 'Nancy', 'Oliver', 'Peter',
         'Quincy', 'Roger', 'Sam', 'Thomas', 'Uwe', 'Vincent', 'William',
         'Xavier', 'Yogi', 'Zachary']
numbers = ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9',
            'v10', 'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'v17',
            'v18', 'v19', 'v20', 'v21', 'v22', 'v23', 'v24', 'v25']

def get_graphviz_names(seq):
    names = names_us
    number_of_nodes = len(seq)
    s = 'digraph G {'
    for i in range(0, number_of_nodes):
        s = s + names[i] + '_L' + str(seq[i][0])+ '_R' + str(seq[i][1]) + ';'
        for j in range(0, number_of_nodes):
                if seq[i][0] == seq[j][1]:
                    s = s + names[i] + '_L' + str(seq[i][0])+ '_R' + str(seq[i][1]) \
                    + '->' + names[j] + '_L' + str(seq[j][0])+ '_R' + str(seq[j][1]) + ';'
    s = s + '}'
    return s

def get_graphviz(seq):
    names = numbers
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