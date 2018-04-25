import random

def has_duplicates(str):
	for i in range(0,len(str)):
		if(str[i]==str[i+1]):
			return True
		else:
			return False

def r_bdays(n):
	t =[]
	for i in range(n):
		bday = random.randint(1,365)
		t.append(bday)
	return t


def count(x,y):
	c = 0
	for i in range(y):
		t = r_bdays(x)
		if has_duplicates(t):
			c +=1
	return c


x = 23
y = 500
c = count(x,y)
print("Taking %s samples with %s students, there are %s samples which matches." %(y,x,c))
