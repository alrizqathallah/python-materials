# Python Materials

---

## Pondasi Pemrograman

---

### Berpikir seperti komputer

**Fokus Pembelajaran**: Memahami bagaimana memecahkan sebuah perintah menjadi instruksi langkah demi langkah yang logis (Algoritma).

Komputer pada dasarnya adalah mesin yang sangat patuh, tetapi sama sekali tidak memiliki inisiatif. Ia tidak bisa memahami perintah yang ambigu atau berasumsi layaknya manusia. Untuk membuat komputer bekerja, kita harus memberikan instruksi yang sangat spesifik, terurut dan logis. Rangkain instruksi inilah yang dalam dunia pemrograman disebut dengan **Algoritma**.

Mari kita gunakan analogi kehidupan nyata: **Memasak Mi Instan**.
Jika kita menyuruh taman, "Tolong buatkan mi," mereka langsung mengerti. Namun, jika kita menyuruh komputer (atau robot), kita harus merinci secara detail:
1. Siapkan panci
2. Isi panci dengan 400ml air.
3. Taruh panci diatas kompor.
4. Nyalakan kompor.
5. Tunggu hingga air mendidih.
6. Masukan mi kedalam air.

Jika kita melewati langkah ke-4("Nyalakan Kompor"), komputer akan tetap menaruh panci disana dan menunggu selamanya karena air tidak akan pernah mendidih. Komputer akan gagal menyelesaikan tugasnya (mengalami *error*) karena instruksi yang diberikan tidak lengkap.

**Latihan**:
Mari berlatih menyusun algoritma sebelum kita menyentuh kode Python. Bayangkan kita harus memberikan instruksi kepada sebuah robot pelayanan untuk **membuat secangkir kopi manis panas**.

Langkah-langkah membuat kopi:
1. Siapkan cangkir dan satu saset kopi.
2. Buka saset kopi dan tuangkan bubuk kopi kedalam cangkir.
3. Ambil panci dan masukan air sebanyak cangkir kopi.
4. Taruh panci berisi air diatas kompor dan nyalakan kompor.
5. Tunggu air sampai mendidih dan matang.
6. Setelah itu tuangkan air tersebut kedalam cangkir yang sudah terisi bubuk kopi.
7. Aduk kopi hingga merata.
8. Kopi siap disajikan

Mari kita lihat susunan instruksi dari "kacamata" sebuah komputer atau robot yang sangat kaku. Terdapat dua celah logika yang menarik disini:

1. **Lupa mematikan kompor**: Di langkah ke-6, kita mneyuruh robot menuangkan air mendidih, tetapi tidak ada instruksi untuk mematikan kompor setelahnya. Robot akan membiarkan kompor menyela terus-menerus! Dalam dunia pemrograman, lupa menghentikan suatu proses bisa menyebabkan program berjalan tanpa henti (*infinite loop*) atau menguras memori komputer.

2. **Asumsi "Kopi Manis"**: Tujuan awal kita adalah membuat secangkir kopi manis panas. Jika saset yang kita maksud adalah kopi campur gula (3-in-1), maka aman. Tapi jika itu kopi hitam pekat, robot tidak akan berinisiatif menambahkan gula kedalamnya karena kita tidak memberikan instruksi "tambahkan satu sendok gula". Komputer sama sekali tidak memiliki inisiatif.

Menemukan celah logika seperti ini dan memperbaikinya adalah kegiatan sehari-hari seorang *Software Engineer*, yang biasa kita sebut sebagai proses **Debugging** (mencari dan membasmi "kutu" atau kesalahan dalam kode).

**Kesimpulan Materi**:
Komputer membutuhkan algoritma (langkah-langkah) yang 100% detail, spesifik, dan tanpa asumsi. Jika program kita mengalami *error*, itu bukan karena komputernya bodoh, melainkan karena ada instruksi kita yang kurang tepat atau terlewat.

---

### Persiapan

**Fokus Pembelajaran**: Mengenal dan menyiapkan perangkat lunak yang dibutuhkan untuk menulis dan menjalankan kode Python.

