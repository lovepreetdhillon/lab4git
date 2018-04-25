
mylist= [1,2,3,4,5,6,7,8,9,10]
f = lambda x: x%3==0
l = filter(f,mylist)
for i in l:
	print(i)		

