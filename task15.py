def reverse_lookup(d,v):
	l = []	
	for k in d:
		if d[k] == v:
			l +=[k]
	return l

def hist(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d


hist = hist("hangover")
k=reverse_lookup(hist,2)
print(k)
