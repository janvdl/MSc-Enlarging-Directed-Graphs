from math import *

def augment(G):
	row_array = [0 for x in xrange(0, len(G))]
	col_array = [0 for x in xrange(0, len(G))]

	for i in xrange(0, len(G)):
		for j in xrange(0, len(G)):
			if G[i][j] == 1:
				row_array[i] += 1
				col_array[j] += 1

	zeroes_count_in_rows = 0
	zeroes_count_in_cols = 0
	zero_rows_index = []
	zero_cols_index = []
	for i in xrange(0, len(G)):
		if row_array[i] == 0:
			zeroes_count_in_rows += 1
			zero_rows_index.append(i)
		if col_array[i] == 0:
			zeroes_count_in_cols += 1
			zero_cols_index.append(i)

	dummy_cols_needed = max(zeroes_count_in_rows, zeroes_count_in_cols)
	dummies_index = [x for x in xrange(len(G), len(G) + dummy_cols_needed)]

	G_new = [[0 for x in xrange(0, len(G) + dummy_cols_needed)] for x in xrange(0, len(G) + dummy_cols_needed)]
	for i in xrange(0, len(G)):
		for j in xrange(0, len(G)):	
			G_new[i][j] = G[i][j]

	zero_rows_index.reverse()
	zero_cols_index.reverse()
	dummies_index.reverse()

	while (len(zero_rows_index) > 0 or len(zero_cols_index) > 0 or len(dummies_index) > 0):

		if (len(zero_rows_index) > 0):
			first = zero_rows_index.pop()
		else:
			first = getSomeNode(G[:], row_array[:], col_array[:])
			print first

		if (len(zero_cols_index) > 0):
			last = zero_cols_index.pop()
		else:
			last = getSomeNode(G[:], row_array[:], col_array[:])

		if (len(dummies_index) > 0):
			mid = dummies_index.pop()
		else:
			mid = getSomeNode(G[:], row_array[:], col_array[:])

		if first != None and mid != None:
			G_new[first][mid] = 1
		if mid != None and last != None:
			G_new[mid][last] = 1

	return G_new

def getSomeNode(G, row_array, col_array):
	r_arr = row_array[:]
	c_arr = col_array[:]
	min_ = 99999999;
	index = None
	for i in xrange(0, len(G)):
		if r_arr[:][i] < min_ and r_arr[:][i] != 0:
			min_ = r_arr[:][i]
			index = i

	return index