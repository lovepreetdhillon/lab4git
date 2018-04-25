import functools
list = []
def evensum(list):
	tot = functools.reduce((lambda x,y:x+y),list)
	print("Sum of even nos. btw 100-500 is:", tot)
	
#def evensq(list):
#	for i in list:
#		list.append(i**2)
#	evensum(list)

def even(x,y):
	i = 1
	for i in range(x+1,y):
		if (i % 2 == 0):
			list.append(i**2)
	evensum(list)




even(0,10)