Sebagai calo *Software Engineer*, kita tidak bisa menulis kode hanya dengan membayangkannya. Kita membutuhkan "bengkel" kerja. Untuk memprogram dalam bahasa Pyton, kita wajib memiliki dua alat utama:

1. **Python Interpreter (Penerjemah)**:
   Komputer pada dasarnya hanya mengeri bahasa mesin, yaitu deretan angka `0` dan `1`. Ia tidak mengerti bahasa inggris, bahasa Indonesia, apalagi bahasa Python. Oleh karena itu, kita perlu menginstal program khusus dari situs resmi Python. Program ini bertugas membaca kode Python yang kita tulis, lalu menerjemahkannya ke bahasa mesin agar komputer bisa memprosesnya.

2. **Code Editor**:
   Ini adalah tempat kita mengetik instruksi atau kode. Secara teknis, kita bisa mengetik kode di program bawaan seperti *Notepad*, tetapi itu sangat menyiksa karena teksnya hanya berwarna hitam putih dan tidak ada pengingat jika kita salah ketik. Di dunia industri, kita menggunakan perangka lunak yang disebut IDE (*Integrated Development Environment*). Salah satu yang paling populer dan gratis adalah **Visual Studio Code (VS Code)**. VS Code akan memberi warna berbeda pada setiap kata kunci dan membantu melengkapi kode kita secara otomatis.

**Alternatif**:
Di era modern ini, adal solusi jika kita tidak ingin atau belum bisa menginstal apa pun di komputer kita. Kita bisa menggunakan **Google Colab**. Ini ibarat *Google Docs* tetapi khusu untuk menjalankan kode Python. Semuanya berjalan secara *online* di dalam peramban (*browser*) kita, sehingga kita bisa langsung melai mengetik kode detik ini juga!

---

### Kode Pertama

**Fokus Pembelajaran**: Memerintahkan komputer untuk berbicara atau menampilkan informasi ke layar.

**Penjelasan Materi**:
Di dalam bahasa Python, instruksi paling dasar yang akan paling sering kita gunakan adalah `print()`.

Bayangkan `print()` sebagai sebuah megafon. Apa pun yang kita letakkan di dalam tanda kurun `()` akan "diteriakkan" (ditampilkan) oleh komputer ke layar kita.

Namun, ada satu aturan ketat dari komputer: Jika kita ingiin menampilkan (huruf, kata, atau kalimat), teks tersebut wajib diapit oleh tanda kutip ganda (`" "`) atau tanda kutip tunggal (`' '`).

Dalam dunia pemrograman, teks yang diapit oleh tnada kutip ini disebut sebagai **String**. Tanda kutip berfungsi sebagai pemisah untuk memberi tahu komputer: "*Hei, ini cuma teks biasa yang harus kamu tampilkan, ini bukan kode perintah rahasia.*" Jika kita lupa memakai tanda kutip, komputer akan bingung (*error*).

**Langkah Praktis di VS Code:**

1. Buka aplikasi VS Code kita.

2. Buat berkas (*file*) baru dan simpan dengan nama `latihan1.py`.
   (*Catatan: Akhiran `.py` wajib digunakan untuk memberi tagu komputer bahwa berkas tersebut berisi instruksi bahasa Python*).

**Latihan**:
Berdasarkan penjelasan diatas, jika instruksi untuk menampilkan kata Halo adalah `print("Halo")`, coba kita tuliskan disini (dan juga di VS Code kita) kode persis yang harus diketik untuk menyuruh komputer menampilakan kalimat berikut:

`Halo dunia, saya siap menjadi Software Engineer!`

Setelah kita mengetiknya di VS Code, coba jalankan kodenya (biasanya dengan menekan tombol 'Play' di pojok kanan atas layar VS Code). Coba tuliskan kode kita dan apa hasil yang muncul!

```python
print("Halo dunia, saya siap menjadi Software Engineer!")
```

```terminal
Halo dunia, saya siap menjadi Software Engineer!
```

**Kesimpulan Materi:** Perintah `print()` adalah cara kita menyuruh komputer berbicara, dan teks biasa harus selalu diapit oleh tanda kutip agar dikenali sebagai *String* (teks) oleh komputer.

---

### Variabel

Menyimpan informasi.

**Fokus Pembelajaran:** Memahami cara komputer menyimpan dan memanggil kembali sebuah data.

