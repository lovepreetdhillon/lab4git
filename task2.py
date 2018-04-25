import functools
list = []
def even(x,y):
	i = 1
	for i in range(x+1,y):
		if (i % 2 == 0):
			list.append(i)
	evensum(list)
	

def evensum(list):
	tot = functools.reduce((lambda x,y:x+y),list)
	print("Sum of even nos. btw 100-500 is:", tot)


even(100,500)
