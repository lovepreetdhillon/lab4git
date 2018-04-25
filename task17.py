import time
def fibonacci(n):
	if (n==0):
		return 0
	elif (n==1):
		return 1
	else:	
		return fibonacci(n-1) + fibonacci(n-2)

known = {0:0, 1:1}


def fibonacci2(n):
	if n is known:
		return known[n]
	res = fibonacci(n-1) + fibonacci(n-2)
	known[n] = res
	return res


start = time.time()
print(fibonacci(10))
t = time.time() - start
print("Original version time is %s seconds" %t)

start = time.time()
print(fibonacci2(10))
t = time.time() - start
print("New version time is %s seconds" %t)


