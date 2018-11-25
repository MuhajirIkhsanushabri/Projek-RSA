print (chr(27) + "[2J")
print ("Dari sisi penerima menentukan:\n")
print ("1. Nilai P dan Q, merupakan bilangan prima")
print ("Dengan syarat P tidak sama dengan Q")
P = int(input('P : '))
Q = int(input('Q : '))
N = P*Q #RSA Modulus
print ("Didapatkan N = P*Q = ", N)
QN = (P-1)*(Q-1) #Eulers Toitent Function
print ("Dan juga QN = (P-1)*(Q-1) = ", QN)
print ("\n2. Public Key (e)")
print ("Dengan syarat 1<e<QN")
e = int(input("e : "))

######################################################

print ("\n###\n\nMetode Enkripsi RSA")
print ("Dari sisi pengirim mengetahui:")
#N = int(input('Masukkan nilai N : '))
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
print ("Dari sisi penerima menghitung nilai d (Private Key)")
print ("Berdasarkan perhitungan menggunakan Algoritma Euclidean")
print ("e.d = 1%QN\n")
d = int(input("Masukkan nilai d : "))
print("Diketahui N = ", N)
print("Diketahui e = ", e)
print("Diketahui Cipher Text = ", bb)
decrypted = []
for x in range (len(bb)):
	MM = ord(bb[x])
	decrypt = MM**d%N
	decryptChr = chr(decrypt)
	decrypted.append(decryptChr)
decryptedStr = ''.join(decrypted)

print ("Pesan yang sudah di dekrip: ", decryptedStr)
