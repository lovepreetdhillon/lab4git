def has_duplicates(str):
	for i in range(0,len(str)):
		if(str[i]==str[i+1]):
			return True
		else:
			return False

print(has_duplicates([1,1,2,2,3,3,5]))
