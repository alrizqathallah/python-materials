# Python Materials

---

## Struktur dan Modularitas

Di bab ini, kita akan belajar bagaimana merapikan kode agar terlihat profesional, menyimpan banyak data sekaligus (seperti keranjang), dan mengajari program cara menghadapi *error*.

### Fungsi / Functions (Membungkus Kode)

**Fokus Pembelajaran**: Mengelompokan baris kode menjadi sebuah "resep" yang bisa dipanggil berkali-kali tanpa harus menulis ulang kodenya.

**Penjelasan Materi**:
Bayangkan kembali analogi robot pembuat kopi di BAB awal. Jika kita ingin robot itu membuat 3 cangkir kopi di waktu yang berbeda, sangat melelahkan jika harus menulis 8 langkah pembuatannya setiap kali kita butuh kopi.

Solusinya? kita ajarkan 8 langkah itu **satu kali** saja, lalu beri nama instruksi tersebut: `buat_kopi()`. Kapan pun kita butuh, kita tinggal memanggil nama instruksinya. Di Python, konsep ini disebut dengan **Fungsi** (atau *Function*).

Untuk membuat fungsi, kita menggunakan kata kunci `def` (singkatan dari *define* atau mendefinisikan), diikuti dengan nama fungsinya, tanda kurung `()`, dan titik dua `:`.

**Contoh:**

```Python
# 1 Mendefinisikan fungsi (mengajarkan resep)
def sapa_pelanggan():
  print("Selamat datang di Toko Maju Jaya!")
  print("Silakan lihat-lihat produk kami.")

# 2. Memanggil fungsi (Menyuruh komputer menjalankan resep)
sapa_pelanggan()
```

Jika kita tidak menulis `sapa_pelanggan()` dibagian bawah, komputer tidak akan mencetak apa-apa. `def` hanya sekedar "menyimpan resep", bukan membuatnya.

**Latihan:**
Mari kita buat sebuah fungsi sederhana. Dengan code editor:
1. Buat sebuah fungsi bernama `tampilkan_toko()` menggunakan `def`.
2. Di dalam fungsi tersebut, isi dengan tiga perintah `print()` yang menampilkan:
   1. Nama toko (bebas).
   2. Alamat toko.
   3. Slogan toko.
3. Di luar dan dibawah fungsi tersebut, panggil fungsinya sebanyak **dua kali**.

**Praktik:**

```Python
# Membuat fungsi (profil toko)
def tampilkan_toko():
  print("Bengs Shop")
  print("Lebak Bulus, Jakarta")
  print("Sesuai pesanan Anda!")

tampilkan_toko()
tampilkan_toko()
```

```Terminal
Bengs Shop
Lebak Bulus, Jakarta
Sesuai pesanan Anda!
Bengs Shop
Lebak Bulus, Jakarta
Sesuai pesanan Anda!
```

### Parameter dan Argumen (Memberi Masukan ke Fungsi)

**Fokus Pembelajaran:** Mengirimkan data spesifik ke dalam fungsi agar hasil dikeluarkan bisa berbeda-beda sesuai kebutuhan.

**Penjelasan Materi:**
Fungsi `tampilkan_toko()` yang telah dibuat sebelumnya bersifat **statis**. Artinya, dipanggil berapa kali pun, hasilnya akan selalu sama persis.

Di dunia nyata, kita ingin fungsi yang lebih **dinamis**. Bayangkan sebuha mesin **blender**. **Blender** adalah fungsinya (alat pemroses). Jika kita memasukkan mangga kedalam *blender*, keluarnya jus mangga. Jika kita memasukkan alpukat, keluarnya jus alpukat.

Dalam Pyhton, "buah" yang kita masukkan ke dalam fungsi disebut sebagai **Argumen**, dan "lubang penampung buah" di mesin *blender* disebut dengan **Parameter**.

Mari kita lihat contoh kodenya:

```Python
# 'nama' di dala kurung adalah Parameter (lubang penampung)
def sapa_pelanggan(nama):
  print("Halo, selamat datang,", nama)

# "Budi" dan "Siti" adalah Argumen (data yang dimasukkan)
sapa_pelanggan("Budi")
sapa_pelanggan("Siti")
```

