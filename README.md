<h2>  Program Python Menghitung Luas & Keliling Lingkaran  </h2>


**DAFTAR ISI**
> - [Rumus Luas & Keliling Lingkaran](Rumus_Luas_&_Keliling_Lingkaran)
> - [Penjelasan](PENJELASAN)
> - 


Rumus Luas & Keliling Lingkaran

Luas     = π × r²
Keliling = 2 x π × r

<img src="img/flowchart.PNG" alt="Flowchart" width="300" height="600">


**PENJELASAN :**
Berikut adalah penjelasan source code program setiap barisnya :

1.  Buat fungsi terlebih dahulu.(Dalam Python, sebuah fungsi didefinisikan menggunakan kata kunci def).
    def luas_lingkaran():
	jari_jari = int(input("Masukan jari-jari lingkaran: "))
	luas = 22/7 * (float(jari_jari) ** 2)
	print("Hasilnya adalah : ", format(luas,'.2f'))
	return luas
2.  def keliling_lingkaran():
	jari_jari2 = int(input("Masukan jari-jari lingkaran: "))
	keliling = 2 * 22/7 * float(jari_jari2)
	print("Hasilnya adalah : ", format(keliling,'.2f'))
	return keliling
3.  while True:
	print("====== SELAMAT DATANG DI PROGRAM LINGKARAN ======")
	print("Berikut adalah menu yang tersedia:")
	print("1. Mencari luas Lingkaran")
	print("2. Mencari keliling Lingkaran")
	print("3. Batal")
	option = input("Option 1-2 : ")
	if option == "1":
		print("Anda Pilih Menu 1: ")
		luas_lingkaran()
	elif option == "2":
		print("Anda Pilih Menu 2:")
		keliling_lingkaran()
	elif option == "3":
		break
	else: 
		print("Keyword Anda Salah!!, Anda bisa coba lagi!!")


Luas Lingkaran          =  40.72
Keliling Lingkaran      =  22.62
Dengan penggunaan fungsi format(luas,’.2f’) akan menghasilkan 2 angka pecahan saja.


