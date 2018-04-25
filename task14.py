def hist(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d


hist = hist("Ganga")

def print_h(s):
	l = sorted(s.keys())
	for i in l:
		print(i, s[i])

	
print(print_h(hist))