```Terminal
Halo, selamat datang, Budi
Halo, selamat datang, Siti
```

Satu fungsi yang sama, tetapi bisa menghasilkan output yang berbeda tergantung data (argumen) apa yang kita masukkan!

Kita juga bisa memasukkan lebih dari satu parameter, cukup pisahkan dengan tanda koma `,`.

**Latihan:**
Mari kita buat sistem pemesanan sederhana untuk "Bengs Shop".

Di kode editor, buatlah kode dengan langkah berikut:
1. Buat sebuah fungsi bernama `proses_pesanan`.
2. Berikan dua parameter di dalam tanda kurungnya: `nama_pelanggan` dan `barang_dibeli`.
3. Di dalam fungsi tersebut, cetak sebuah kalimat menggunakan `print()`. Contoh kalimatnya: `"Pesanan [barang_dibeli] untuk Bapa/Ibu [nama_pelanggan] sedang disiapkan!"` (*Ganti tanda kurung siku dengan memanggil parameternya*).
4. Di luar fungsi, panggil `proses_pesanan` sebanyak **dua kali**.
    - Panggilan pertama, masukkan nama argumen dan barang "Kemeja".
    - Panggilan kedua, masukkan argumen nama teman dan barang "Sepatu".

**Praktik:**

```Python
# Membuat fungsi (proses_pesanan)
def proses_pesanan(nama_pelanggan, barang_dibeli):
  print("Pesanan,", barang_dibeli, "untuk Bapak/Ibu", nama_pelanggan, "sedang disiapkan!")

proses_pesanan("Alrizq", "Kemeja")
proses_pesanan("Rica", "Sepatu")
```

```Terminal
Pesanan, Kemeja untuk Bapak/Ibu Alrizq sedang disiapkan!
Pesanan, Sepatu untuk Bapak/Ibu Rica sedang disiapkan!
```

**Kesimpulan Materi:**
Parameter bertindak sebagai "jalur masuk" data ke dalam fungsi. Dengan parameter, kita bisa mendaur ulang satu blok untuk memproses berbagai macam data yang berbeda (argumen).

### Return (Mengembalikan Nilai)

**Fokus Pembelajaran:** Memahami perbedaan antar sekedar menampilkan hasil ke layar dengan memberikan hasil tersebut kembali ke sistem agar bisa diproses lebih lanjut.

**Penjelasan Materi:**
Sejauh ini, fungsi yang kita buat menggunakan `print()`. Ibaratnya, kita menyuruh asisten menghitung uang kasir, lalu asisten tersebut hanya berteriak dari jauh, "Totalnya seratus ribu!". Kita mendengarnya (tampil di layar), tapi kita tidak memegang uangnya.

Di dalam pemrograman sungguhan, kita jarang menggunakan `print()` di dalam sebuah fungsi pemrosesan. Kita menggunakan perintah `return`.

`return` ibarat asisten tersebut menghitung uang, lalu **menyerahkan uang tersebut ke tangan kita**. Karena uangnya sekarang ada di tangan kita, kita bisa menyimpannya kedalam sebuah laci (variabel), membaginya, atau membelanjakannya lagi.

Mari kita lihat perbedaannya:

**Fungsi dengan `print()` (Hanya berterika):**

```Python
def tambah_print(a, b):
  hasil = a + b
  print(hasil)

tambah_print(5, 10) # Langsung muncul 5 di layar. Selesai.
```

**Fungsi dengan `return` (Menyerahkan hasil):**

```Python
def tambah_return(a, b):
  hasil = a + b
  return hasil

# Karena fungsi ini 'menyerahkan' hasil, kita bisa menagkapnya dengan variabel
angka_baru = tambah_return(5, 10)

# Sekarang kita bisa memprosesnya lagi!
total_akhir = angka_baru * 2
print("Total akhir setelah dikali dua:", total_akhir)
```

