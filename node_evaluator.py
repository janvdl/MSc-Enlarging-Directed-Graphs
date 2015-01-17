import operator

def evaluate(G, cycles):
	node_dict = dict()
	node_score_dict = dict()
	nodes_in_cycles = sum(cycles, [])

	for node in xrange(0, len(G)):
		node_dict[node] = [0,0,0] #[Incoming, Outgoing, In Cycle?]

	for node in xrange(0, len(G)):
		#print "Evaluating node", node
		if len(G[node]) > 0:
			if node in node_dict:
				node_dict[node][1] = 1
				if node in nodes_in_cycles:
					node_dict[node][2] = 1
			else:
				node_dict[node] = [1,0,0]
		for adjacency in G[node]:
			#print "Evaluating node", node, "adjacency", adjacency
			if adjacency in node_dict:
				node_dict[adjacency][0] = 1
			else:
				node_dict[adjacency] = [1,0,0]

	for node in xrange(0, len(G)):
		node_score_dict[node] = sum(node_dict[node])

	return sorted(node_score_dict.items(), key=operator.itemgetter(1), reverse=True)