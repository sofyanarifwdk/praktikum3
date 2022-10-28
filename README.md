<h2>  <b>Program Python Menghitung Luas & Keliling Lingkaran</b>  </h2>


**DAFTAR ISI**
> - [Rumus Luas & Keliling Lingkaran](Rumus_Luas_&_Keliling_Lingkaran)
> - [Flowchart Menghitung Luas & Keliling Lingkaran](Flowchart_Menghitung_Luas_&_Keliling_Lingkaran)


Rumus Luas & Keliling Lingkaran

Luas     = π × r²
Keliling = 2 x π × r

Nilai Phi yang akan kita gunakan adalah 3.14
r merupakan jari-jari lingkaran

Phi merupakan nilai konstanta di matematika sementara jari-jari merupakan jarak antara titik pusat dengan tepi lingkaran. Sebetulnya ada rumus lain untuk menghitung keliling lingkaran yaitu dengan menggunakan diameter, tapi pada kasus ini kita cukup menggunakan jari jari lingkaran saja.

Flowchart Menghitung Luas & Keliling Lingkaran

<img src="img/flowchart.PNG" alt="Flowchart" width="300" height="600">


<img src="img/alur.PNG" alt="Flowchart" width="600" height="200">
<img src="img/output.PNG" alt="Flowchart" width="1500" height="100">

**PENJELASAN :**
*   Program diatas saya mengimport modul math yang sudah di sediakan oleh python. Fungsinya supaya saya dapat menyertakan nilai phi yang sudah tersedia dalam modul tersebut dengan perintah math.pi jika kita coba mencetak fungsi tersebut maka akan menghasilkan nilai 3.14

*   Selanjutnya kita memerlukan nilai jari-jari (r) yang nantinya akan di masukan oleh pengguna pada layar console. Kita menggunakan fungsi input() yang nilainya di konversi ke tipe data float (bilangan riil). Ingat bahwa fungsi input() akan menganggap semua nilai inputan bertipe string, sehingga kita perlu melakukan konversi ke tipe yang diinginkan.

*   Ketika kita sudah mendapat nilai phi dan jari-jari selanjutnya kita bisa menghitung luas dan keliling sesuai dengan rumus-nya masing-masing (lihat pada baris ke 3 & 4).

*   Selanjutnya kita tampilkan hasilnya dengan fungsi print(). sintak \t merupakan karakter espace yang berfungsi untuk membuat tab. dalam kasus ini agar sejajar karakter sama dengan (=) nya.

*   Jika dilihat hasil luas dan keliling lingkaran mempunyai angka pecahan yang cukup banyak, untuk mengambil 2 angka pecahan saja kita pakai fungsi format() seperti berikut:

<img src="img/output1.PNG" alt="Flowchart" width="600" height="200">

Dengan penggunaan fungsi format(luas,’.2f’) akan menghasilkan 2 angka pecahan saja.
