P = 51
Q = 5
e = 7
N = P*Q #255
QN = (P-1)*(Q-1) #200
print ("P= ", P, "Q= ", Q)
print ("N= ", N, "QN= ", QN)

# QN = a*e + b
# 200 = 28*7 + 4
def nwd(QN,e):
	iterasi = []
	while (e!=0):
		a = int(QN/e)
		b = QN%e
		setring = QN, '=',a,'*',e,'+',b
		QN = e
		e = b
		iterasi.append(setring)
	return iterasi

nwd(QN,e)
print ("Panjangan iterasi = ", len(nwd(QN,e)),'\n')

print ("Euclidean Algorithm:")
for x in range (len(nwd(QN,e))):
	print (nwd(QN,e)[x])
print ("\nExtended Euclidean Algorithm:")
iterasi2 = []
for x in range (len(nwd(QN,e))-1):
	setring2 = nwd(QN,e)[(len(nwd(QN,e))-2)-x][6], '=', nwd(QN,e)[(len(nwd(QN,e))-2)-x][0], '-', nwd(QN,e)[(len(nwd(QN,e))-2)-x][2], '*', nwd(QN,e)[(len(nwd(QN,e))-2)-x][4]
	iterasi2.append(setring2)
#	print (iterasi2[x])
print (iterasi2[0])
print (iterasi2[1])
print (iterasi2[2])
