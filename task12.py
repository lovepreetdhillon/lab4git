f = open('words.txt')

def create_dict():
	word = {}
	for l in f:
		w = l.strip()
		word[w] = w
	return word

print(create_dict())