Di program sebelumnya, kita langsung menyuruh komputer menampilkan teks. Namun, bagaimana jika kita ingin komputer mengingat nama kita, lalu memanggilnya berkali-kali di bagian program yang lain? Disinilah kita menggunakan **Varibel**.

Bayangkan variabel sebagai sebuah kardus kosong. Kita bisa memasukan barang apa saja ke dalamnya, lalu kita menempelkan label nama di luar kardusnya agar tidak lupa isinya.

Contoh di Python:

```Python
nama = "Budi"
```

Di sini, kita membuat kardus (variabel) berlabel `nama`, dan kita memasukan teks `"Budi"` ke dalamnya. Tanda samas dengan (`=`) di sini bukan berarti "sama dengan" seperti matematika, melainkan perintah **Memasukkan nilai** (dari kanan ke kiri).

Jika ingin melihat isi kardus tersebut, kita cukup memanggil labelnya:

```Python
print(nama)
```

*Catatan penting:* Perhatikan bahwa saat kita memanggil variabel di dalam `print()`, kita **tidak** menggunakan tanda kutip. Jika kita menggunakan tanda kutip `print("nama")`, komputer akan mencetak kata "nama", bukan isinya ("Budi").

**Latihan Anda:**
Coba buat sebuah kode di VS Code dengan dua langkah ini:

1. Buat sebuah variabel bernama `cita_cita` dan masukkan teks `Software Engineer` ke dalamnya.

2. Gunakan perintah `print()` untuk menampilkan isi dari variabel `cita_cita` tersebut ke layar.

**Praktik:**

```Python
cita_cita = "Software Engineer"

print(cita_cita)
```

```Terminal
Software Engineer
```

Sifat utama dari variabel adalah nilainya bisa diubah. Jika dibaris paling bawah ditambahkan kode `cita_cita = "Tech Lead"` lalu mencetaknya lagi dengan `print(cita_cita)`, komputer akan menampilkan "Tech Lead". Komputer mengeksekusi kode dari atas ke bawah dan selalu mengingat isi yang paling baru.

**Praktik:**

```Python
cita_cita = "Software Engineer"

print(cita_cita)

cita_cita = "Tech Lead"

print(cita_cita)
```

```Terminal
Tech Lead
```

**Kesimpulan Materi:**
Variabel adalah wadah menyimpan data. Untuk melihat isinya, kita memanggil nama variabel tersebut di dalam `print()` tanpa menggunakan tanda kutip.

---

### Tipe Data

Sejauh ini, kita memasukkan teks ke dalam variabel menggunakan tanda kutip. Teks ini desebut dengan tipe data **String**. Namun, komputer memiliki perlakuan berbeda jika kita ingin menyimpan angka untuk dihitung.

Untuk angka, **tidak boleh** menggunakan tanda kutip:
- `"10"` = String/Teks biasa. Komputer membacanya sebagai huruf '1' dan '0'. Jika kita menjumlahkan '10' + '10', hasilnya adalah '1010'.
- `10` = Angka bulat. Dalam pemrograman, ini disebut tipe data **Integer**. Jika kita menjumlahkan `10 + 10`, hasilnya adalah `20`.

**Contoh Kasus Nyata:**
Mari kita buat program kasir mini untuk menghitung total pesanan kopi:

```Python
harga_kopi = 15000
jumlah_beli = 2
total_bayar = harga_kopi * jumlah_beli # Tanda bintang (*) digunakan untuk perkalian di Python

print(total_bayar)
```

**Latihan:**
Mari kita buat program kalkulator umur yang otomatis. Buat kode baru di VS Code dengan mengikuti urutan logika berikut:
1. Buat variabel `tahun_lahir` dan isi dengan tahun lahir (gunakan angka, tanpa tanda kutip).
2. Buat variabel `tahun_sekarang` dan isi dengan angka `2026`.
3. Buat variabel `umur` yang isinya adalah hasil operasi pengurangan `tahun_sekarang` dikurangi `tahun_lahir`. (*Petunjuk: Gunakan tanda `-` untuk pengurangan*).
4. Tampilkan isi varibel `umur` menggunakan `print()`.