Jika fungsi menggunakan `return`, proses di dalam fungsi tersebut akan langsung berhenti, dan nilainya akan dilemparkan kembali ke baris kode yang memanggilnya.

**Contoh Kasus Nyata:**
Sebagai *Software Engineer*, kita membuat fungsi perhitungan ongkos kirim. Hasil perhitungan ongkos kirim itu tidak bole sekedar di-`print` ke layar pembeli, tetapi harus di-`return` agar bisa ditambahkan dengan harga barang oleh sistem keranjang belanja.

**Latihan:**
Mari kita terapkan ini untuk sistem keuangan Bengs Shop.

Di kode editor, susunlah kode dengan langkah berikut:
1. Buat sebuah fungsi bernama `hitung_pajak`.
2. Berikan satu parameter: `harga_barang`.
3. Di dalam fungsi, buat variabel `pajak` yang isinya adalah `harga_barang` dikali `0.11` (ini adalah tarif PPN 11% di Indonesia. Gunakan titik untuk desimal di Python).
4. Gunakan perintah `return` untuk mengembalikan nilai dari variabel `pajak` tersebut.
5. Di luar fungsi, buat variabel bernama `pajak_sepatu`, lalu tugaskan pemanggilan fungsi `hitung_paka(200000)` ke dalam variabel tersebut.
6. Terakhir, gunakan `print()` untuk mencetak `pajak_sepatu`.

**Praktik:**

```Python
# Membuat fungsi (Perhitungan pajak barang)
def hitung_pajak(harga_barang):
  pajak = harga_barang * 0.11
  return pajak

pajak_sepatu = hitung_pajak(200000)

print(pajak_sepatu)
```

```Terminal
22000.0
```

Sebagai catatan kecil: perhatikan bahwa hasil diterminal adalah `22000.0` (ada tambahan `.0` di belakang). Ini terjadi karena kita mengalikan angka bulat (200000) dengan angka desimal (0.11). Komputer otomatis mengubah tipe data hasilnya menjadi **Float** (angka desimal). Ini adalah hal yang wajar dan sangat normal di Python.

**Kesimpulan Materi:** Perintah `return` digunakan untuk mengeluarkan hasil proses dari dalam fungsi agar nilainya bisa ditangkap oleh variabel lain dan digunakan kembali dalam perhitungan selanjutnya.

Sekarang program kita sudah memiliki perhitungan yang rapi. Namun, bagaimana jika toko kita memiliki ratusan barang? Tentu kiat tidak mungkin membuat variabel `barang1`, `barang2` hingga `barang100`. Mari kita selesaikan masalah tersebut.

### List (Menyimpan Banyak Data Sekaligus)

**Fokus Pembelejaran:** Memahami cara membuat, memanggil, dan menambahkan data ke dalam sebuah daftar.

**Penjelasan Materi:**
Sejauh ini, variabel yang kita gunakan ibarat sebuah kardus kecil yang hanya bisa menampung satu barang. Jika kita memasukkan barang baru, barang lama akan terbuang.

Di Python, kita memiliki tipe data bernama **List**. Bayangkan List seperti sebuah lemari laci vertikal. Kita bisa menyimpan banyak barang di dalamnya, dan setiap laci memiliki nomor urut agar kita mudah mencarinya.

Untuk membuat List, kita menggunakan **tanda kurung siku** `[]` dan memisahkan setiap datanya dengan tanda koma `,`.

**Contoh:**

```Python
# Membuat List
keranjang = ["Kemeja", "Sepatu", "Topi"]

# Menampilkan semua isi List
print(keranjang)
```

**Memanggil Satu Data Spesifik (Indeks):**
Ingatkan pembahasan tentang perulangan `for`? Komputer selalu memulai berhitung dari angka **0**. Nomor laci inilah yang disebutkan dengan **Indeks**.
- Indeks 0 = "Kemeja"
- Indeks 1 = "Sepatu"
- Indeks 2 = "Topi"

Jika kita hanya mengambil "Sepatu", kita menuliskan nama List-nya, diikuti kurung siku dan nomor indeksnya:

