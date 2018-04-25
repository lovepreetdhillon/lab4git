def middle(l):
	m = float(len(l))/2
	if m % 2 == 0:
		return l[int(m-1)],l[int(m)]
	else:
		if (int(m-0.5) == int(m)):
			return l[int(m)]
		else:
			return l[int(m-0.5)], l[int(m)]

k = middle([1,2,3,4,5])
i = []
i.append(k)
print(i)
