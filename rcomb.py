import math

def combination(cycles, r):
	all_picked_cycles = []
	nodes_in_cycles = set(sum(cycles, []))
	n = len(cycles)
	s = []
	for i in xrange(0, r):
		s.append(i)
	
	for i in xrange(1, C(n,r)):
		m = r - 1
		max_val = n - 1
		while (s[m] == max_val):
			m = m - 1
			max_val = max_val - 1

		s[m] = s[m] + 1

		for j in xrange(m + 1, r):
			s[j] = s[j-1] + 1

		picked_cycles = []
		for i in s:
			picked_cycles.append(cycles[i])
		picked_nodes = set(sum(picked_cycles, []))

		if (len(nodes_in_cycles) == len(picked_nodes)):
			all_picked_cycles.append(picked_cycles)

	return all_picked_cycles

def C(n, r):
	return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

# def factorial(n):
# 	if n <= 1:
# 		return 1
# 	else:
# 		return n * factorial(n - 1)

#print combination([[0, 5], [1, 5], [2, 5], [3, 6, 8, 7, 9], [0, 4, 6, 10, 2, 5], [1, 4, 6, 10, 2, 5], [2, 4, 6, 10]], 3)