```Python
print(keranjang[1])
```

**Menambah Data Baru:**
Jika pembeli ingin memasukkan barang baru ke keranjang, kita tidak perlu membongkar List yang sudah ada. Kita bisa menggunakan perintah tambahan bernama `.append()` yang otomatis akan menaruh barang baru di laci paling bawah.

```Python
keranjang.append("Jaket")
```

**Latihan:**
Mari kita perhatikan cara mengelola daftar inventaris atau keranjang belanja ini.

Di kode editor, coba buatkan kode dengan langkah berikut:
1. Buat sebuah variabel bernama `daftar_belanja` yang merupakan list, dan isi dengan tiga buah teks (nama barang bebas).
2. Gunakan perintah `.append()` untuk menambahkan satu barang baru lagi ke dalam `daftar_belanja`.
3. Gunakan `print()` untuk mencetak **seluruh isi** List tersebut agar kita bisa melihat apakah barang barunya berhasil masuk.
4. Gunakan `print()` lagi untuk mencetak **hanya barang kedua** dari List. (*Ingat aturan hitungan komputer!*)

**Praktik:**

```Python
# Membuat List
daftar_belanja = ["Kaos", "Celana", "Sepatu"]

daftar_belanja.append("Topi")

print(daftar_belanja)

print(daftar_belanja[1])
```

```Terminal
['Kaos', 'Celana', 'Sepatu', 'Topi']
Celana
```

Kita berhasil menambahkan item baru ke dalam List dan memanggil data spesifik dengan memahami bahwa indeks ke-1 adalah barang kedua.

Sebagai *Software Engineer*, List adalah salah satu struktur data yang akan kita temui setiap hari, baik saat mengambil data dari database (seperti daftar produk atau daftar pengguna) maupun saat merender tampilan di aplikasi.

Sekarang kita sudah tahu cara menyimpan banyak barang, tetapi ada masalah baru: bagaimana jika kita perlu menampilkan semua barang tersebut satu per satu ke layar secara otomatis?

### Menggabungkan Perulangan dan List

**Fokus Pembelajaran:** Memerintahkan komputer untuk menelusuri isi sebuah daftar dari awal hingga akhir tanpa perlu memanggil nomor indeksnya satu per satu.

**Penjelasan Materi:**
Di materi tentang perulangan menggunakan `range(). Namun, ada cara yang jauh lebih elegan untuk melakukan perulangan pada sebuah List di Python.

Kita bisa menggunakan `for` untuk mengambil setiap barang di dalam kardus (List) satu per satu secara otomatis.

**Contoh:**

```Python
keranjang = ["Kemeja", "Sepatu", "Topi"]

for barang in keranjang:
  print("Saya membeli:", barang)
```

```Terminal
Saya membeli Kemeja
Saya membeli Sepatu
Saya membeli Topi
```

**Bagaimana ini bekerja?**
- Kata `barang` di situ hanyalah seubah **variabel sementara**. Kita bisa menamainya apa saja (seperti `item`, `x`, atau `produk`).
- Perintah `for barang in keranjang:` secara harfiah berarti: "Untuk setiap barang yang ada di dalam keranjang, lakukan instruksi di bawah ini secara bergantian."
- Komputer akan otomatis berhenti ketika semua isi laci sudah habis diproses. Kita tidak perlu lagi menghitung jumlah lacinya.

**Latihan:**
Mari kita praktikan gabungan konsep ini.
Di kode editor, buatlah kode dengan langkah berikut:
1. Buat List `karyawan` yang berisi tiga nama karyawan.
2. Gunakan perulangan `for` utnuk memproses List tersebut.
3. Di dalam perulangan, cetak kalimat sapaan, misalnya: `"Selamat pagi, [nama_karyawan]! Selamat bekerja."` (*Ganti bagian kurung siku dengan nama dari List*).

**Praktik:**

```Python
karyawan = ["Alrizq", "Athallah", "Sulung"]

for nama in karyawan:
  print("Selemat pagi", nama, "!", "Selemat bekerja.")
