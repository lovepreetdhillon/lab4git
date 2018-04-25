import functools

def list_sum(l):
	print(l)	
	a=functools.reduce(lambda c, x: c + [c[-1] + x], l, [0])[1:]
	return a

e=list_sum([1,2,3,5,7])
print(e)
