print (chr(27) + "[2J")
print ("Metode Dekripsi RSA\n")
#print ("Ingin memakai data enkripsi sebelumnya?")

N = int(input('Masukkan nilai N : '))
e = int(input('Masukkan Public Key : '))
d = int(input('Masukkan Private Key: '))
p = input("Masukkan Plain Text : ")
data = list(pesan)
o = []
for x in range (len(data)):
	M = ord(data[x])
#	print ("Plain text dalam ascii", M)
	c = M**e%N
	o.append(c)
#	print ("Proses enkrip : c = ",M,"**",e,"%",N)
#	print ("Hasil enkrip = ", c)
print ("Cipher Text : ", o)
