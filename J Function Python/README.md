# Funtion in Python

## Bagaimana Function Bekerja di Python?

Function adalah rangkaian kode yang dapat digunakan secara berulang.

Fungsi `print()` merupakan salah satu contoh yang sudah digunakan.

Fungsi lain yang dapat digunakan juga adalah `input()`

```Python
name = input('What is your name?')
print('Hello', name)
```

Penggunaan konversi tipe data (casting), juga menggunakan fungsi seperti `int()`.

```Python
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 
```

Di Python, jika pengguna ingin membuat fungsi yang umumnya seperti di bahas pemrograman lain, dapat menggunakan kata kunci `def` yang diikuti nama fungsi, parentheses `()` dan colon `:`.

Seperti contoh fungsi berikut:

```Python
def hello():
  print('Hello World')

hello()
```

untuk menggunakan fungsi tersebut, dapat dipanggil nama fungsi yang dibuat.

Berikut contoh penggunaan fungsi lebih jauh, untuk dimengerti secara kerja dan caranya.

```Python
def addition(a,b):
  print(a + b)

addition(1, 4)  # 5
```

atau hasil dari penjumlahan dapat ditampung dalam sebuah variabel baru.

```Python
price = 80.50
discount = 0.10

def calculate_total(p, d):
    # Menghitung harga setelah diskon
    final_price = p * (1 - d)
    
    # "Mengembalikan" nilai agar bisa disimpan di luar fungsi
    return final_price

# Memanggil fungsi dan MENYIMPAN hasilnya ke dalam variabel baru
hasil_belanja = calculate_total(price, discount)

# Sekarang kita bisa menggunakan variabel 'hasil_belanja' kapan saja
print(f"Tagihan yang harus dibayar adalah: Rp{hasil_belanja}")

# Contoh penggunaan ulang: jika bayar pakai uang 100
kembalian = 100 - hasil_belanja
print(f"Uang kembalian Anda: Rp{kembalian}")
```

*Parameter*: Adalah tombol atau slot pada mesin (misal: Slot Biji Kopi, Tombol Takaran Gula). Ini adalah "wadah kosong" yang menunggu diisi.

```Python
# 'nama' dan 'posisi' adalah PARAMETER
def sapa_karyawan(nama, posisi):
    print(f"Halo {nama}, selamat bekerja sebagai {posisi}!")
```

*Argumen*: Adalah benda nyata yang kamu masukkan (misal: Biji Arabika, 2 sendok gula). Ini adalah isi aslinya.

```Python
# "Budi" dan "Data Analyst" adalah ARGUMEN
sapa_karyawan("Budi", "Data Analyst")
```

*Return*: Adalah secangkir kopi yang keluar dari mesin. Kamu bisa membawa cangkir itu ke meja kerja atau memberikannya ke teman.

Return adalah perintah untuk mengirimkan hasil pemrosesan keluar dari fungsi. Tanpa return, fungsi hanya melakukan tugasnya lalu "diam" (hasilnya tidak bisa disimpan ke variabel lain).

```Python
# Parameter: gaji_pokok, bonus
def hitung_total_gaji(gaji_pokok, bonus):
    total = gaji_pokok + bonus
    return total # Mengirim hasil keluar

# Argumen: 5000000, 1500000
gaji_bulan_ini = hitung_total_gaji(5000000, 1500000)

# Karena ada RETURN, kita bisa mengolah hasilnya lagi
pajak = gaji_bulan_ini * 0.05
print(f"Gaji setelah pajak: {gaji_bulan_ini - pajak}")
```

LEGB adalah singkatan dari urutan pencarian nama variabel oleh Python: Local, Enclosing, Global, dan Built-in.

**Analogi Dunia Nyata: Mencari Barang di Kantor** 🏢
Bayangkan kamu sedang duduk di meja kerjamu di sebuah perusahaan besar:

- *Local (L)*: Kamu mencari pulpen di atas mejamu sendiri. (Paling dekat).

- *Enclosing (E)*: Jika tidak ada, kamu mencari di ruangan timmu. (Satu tingkat di luar mejamu).

- *Global (G)*: Jika masih tidak ada, kamu mencari di lantai/aula gedung. (Seluruh area perusahaan).

- *Built-in (B)*: Jika tetap tidak ada, kamu mencari di toko alat tulis di luar gedung yang disediakan pemerintah. (Fungsi bawaan Python).

**Local (L)**
Variabel yang didefinisikan di dalam sebuah fungsi. Hanya bisa dilihat oleh fungsi itu sendiri.

```Python
def fungsi_saya():
    x = "Lokal" # Hanya ada di dalam sini
    print(x)
```

**Enclosing (E)**
Ini terjadi jika ada fungsi di dalam fungsi (nested function). Fungsi yang di dalam bisa melihat variabel milik fungsi "induknya".

```Python
def fungsi_luar():
    x = "Enclosing"
    def fungsi_dalam():
        print(x) # Dia meminjam x milik fungsi_luar
    fungsi_dalam()
```

**Global (G)**
Variabel yang didefinisikan di level paling atas dari file .py kamu (di luar semua fungsi).

```Python
x = "Global" # Bisa diakses siapa saja di file ini

def tes():
    print(x)
```

