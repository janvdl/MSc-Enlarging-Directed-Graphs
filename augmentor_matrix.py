from math import *

def augment(G, seq):
	G = destroyDuplicates(G)
	newseq = []

	#Count the row and column totals
	row_array = countRowColTotals(G)[0]
	col_array = countRowColTotals(G)[1]

	#Count the zeroes in the row and column totals - these are the nodes with no incoming/outgoing edges
	zeroes_count_in_rows = 0
	zeroes_count_in_cols = 0
	zero_rows_index = []
	zero_cols_index = []

	#the sequence length is important as destroyDuplicates(G) already enlarges the graph and adds zeroes
	for i in xrange(0, len(seq)):
		if row_array[i] == 0:
			zero_rows_index.append(i)
			#print "Row", i, "has a zero"
		if col_array[i] == 0:
			zero_cols_index.append(i)
			#print "Col", i, "has a zero"

	# for i in xrange(0, len(G)):
	# 	if row_array[i] == 0:
	# 		zeroes_count_in_rows += 1
	# 	if col_array[i] == 0:
	# 		zeroes_count_in_cols += 1

	#We need dummy columns for the zeroes. Determine the maximum between the row zeroes and column zeroes
	#dummy_cols_needed = max(zeroes_count_in_rows, zeroes_count_in_cols)
	#basically expand by the same number that destroyDuplicates expanded by
	dummy_cols_needed = len(zero_rows_index) #len(G) - len(seq)
	#print "dummy_cols_needed x 2 = ", dummy_cols_needed
	dummies_index = [x for x in xrange(len(seq), len(seq) + (dummy_cols_needed))]

	#Create a new sequence array to contain dummies
	newseq = [[0,0] for x in xrange(0, len(seq) + (dummy_cols_needed))]
	for i in xrange(0, len(seq)):
		newseq[i] = seq[i]

	#Create new bigger matrix and copy the old matrix into it
	G_new = expandGraph(G, dummy_cols_needed)

	#Reverse it to ensure that pop() will return the original first node in each list
	zero_rows_index.reverse()
	#zero_cols_index.reverse()
	dummies_index.reverse()

	print zero_rows_index
	print zero_cols_index
	print dummies_index

	#While there's some node without an incoming/outgoing edge
	while (len(zero_rows_index) > 0 or len(zero_cols_index) > 0 or len(dummies_index) > 0):

		if (len(zero_rows_index) > 0):
			first = zero_rows_index.pop()
		else:
			first = getSomeNode(G[:], row_array[:], col_array[:], [])

		if (len(zero_cols_index) > 0):
			last = zero_cols_index.pop()
		else:
			last = getSomeNode(G[:], row_array[:], col_array[:], [first])

		if (len(dummies_index) > 0):
			mid = dummies_index.pop()
		else:
			mid = getSomeNode(G[:], row_array[:], col_array[:], [first, last])

		#Create the connection
		G_new[first][mid] = 1
		G_new[mid][last] = 1
		print "creating connection", first, mid, last
		newseq[first] = seq[first]
		newseq[last] = seq[last]
		newseq[mid] = [seq[last][1], seq[first][0]]

	return [G_new, newseq]

def destroyDuplicates(G):
	#Count the row and column totals
	row_array = countRowColTotals(G)[0]
	col_array = countRowColTotals(G)[1]

	extraZeroesNeeded = 0

	row_indices_counts = dict()
	col_indices_counts = dict()
	for i in xrange(0, len(row_array)):
		if row_array[i] > 1:
			row_indices_counts[i] = row_array[i]
		if col_array[i] > 1:
			col_indices_counts[i] = col_array[i]

	for key in row_indices_counts:
		while row_indices_counts[key] > 1:
			for i in reversed(xrange(0, len(G))):
				if G[key][i] == 1:
					G[key][i] = 0
					row_indices_counts[key] = row_indices_counts[key] - 1
					extraZeroesNeeded += 1
					break


	#Refresh the row and column totals
	row_array = countRowColTotals(G)[0]
	col_array = countRowColTotals(G)[1]

	extraZeroesNeeded = 0

	row_indices_counts = dict()
	col_indices_counts = dict()
	for i in xrange(0, len(row_array)):
		if row_array[i] > 1:
			row_indices_counts[i] = row_array[i]
		if col_array[i] > 1:
			col_indices_counts[i] = col_array[i]

	for key in col_indices_counts:
		while col_indices_counts[key] > 1:
			for i in reversed(xrange(0, len(G))):
				if G[i][key] == 1:
					G[i][key] = 0
					col_indices_counts[key] = col_indices_counts[key] - 1
					extraZeroesNeeded += 1
					break
	return G
	#return expandGraph(G, extraZeroesNeeded)

def expandGraph(G, numberOfNodesExtra):
	#Create new bigger matrix and copy the old matrix into it
	print "expanding the graph by nodes: ", numberOfNodesExtra

	G_new = [[0 for x in xrange(0, len(G) + numberOfNodesExtra)] for x in xrange(0, len(G) + numberOfNodesExtra)]
	for i in xrange(0, len(G)):
		for j in xrange(0, len(G)):
			G_new[i][j] = G[i][j]

	return G_new

def countRowColTotals(G):
	#Count the row and column totals
	row_array = [0 for x in xrange(0, len(G))]
	col_array = [0 for x in xrange(0, len(G))]

	for i in xrange(0, len(G)):
		for j in xrange(0, len(G)):
			if G[i][j] == 1:
				row_array[i] += 1
				col_array[j] += 1

	return [row_array, col_array]

def getSomeNode(G, row_array, col_array, exclude_list):
	r_arr = row_array[:]
	c_arr = col_array[:]
	min_ = 99999999;
	index = None
	for i in xrange(0, len(G)):
		if r_arr[:][i] < min_ and r_arr[:][i] != 0 and i not in exclude_list:
			min_ = r_arr[:][i]
			index = i

	return index
