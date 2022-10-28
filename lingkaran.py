import math
r = float(input("Masukan Jari-jari : "))

luas = math.pi*(r*r)
keliling = 2*math.pi*r

print("Luas Lingkaran \t\t= ", luas)
print("Keliling Lingkaran\t= ", keliling)


print("Luas Lingkaran \t\t= ", format(luas, '.2f'))
print("Keliling Lingkaran \t= ", format(keliling, '.2f'))
