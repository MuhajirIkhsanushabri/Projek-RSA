import math
import random

P = 0
Q = 0

def cekPrima(num):
	if num>1:
		for i in range (2,num):
			if num%i == 0:
#				print (num, "bukan bilangan prima")
#				print (i, "kali", num//i, "=", num)
				return 0
			else: #Return True jika bilangan prima
				return 1
	else:
#		print(num, "bukan bilangan prima")
		return 0

def inputPQ():
	global P
	global Q
	x = int(input("P : "))
	y = int(input("Q : "))
	cekPrima(x)
	cekPrima(y)

#	print ("x = ", cekPrima(x))
#	print ("y = ", cekPrima(y))

	if cekPrima(x)==1 and cekPrima(y)==1:
		P = x
		Q = y
	else:
		print ("P atau Q bukan bilangan prima!\n")
		return inputPQ()

inputPQ()
#print ("P = ", P)
#print ("Q = ", Q)
N = P*Q
QN = (P-1)*(Q-1)
e = 0

print ("Generated N = ",N)
print ("Generated QN = ", QN)


e_avail = []

def pubKey(y): #y = QN
	print ("\nMenentukan Public Key")
	for x in range(2, y):
		if math.gcd(x,QN) == 1:
			e_avail.append(x)
	print ("Nilai e yang bisa digunakan: ", e_avail)
	answer = input("\nIngin me-random nilai e? (y/n): ")
	if answer == 'y':
		e = random.choice(e_avail)
	else:
		e = input("Pilih nilai e yang tersedia di list di atas: ")
	print ("\nNilai e yang digunakan : ", e)
	return e

pubKey(QN)
