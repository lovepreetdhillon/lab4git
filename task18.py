def has_duplicates(str):
	return len(set(str)) < len(str)

print(has_duplicates([1,2,3,5]))