**Praktik:**

```Python
tahun_lahir = 1998
tahun_sekarang = 2026
umur = tahun_sekarang - tahun_lahir

print(umur)
```

```Terminal
28
```

**Kesimpulan Materi:** Komputer membedakan antara teks (*String*) yang diapit tanda kutip dan angka (*Integer*) yang ditulis tanpa tanda kutip. Tipe data angka dapat diproses menggunakan operasi matematika dasar seperti `+`(tambah), `-`(kurang), `*`(kal) dan `/`(bagi).

---

### If/Else (Percabangan/Conditional)

**Fokus Pembelajaran:** Melatih komputer untuk membuat keputusan secara otomatis berdasarkan kondisi tertentu.

**Penjelasan Materi:**
Dalam dunia nyata, kita bertindak berdasarkan situasi. *"Jika cuaca hujan, maka saya bawa payung. Jika tidak, saya pakai kacamata hitam."*

Komputer juga bisa melakukan ini menggunakan perintah `if` (jika) dan `else` (jika tidak). Mari kita lihat contoh kodenya:

```Python
cuaca = "hujan"

if cuaca == "hujan":
   print("Jangan lupa bawa payung!")
else:
   print("Pakai kacamata hitam ya!")
```

Ada tiga aturan yang sangat penting dalam penulisan logika ini di Python:
1. **Tanda Titik Dua (`:`):** Setiap kali menulis kondisi `if` atau `else`, baris tersebut **wajib** diakhir dengan tanda titik dua `:`. Ini pertanda bahwa ada instruksi lanjutan di bawahnya.
2. **Menjorok ke Dalam (*Indentation*):** Perhatikan bahwa perintah `print()` tidak sejajar dengan `if`. Ia menjorok ke dalam (biasanya 4 ketukan spasi atau 1 kali tombol Tab). Di Python, posisi menjorok ini wajib. Ini cara Python tahu bahwa `print()` tersebut adalah bagian dari perintah `if`. Jika posisinya sejajar, program akan *error*.
3. **Tanda Sama Dengan Ganda (`==`):** Ingat, satu tanda `=` berarti kita **memasukkan nilai** ke dalam variabel (seperti memasukkan barang ke kardus). Sedangkan dua tanda `==` adalah **pertanyaan perbandingan**, yang artinya *"Apakah nilainya sama peris dengan... ?"*

**Contoh Kasus Nyata:**
Sebagai *Software Engineer*, kita sering diminta membuat sistem validasi. Misalnya, sistem pendaftaran yang mengecek apakah pengguna sudah cukup umur atau belum.

Selain `==`, kita juga bisa menggunakan perbandingan angka lainnya, seperti:
- `>` (Lebih besar dari)
- `<` (Lebih kecil dari)
- `>=` (Lebih besar atau sama dengan)

**Latihan:**
Mari kita kembangkan program kalkulator umur yang telah dibuat sebelumnya. Kita akan membuat program penentu kelayakan membuat KTP (Kartu Tanda Penduduk), dimana syaratnya adalah minilam berusia 17 tahun.

Cobalah tulis kode di VS Code dengan urutan berikut:
1. Gunakan kembali kode perhitungan umur sebelumnya (yang menghasilkan `umur = 28`).
2. Tambahkan logika `if` untuk mengecek: Jika `umur`lebih besar atau sama dengan (`>=`) `17`.
3. Jika kondisi itu benar, cetak: `"Selamat, Anda sudah boleh membuat KTP!"`.
4. Gunakan `else` untuk kondisi sebaliknya, lalu cetak: `"Maaf, Anda belum cukup umur."`.

**Prakti:**

```Python
tahun_lahir = 1998
tahun_sekarang = 2026
umur = tahun_sekarang - tahun_lahir

if umur >= 17:
   print("Selamat, Anda sudah boleh membuat KTP!")
else:
   print("Maaf, Anda belum cukup umur.")
```

```Terminal
Selamat, Anda sudah boleh membuat KTP!
```

**Kesimpulan Materi:** Komputer dapat mengambil keputusan otomatis menggunakan `if` dan `else` berdasarkan perbandingan logika.

### Loop (Perulangan)

