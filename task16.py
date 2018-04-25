def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key)
		#inverse[val].append[key]
	return inverse

def hist(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d


hist = hist("Romil.")
k = invert_dict(hist)
print(k)
