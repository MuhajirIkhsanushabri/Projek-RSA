import math
import random

#Menentukan variabel RSA
def cekPrima(num):
	if num>1:
		for i in range (2,num):
			if num%i == 0: #Bilangan bisa dibagi bilangan lain
				return 0
		else: #Bilangan Prima
			return 1
	else: #Bilangan minus, 0 atau 1
		return 0
def inputPQ():
	global P
	global Q
	x = int(input("P : "))
	y = int(input("Q : "))
	cekPrima(x)
	cekPrima(y)
	if cekPrima(x)==1 and cekPrima(y)==1:
		P = x
		Q = y
	else:
		print ("P atau Q bukan bilangan prima!\n")
		return inputPQ()
def pubKey(y):
	global e
	print ("\nMenentukan Public Key (e)")
	for x in range(2, y):
		if math.gcd(x,QN) == 1:
			e_avail.append(x)
	print ("Nilai e yang bisa digunakan: ", e_avail)
	answer = input("\nIngin me-random nilai e? (y/n): ")
	if answer == 'y':
		e = int(random.choice(e_avail))
	else:
		e = int(input("Pilih nilai e yang tersedia di list di atas: "))
	print ("\nNilai e yang digunakan : ", e)
	return e
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, x, y = egcd(b%a, a)
		return (g, y - (b // a) * x, x)
def pvtKey(a, QN):
	global d
	if a > 0:
		d = a
	else:
		d = QN + a
	print ("d = ", d)
	return d

P = 0
Q = 0
inputPQ()

N = P*Q
QN = (P-1)*(Q-1)
e = 0
e_avail = []
d = 0

print ("Generated N = ",N)
print ("Generated QN = ", QN)
pubKey(QN)
egcd(e, QN)
pvtKey(egcd(e, QN)[1], QN)

######################################################

print ("\n###\n\nMetode Enkripsi RSA")
print ("Dari sisi pengirim mengetahui:")
print ("N = ", N, "e = ", e)
pesan = input("Masukkan Plain Text : ")
data = list(pesan)
a = []
b = []
for x in range (len(data)):
	M = ord(data[x])
	c = M**e%N
	cc = chr(c)
	a.append(c)
	b.append(cc)
bb = ''.join(b)

print ("Cipher Text dalam ASCII: ", a)
print ("Cipher Text dalam Char: ", bb)

######################################################

print ("\n###\n\nMetode Dekripsi RSA")
print ("Dari sisi penerima mengetahui:")
print("N = ", N, "\ne = ", e, "\nd = ", d, "\nCipher Text = ", bb)

decrypted = []
for x in range (len(bb)):
	MM = ord(bb[x])
	decrypt = MM**d%N
	decryptChr = chr(decrypt)
	decrypted.append(decryptChr)
decryptedStr = ''.join(decrypted)

print ("Pesan yang sudah di dekrip: ", decryptedStr)
