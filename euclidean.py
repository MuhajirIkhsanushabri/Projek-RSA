def nwd(a,b):
	while (b!=0):
		c=a%b
		a=b
		b=c
	return a

a = int(input("a = "))
b = int(input("b = "))
print (nwd(a,b))
