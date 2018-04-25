import collections

def remove_duplicates(s):
	a=set(s)
	list=[]
	for i in a:
		list.append(i)
	return list

print(remove_duplicates([1,1,3,3,4,4,5,7,7,8,8]))