```

```Terminal
Selemat pagi Alrizq ! Selemat bekerja.
Selemat pagi Athallah ! Selemat bekerja.
Selemat pagi Sulung ! Selemat bekerja.
```

**Tips Ala Software Engineer (Bonus):**
Pernahkah kita menyadari ada spasi ekstra sebelum tanda seru di hasil terminal sebelumnya (`Alrizq !`)? Itu terjadi karena saat kita memisahkan teks dan variabel dengan tanda koma `,` di dalam `print()`, Python secara otomatis menyisipkan spasi di antara mereka.

Untuk membuat kalimat yang lebih rapi, para *Engineer* modern biasanya menggunakan fitur bernama **f-string** (Format String). Caranya, letakkan huruf `f` sebelum tanda kutip pembuka, lalu masukkan variabel kita kedalam kurung kurawal `{}` langsung di dalam teksnya.

Contoh:

```Python
print(f"Selamat pagi {nama}! Selamat bekerja.")
```

Hasilnya akan menjadi: `Selamat pagi Alrizq! Selamat bekerja.` (Tanpa spasi sebelum tanda seru). Kita bisa mencoba fitur ini di latihan-latihan selanjutnya!

**Kesimpulan Materi:** Perulangan `for` dapat digabungkan dengan List utnuk menelusuri dan memproses setiap data di dalam daftar secara otomatis dari awal hingga akhir.

Mari kita lanjutkan ke tipe data terakhir selebelum kita membuat *Mini Project* BAB 2.

### Dictionary (Menyimpan Data Berpasangan "Key-Value Pair")

**Fokus Pembelejaran:** Memahami cara menyimpan data yang memiliki label khusu (seperti nama dan nomor telepon), bukan sekedar urutan angka.

**Penjelasan Materi:**
List (menggunakan kurung siku `[]`) sangat bagus untuk menyimpan daftar barang yang berurutan. Namun, bagaimana jika kita ingin menyimpan sebuah kontak telepon? Jika menggunakan List, kita hanya mengingat urutan: indeks 0 adalah nama, indeks 1 adalah nomornya. Ini sangat membingungkan jika datanya banyak.

Di sinilah kita menggunaakn **Dictionary** (Kamus).
Dictionary menggunakan **kurung kurawal** `{}`. Alih-alih menggunakan nomor indeks (0, 1, 2), Dictionary menggunakan sistem **Kunci dan Nilai** (*Key* & *Value*).

Bayangkan sebuah kamus bahasa: Anda mencari kata (Kunci) untuk menemukan artinya (Nilai).

**Contoh:**

```Python
# Membuat Dictionary
kontak_guru = {
  "Pak Budi": "0812345678",
  "Bu Siti": "0898765432"
}

# Memanggil data spesifik (menggunakan Kuncinya, bukan indeks angka)
print(kontak_guru["Pak Budi"])
```

Jika dijalankan, komputer akan mencetak `"0812345678"`. Jauh lebih mudah dipahami daripada `kontak_guru[0]`, bukan?

**Menambahkan Data Baru ke Dictionary:**
Caranya sangat mudah, cukup sebutkan nama kamusnya, tulis Kunci barunya di dalam kurung siku, dan masukkan Nilainya menggunakan tanda sama dengan `=`.

```Python
kontak_guru["Pak Andi"] = "0855511122"

print(kontak_guru)
```

**Latihan:**
Mari kita mulai menyicil logika untuk *Mini Project* kita nanti.

Di kode editor, coba buatkan kode dengan langkah berikut:

1. Buat sebuah variabel bernama `data_diri` yang merupakan Dictionary (gunakan kurung kurawal `{}`).
2. Isi Dictionary tersebut dengan tiga pasang data (Kunci dan Nilai):
    - Kunci `"nama"`, isinya nama kita.
    - Kunci `"pekerjaan"`, isinya `"Software_Engineer"`.
    - Kunci `"domisili"`, isinya kota tempat tinggal kita.
3. Cetak hanya **kota domisili** kita dengan cara mengambil kunci dari Dictionary tersebut.
4. (*Tantangan*) Tambahkan satu dat baru ke dalam `data_diri`, yaitu `"hobi"` dengan nilai hobi kita, lalu cetak **keseluruhan** isi Dictionary tersebut.

**Praktik:**

```Python
data_diri = {
  "nama": "Alrizq Athallah",
  "pekerjaan": "Software Engineer",
  "domisili": "Jakarta",
}

