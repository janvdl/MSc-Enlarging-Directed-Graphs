import math
from itertools import combinations
from copy import deepcopy

def combination(cycles, r):
	all_picked_cycles = []
	nodes_in_cycles = set(sum(cycles, []))
	all_combs = built_in_rcombs(cycles, r)
	for comb in all_combs:
		picked_nodes = set(sum(comb, []))

		if (len(nodes_in_cycles) == len(picked_nodes)):
		 	all_picked_cycles.append(comb)

	return all_picked_cycles

def C(n, r):
	return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

def built_in_rcombs(items, r):
	return list(combinations(items, r))

def custom_rcomb(items, r):
	indices = [x for x in xrange(0, len(items))]
	# print indices

	n = len(indices)
	s = []
	permuted_items = []
	for i in xrange(0, r):
		s.append(i)

	permuted_items.append([items[k] for k in s])
	for i in xrange(1, C(n,r)):
		# print "Entering iteration", i
		m = r - 1
		max_val = n - 1
		while (s[m] == max_val):
			m = m - 1
			max_val = max_val - 1

		s[m] = s[m] + 1

		for j in xrange(m + 1, r):
			s[j] = s[j-1] + 1

		temp_ = []
		for k in s:
			temp_.append(items[k])
		# print temp_
		permuted_items.append(temp_)

	return permuted_items

# def factorial(n):
# 	if n <= 1:
# 		return 1
# 	else:
# 		return n * factorial(n - 1)

#print combination([[0, 5], [1, 5], [2, 5], [3, 6, 8, 7, 9], [0, 4, 6, 10, 2, 5], [1, 4, 6, 10, 2, 5], [2, 4, 6, 10]], 3)

#print custom_rcomb([[0, 4, 3, 2, 5], [0, 4, 5], [2, 3], [6, 7], [0, 4, 1, 9], [0, 4, 3, 2, 1, 9], [6, 10, 8, 7]], 3)

#print C(3000, 2)