**Fokus Pembelajaran:** Memerintahkan komputer untuk melakukan tugas yang sama bekali-kali secara otomatis.

**Penjelasan Materi:**
Bayangkan kita dihukum oleh guru untuk menulis sebuah kalimat sebanyak 100 kali di buku. Tentu sangat melelahkan. Bagi komputer, mengulang tugas ribuan kali bisa dilakukan dalam hitungan milidetik tanpa mengeluh, dan kita tidak perlu menulis perintah `print()` sebanyak 100 baris.

Di Python, kita menggunakan perintah `for` untuk melakukan perulangan yang jumlahnya sudah kita ketahui. Kita menggunakan bantuan `range()` untuk menentukan jumlah ulangannya.

Contoh:

```Python
for i in range(3):
   print("Kopi ke-", i)
```

Jika kode ini dijalankan, hasilnya adalah:

```Terminal
Kopi ke- 0
Kopi ke- 1
Kopi ke- 2
```

*Catatan penting:*
1. Sama seperti `if`, baris `for` wajib diakhiri dengan titik dua `:`.
2. Instruksi yang ingin diulang (`print`) wajib menjorok ke dalam (*Indentation*).
3. Komputer secara *default* selalu mulai berhitung dari angka **0**, bukan **1**. Jadi `range(3)` berarti menghitung 0, 1, dan 2 (totalnya ada 3 angka). Huruf `i` di situ adalah variabel sementara yang otomatis menyimpan angka urutan tersebut setiap kali putaran terjadi.

**Latihan:**
Sebagai persiapan sebelum kita membuat program kasi, mari kita pastikan kita menguasai perulangan ini.

Coba buat kode untuk mencetak kalimat `"Saya siap mengerjakan Mini Project!"` sebanyak **5 kali** menggunakan perintah `for`.

**Praktik:**

```Python
for i in range(5):
   print("Saya siap mengerjakan Mini Project!")
```

```Terminal
Saya siap mengerjakan Mini Project!
Saya siap mengerjakan Mini Project!
Saya siap mengerjakan Mini Project!
Saya siap mengerjakan Mini Project!
Saya siap mengerjakan Mini Project!
```

Dengan selesainya materi perlungan ini, kita telah menguasai seluruh pondasi dasar Materi 1: membuat variabel, membedakan tipe data, melakukan operasi matematika, membangun logik pengambilan keputusan (`if/else`), dan menjalankan perulangan (`for`).

## Mini Project Materi 1: Program Kasir Sederhana

**Skenario:**
Kita diminta membuat program kasir otomatis untuk sebuah kedai. Karena kita belum belajar cara mengambil *input* ketikan langsung dari pengguna saat program berjalan, kita akan memasukkan dtanya langsung ke dalam variabel di awal kode.

**Tugas:**
Coba buat sebuah *file* baru (misalnya `kasir.py`) dan susun program dengan alur logika berikut:
1. **Siapkan Data (Variabel & Tipe Data):**
   - Buat varibel `nama_barang` dan isi dengan teks nama barang apa saja.
   - Buat variabel `harga_satuan` dan isi dengan angka (misal: 15000).
   - Buat variabel `jumlah_beli` dan isi dengan angka.
   - Buat variabel `uang_pelanggan` dan isi dengan angka uang yang dibayarkan.
2. **Proses Hitung:**
   - Buat variabel `total_harga` yang menghitung perkalian `harga_satuan` dengan `jumlah_beli`.
3. **Logika Pembayaran (if/else):**
   - Cek apakah `uang_pelanggan` lebih besar atau sama dengan (`>=`) `total_harga`.
   - **Jika uangnya cukup:**
       - Hitung kembaliannya (uang pelanggan dikurangi total harga).
       - Cetak struk pembelian yang menampilkan nama barang, total harga, dan jumlah kembalian.
       - **Tantangan Perulangan:** Gunakan perulangan `for` untu, mencetak kalimat `"Terima kasih telah berbelanja!"` sebanyak **3 kali** dibagian paling bawah struk.
   - **Jika uangnya tidak cukup:**
       - Cetak pesan peringatan, misalnya: `"Maaf, uang Anda tidak cukup untuk membayar pesanan ini."`