print(data_diri["domisili"])

data_diri["hobi"] = "Belajar"

print(data_diri)
```

```Terminal
Jakarta
{'nama': 'Alrizq Athallah', 'pekerjaan': 'Software Engineer', 'domisili': 'Jakarta', 'hobi': 'Belajar'}
```

Tanpa sadar kita menggunakan "koma ekstra" (trailling comma) di akhir baris `"domisili": "Jakarta"`. Di dunia industri, ini adalah praktik penulisan kode yang sangat baik karena memudahkan kita jika ingin menambahkan data baru di baris berikutnya nanti.

**Kesimpulan Materi:** Dicitionary menyimpan data menggunakan sistem Kunci dan Nilai. Ia sangat berguna untuk menyimpan data yang berlabel spesifik, seperti profil pengguna atau kontak telepon, sehingga kita tidak perlu repot mengingat urutan angka indeks seperti pada List.

Sekarang, mari kita masuk ke materi terkahir di BAB 2 sebelum kita mengerjakan *Mini Project*.

### Try / Except (Mengantisipasi Masalah)

**Fokus Pembelajaran:** Mengajari komputer cara menangani masalah agar program tidak mati mendadak (*crash*) saat terjadi kesalahan.

**Penjelasan Materi:**
Sebagai *Software Engineer*, kita harus berasumsi bahwa pengguna bisa saja melakukan kesalahan. Misalnya, program meminta angka, tetapi pengguna mengetik huruf. Atau program mecari data "Budi" di buku telepon, padahal nama tersebut belum didaftarkan.

Jika hal itu terjadi, Python akan panik, memunculkan teks merah panjang (pesan *Error*), dan program kita akan langsung mati saat itu juga.

Untuk mencegah hal ini, kita menggunakan sistem pengamanan yang disebut **Try** dan **Except**.

- `try`: *"Coba jalankan blok kode ini."*
- `except`: *"Jika terjadi error di dalam blok 'try', jangan matikan programnya. Jalankan blok kode ini sebagai gantinya."*

**Contoh Sederhana (Pembagian dengan Nol):**
Di matematika, kita tidak bisa mebagi angka dengan 0. Jika kita memaksa komputer melakukannya, ia akan *error*.

```Python
# Try & Except (mengantisipasi kesalahan)
try:
  hasil = 10 / 0
  print(hasil)
except:
  print("Sistem medeteksi kesalahan: Anda tidak bisa membagi dengan angka nol!")
```

Jika kita menjalankan kode di atas, program tidak akan *crash*. Ia akan dengan tenang menampilkan pesan peringatan yang ramah.

**Latihan:**
Mari kita gunakan Dictionary yang sudah kita pelajari untuk menguji fitur pengaman ini.
Jika kita mencoba mencetak sebuah Kunci dan Dictionary yang belum pernah kita buat, Python akan menghasilkan `KeyError` dan program akan mati.

Di kode editor, buatlah kode dengan urutan berikut:
1. Buat Dictionary `buku_telepon` yang harus berisi satu kontak `{"Andi": "08111"}`.
2. Buat blok `try:`. Jangan lupa titik dua dan pastikan baris bawahnya menjorok ke dalam !
3. Di dalam blok `try`, perintahkan komputer untuk mencetak kontak yang **tidak ada**, misalnya: `print(buku_telepon["Budi"])`.
4. Di bawahnya, sejajar dengan `try`, buat blok `except:`.
5. Di dalam blok `except`, perintahkan komputer untuk mencetak pesan ramah: `"Maaf, nama tersebut tidak ada di buku telepon."`

**Praktik:**

```Python
# Latihan
buku_telepon = {
  "Andi": "08111",
}

