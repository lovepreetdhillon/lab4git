def nested_sum(list):
	total=0
	for l in list:
		if (type(l) == type([])):
			total = total + nested_sum(l)
		else:
			total = total + l
	return total

n = [[2,3],[2,3],[5,7]]
print("Sum is:", nested_sum(n))