**Built-in (B)**
Nama-nama khusus yang sudah ada di Python sejak awal, seperti print, len, sum, atau int. Kamu tidak perlu mendefinisikannya.

Contoh:

```Python
x = "Global"

def luar():
    x = "Enclosing"
    def dalam():
        x = "Local"
        print(x) # Hasilnya: "Local"
    dalam()

luar()
```

Setelah kita membahas aturan LEGB, kamu mungkin menyadari satu hal: Kita bisa membaca variabel global dari dalam fungsi, tapi apa yang terjadi jika kita ingin mengubah nilainya?

Di sinilah Keyword global berperan sebagai "surat izin" khusus.

Konsep Utama: Membaca vs Mengubah 🔑
Secara default, Python sangat protektif.

Jika kamu hanya membaca variabel global di dalam fungsi, Python akan mengizinkannya.

Namun, jika kamu mencoba mengisi ulang (assignment) variabel tersebut, Python akan menganggap kamu sedang membuat variabel Lokal baru dengan nama yang sama.

Keyword global memberi tahu Python: "Jangan buat variabel lokal baru. Gunakan dan ubah variabel yang ada di level Global."

Analogi Dunia Nyata: Papan Pengumuman Kantor 🏢
Tanpa global: Kamu melihat papan pengumuman di lobi (Global). Kamu menuliskan catatan di buku saku pribadimu (Lokal) dengan judul yang sama. Papan di lobi tidak berubah sama sekali.

Dengan global: Kamu membawa spidol besar, berjalan ke lobi, dan mengubah isi papan pengumuman tersebut. Sekarang, semua orang di kantor melihat perubahan yang kamu buat.

1. Tanpa Keyword global (Gagal Mengubah)

```Python
skor = 0

def tambah_skor():
    skor = 10  # Python menganggap ini variabel LOKAL baru
    print(f"Skor di dalam fungsi: {skor}")

tambah_skor()
print(f"Skor di luar fungsi: {skor}") 
# Hasilnya tetap 0, karena skor Global tidak tersentuh.
```

2. Menggunakan Keyword global (Berhasil Mengubah)

```Python
skor = 0

def tambah_skor():
    global skor  # "Izin" untuk mengakses skor di luar
    skor = 10    # Sekarang kita mengubah skor yang asli
    print(f"Skor di dalam fungsi: {skor}")

tambah_skor()
print(f"Skor di luar fungsi: {skor}") 
# Hasilnya 10! Variabel Global benar-benar berubah.
```

Peringatan Sang Mentor (Best Practice)
Meskipun global itu sakti, jangan terlalu sering menggunakannya. Mengapa?

Sulit Dilacak: Jika programmu sudah besar, sulit mengetahui fungsi mana yang tiba-tiba mengubah nilai variabelmu.

Spaghetti Code: Kode jadi berantakan dan sulit diperbaiki (debug).

Solusi Lebih Baik: Gunakan return (seperti yang kita pelajari sebelumnya) untuk mengirimkan hasil perhitungan keluar fungsi.

Jika global adalah surat izin untuk mengubah variabel di level paling atas (Gedung Pusat), maka nonlocal adalah surat izin untuk mengubah variabel di level Enclosing (Ruang Departemen).

Keyword ini hanya digunakan ketika kita memiliki fungsi di dalam fungsi (nested functions).

Konsep Utama: Menembus Satu Lapisan 🚪
Secara standar, fungsi yang ada di dalam (inner function) bisa membaca variabel milik fungsi luarnya (outer function), tapi tidak bisa mengubahnya. Jika kamu mencoba mengubahnya, Python malah akan membuat variabel lokal baru yang berbeda.

nonlocal memberi tahu Python: "Jangan buat variabel baru di sini. Saya ingin mengubah variabel milik fungsi pembungkus saya (tapi bukan yang Global)."

Analogi Dunia Nyata: Tabungan Keluarga 👨‍👩‍👧
Global: Rekening Bank Pusat (Semua orang tahu).

Enclosing (Outer Function): Celengan di ruang tamu milik Ayah.

Local (Inner Function): Dompet pribadi kamu.

Jika kamu ingin mengambil uang dari Celengan Ayah untuk diisi ulang, kamu tidak bisa hanya bilang "Ini uang saya" (Lokal). Kamu harus bilang, "Saya sedang memakai uang Non-Lokal (milik Ayah di ruang tamu) ini."

1. Tanpa nonlocal (Gagal Mengupdate)

```Python
def luar():
    angka = 10
    def dalam():
        angka = 20 # Python menganggap ini variabel LOKAL baru
        print(f"Dalam: {angka}")
    
    dalam()
    print(f"Luar: {angka}")

luar()
# Hasilnya: Dalam 20, Luar 10 (Variabel luar tidak berubah)
```

2. Menggunakan nonlocal (Berhasil Mengupdate)

```Python
def luar():
    angka = 10
    def dalam():
        nonlocal angka # "Izin" mengubah variabel milik fungsi 'luar'
        angka = 20
        print(f"Dalam: {angka}")
    
    dalam()
    print(f"Luar: {angka}")

luar()
# Hasilnya: Dalam 20, Luar 20 (Variabel luar ikut berubah!)
```