try:
  print(buku_telepon["Budi"])
except:
  print("Maaf, nama tersebut tidak ada di buku telepon.")
```

```Terminal
Maaf, nama tersebut tidak ada di buku telepon.
```

**Kesimpulan Materi:** Menggunakan `try` and `except` adalah cara standar di industri (*Best Practice*) untuk memastikan program tetap berjalan stabil meskipun pengguna melakukan kesalahan atau ada data yang tidak ditemukan.

### Mini Project BAB 2: Aplikasi Buku Telepon Digital

**Skenario:**
Kita diminta untuk membangun mesin logika sederhana di balik sebuah aplikasi kontak telepon. Sistem ini harus bisa menambahkan kontak baru secara dinamis dan memiliki fitur pencarian yang aman (tidak *crash* jika nama yang dicari tidak ada).

**Tugas:**
Coba buat *file* bari di kode editor (misalnya `buku_telepon.py`) dan susun program dengan alur logika berikut:
1. **Siapkan Penyimpanan Utama:**
    - Buat sebuah Dictionary kosong bernama `kumpulan_kontak = {}` di baris paling atas. Ini akan menjadi tempat kita menyimpan data.
2. **Fitur Tambah Kontak (Fungsi):**
    - Buat fungsi bernama `tambah_kontak` yang menerima dua parameter: `nama` dan `nomor`.
    - Di dalam fungsi ini, tambahkan `nama` sebagai Kunci dan `nomor` sebagai Nilai ke dalam Dictionary `kumpulan_kontak`.
    - Cetak pesanan keberhasilan menggunakan f-string, contoh: `"Kontak {nama} berhasil ditambahkan!"`
3. **Fungsi Cari Kontak (Fungsi + Pengaman):**
    - Buat fungsi bernama `cari_kontak` yang menerima satu parameter: `nama_dicari`.
    - Di dalam fungsi ini, gunakan blok `try` dan `except`.
    - Di dalam blok `try`, perintahkan program untuk mencetak nomor telepon dari `nama_dicari` tersebut. Gunakan f-string agar rapi: `"Nomor telepon {nama_dicari} adalah {kumpulan_kontak[nama_dicari]}".
    - Di dalam blok `except`, cetak pesan peringatan: `"Maaf, kontak {nama_dicari} tidak ditemukan."`
4. **Uji Coba Sistem (Pemanggilan Fungsi):**
    - Di luar fungsi, panggil `tambah_kontak()` dua kali memasukkan nama dan nomor siapa saja.
    - Panggil `cari_kontak()` untuk mencari nama yang **sudah** kita tambahkan.
    - Panggil `cari_kontak`untuk mencari nama yang **belum** kita tambahkan, guna menguji pengaman `except` kita berfungsi.

**Tantangan Tambahan (Opsional):**
Bisakah kita membuat satu fungsi tambahan bernama `lihat_semua_kontak()` yang menggunakna perulangan `for` untuk menelusuri Dictionary `kumpulan_kontak` dan menampilkan semua nama yang tersimpan? (*Petunjuk: Kita bisa menggunakan perulangan `for nama in kumpulan_kontak:`)

**Praktik:**

```Python
# Fitur Tambah Kontak
kumpulan_kontak = {}

def tambah_kontak(nama, nomor):
  kumpulan_kontak[nama] = nomor

# Fitur Cari Kontak + Pengaman
def cari_kontak(nama_dicari):
  try:
    print(f"Nomor telepon {nama_dicari} adalah {kumpulan_kontak[nama_dicari]}")
  except:
    print(f"Maaf, kontak {nama_dicari} tidak ditemukan.")
    
# Uji Coba Sistem
tambah_kontak("Bengs", "081287855393")

cari_kontak("Bengs")

cari_kontak("Alrizq")

# Fungsi Tambahan
def lihat_semua_kontak():
  for nama in kumpulan_kontak:
    print(nama)
    
lihat_semua_kontak()
```

```Terminal
Nomor telepon Bengs adalah 081287855393
Maaf, kontak Alrizq tidak ditemukan.
Bengs
```