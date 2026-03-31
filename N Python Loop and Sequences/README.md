# Python Loop and Sequence

## Apa itu List?

*List* dapat diibaratkan sebuah rak laci panjang yang saling menyambung. Kita dapat menyimpan berbagai jenis barang didalam setiap lacinya, seperti barang (string, integer, boolean), bahkan rak laci lainnya.

**Tiga sifat utama List yang wajib diketahui**:

- **Berurutan** (*Ordered*): Setiap barang memiliki nomor urut tersendiri.
- **Bisa Diubah** (*Mutable*): Kita dapat menambah, mengganti dan membuang isi laci kapan saja.
- **Mulai dari Nol (Zero-Based Indexing)**: Merupakan aturan utama di Python, bahwa urutan pertama laci (List) adalah 0, bukan 1.

### Cara Membuat dan Mengambil List

Untuk membuat *List*, kita dapat menggunakan `[]` (*Square-bracket*).

```Python
# Membuat List
kota = ['Jakarta', 'Bandung', 'Surabaya']
```

Untuk memanggil salah satu dari isi list tersebut, dengan cara memanggil nama list yang diikuti urutan (indeks) dari item didalam list tersebut.

```Python
# Memanggil List
print(kota[0])   # Hasil: 'Jakarta' (indeks 0 (pertama), pada list tersebut)
```

**Trik Indeks Negatif**:

Jika memerlukan pemanggilan terhadap item terakhir pada list, tanpa mengetahui pasti urutan indeks. Bisa menggunakan cara *negative-indexing*. Jika kita menggunakan `[-1]` maka item list paling terakhir akan dipanggil.

```Python
# Negatif indexing
print(kota[-1])   # Hasil: 'Surabaya' (memanggil item list pada indeks paling terkahir)
```

### Alat Bantu List

Python memiliki beberapa fungsi yang dapat digunakan untuk membantu bekerja dengan List.

- Fungsi `len()` (length / panjang): digunakan untuk mengetahui berapa total panjang list (index list).

```Python
# Fungsi Len
angka = [1, 2, 3, 4, 5]
print(len(angka))   # Hasil: 5 (panjang list (index) 5)
```

- Fungsi `list()`, digunakan untuk memecah sebuah data menjadi list. Bekerja pada tipe data string, yang akan memecah sub-string didalamnya kedalam bentuk list. Fungsi `list()` hanya bekerja pada elemen berbentuk string, tidak dengan integer dan lainnya.

```Python
# Fungsi List
nama = 'Budi'
print(nama)   # Hasil: ['B', 'u', 'd', 'i']
```

### Mengubah dan Menghapus List

Dikarenakan *List* merupakan tipe data yang *mutable* (dapat diubah), kita dapat mengubah dan menghapus item pada list dengan mudah.

**Mengganti isi List**:

```Python
# Mengganti item pada List
bahasa = ['Python', 'Jav', 'C++', 'Rust']
bahasa[0] = 'JavaScript'   # Mengganti index ke-0 dari 'Python' menjadi 'JavaScript'
print(bahasa)   # Hasil: ['JavaScript', 'Java', 'C++', 'Rust']
```

Catatan: Perlu dipastikan dengan benar index item yang hendak digantikan. Jika kita mengganti index item yang tidak terdapat pada list, maka Python akan mengirimkan pesan `IndexError`.

**Menghapus isi List**:

Selain mengganti item pada List, kita juga dapat menghapus item pada List dengan menggunakan kata kunci `del`.

```Python
# Menghapus Item List dengan kata kunci `del`
karyawan = ['Budi', 23, 'Programmer']
print(karyawan)   # Hasil: ['Budi', 23, 'Programmer']
del karyawan[1]   # Statement ini akan menghapus index ke-1 (23)
print(karyawan)   # Hasil: ['Budi', 'Programmer']
```

### Mengecek isi dan List Bertingkat (Nested List)

Untuk mengecek suatu item terdapat (ada) pada suatu list atau tidak, kita dapat menggunakan operator `in`. Hasil dari pengecekan tersebut, Python akan mengembalikan nilai boolean, True (Benar) dan False (Salah).

```Python
# Mengecek isi List dengan operator `in`
bahasa = ['Python', 'Java']
print('Java' in bahasa)   # Hasil: True (Benar)
print('Ruby' in bahasa)   # Hasil: False (Salah)
```

**Mengecek List di dalam List**:

Kita dapat mengecek sebuah list (*nested list*) didalam sebuah list:

```Python
# Mengecek Nested List
data = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(data[2][1]) # Hasilnya: 'Rust'
```

### Melakukan Unpacking dan Slicing pada List

*Unpacking*, teknik untuk membongkar sebuah list, dan memasukannya kedalam variabel baru secara bersamaan.

```Python
# Melakukan Unpacking pada List
profil = ['Alice', 34, 'Developer']
nama, usia, pekerjaan = profil

print(nama)   # Hasil: 'Alice'
```

Catatan: Terkadang kita hanya memerlukan satu atau lebih item kedalam variabel yang sama. Dalam kondisi tersebut, kita dapat menggunakan simbol `*` untuk memberi tanda pada variabel yang dimaksud.

```Python
# Unpacking dengan bersamaan `*`
siswa = ['Ali', 'Budi', 'Carlos']
siswa_pertama, *siswa_lainnya = siswa
print(siswa_pertama)   # Hasil: 'Ali'
print(siswa_lainnya)   # Hasil: ['Budi', 'Carlos']
```

**Melakukan Slicing pada List**:

Kita dapat melakukan slicing pada List, yang berguna untuk mengakses beberapa item secara bersamaan dengan cara yang lebih terukur. Untuk melakukan slicing, kita dapat menggunakan operator `:` semicolon, dengan model statement seperti berikut `[Mulai:Berhenti]`.

```Python
# Melakukan Slicing pada List
kue = ['Bolu', 'Kukis', 'Es Krim', 'Pie', 'Brownies']
print(kue[1:4])   # Hasil: ['Kukis', 'Es Krim', 'Pie']
```

Dalam Slicing, kita juga dapat menerapkan *step* dimana mengambil angak kelipatan pada index.

```Python
# Melakukan Slicing - Step
bilangan = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bilangan[1::2])   # Hasil: [2, 4, 6, 8]. Mulai dari index ke-1, naik dua index setelahnya [2, 4, 6, 8]
```

List adalah struktur data yang paling sering digunakan di Python. Dengan memahami konsep List, maka akan mempermudah untuk menguasai Bahasa Pemrograman Python.

## Method List

*Method* adalah alat bantu yang dapat digunakan untuk memodifikasi dan bekerja dengan List.

### Menambahkan Item pada List

**Menambahkan item menggunakan `append()`**:

Method `append()` digunakan untuk menambahkan item pada List. Penggunaan method tersebut akan menambahkan item baru kedalam List, pada indeks terkahir, atau menambah indeks baru (paling belakang).

```Python
# Menambah item menggunakan `append()`
angka = [1, 2, 3, 4, 5]
angka.append(6)

print(angka)   # Hasil: [1, 2, 3, 4, 5, 6]
```

Catatan: Menggunakan method `append()`, juga dapat digunakan untuk menambahkan List baru kedalam List (nesting list).

```Python
# Menggunakan method append() - Nesting List
angka = [1, 3, 5]
angka_genap = [2, 4, 6]
angka.append(angka_genap)

print(angka)   # Hasil: [1, 3, 5, [2, 4, 6]]
```

**Menambahkan item menggunakan `extend()`**:

Kita juga dapat menggunakan `extend()` untuk menambahkan List. Method ini bersifat ordered (terurut), mirip dengan method `append()` yang dapat menambahkan List lain kedalam List baru atau lama, namun dengan tidak menesting list yang ditambahkan.

```Python
# Menambahkan List dengan method `extend()`
angka = [1, 2, 3]
angka_ditambah = [4, 5, 6]
angka.extend(angka_ditambah)

print(angka)   # Hasil: [1, 2, 3, 4, 5, 6]
```

**Menambahkan item menggunakan `insert()`**:

Digunakan untuk menambahkan (menyisipkan) item pada posisi index tertentu, bukan diakhir seperti `append()`.

```Python
# Menambahkan item menggunakan method `insert()`
angka = [1, 2, 4, 5]
angka.insert(2, 3)   # 2 adalah index yang hendak disisipkan, dan 3 merupakan item yang dimasukan

print(angka)   # [1, 2, 3, 4, 5]
```

### Menghapus Item pada List

**Menggunakan `remove()`**:

Method `remove()` digunakan untuk menghapus item pada sebuah List. Method ini menggunakan nilai (value) yang berada pada List tersebut.

```Python
# Menghapus item menggunakan `remove()`
nilai = [10, 20, 30, 40, 50, 60 , 50]
nilai.remove(50)   # statment ini akan menghapus nilai (value) 50 yang ada pada List

print(nilai)   # Hasil: [10, 20, 30, 40, 60, 50]
```

Catatan: Method `remove()` hanya akan menghapus nilai pertama (nilai-sama) yang ditemui, tetapi tidak dengan nilai sama yang muncul setelahnya.

**Menggunakan `pop()`**:

Berbeda dengan `remove()`, `pop()` menghapus item berdasarkan nilai index-nya.

```Python
# Menghapus item pada List dengan `pop()`
angka = [1, 2, 3, 4, 5, 6]
angka.pop(1)   # statement ini akan menghapus nilai 2 pada List

print(angka)   # Hasil: [1, 3, 4, 5, 6]

angka.pop()   # statement ini akan menghapus nilai terakhir pada List, dengan tidak menambahkan argumen apapun pada method `pop()`

print(angka)   # Hasil: [1, 3, 4, 5]
```

Catatan: Jika argumen pada method `pop()` tidak diberikan, maka secara bawaan, Python akan menyingkirkan nilai terakhir pada List.

**Menggunakan `clear()`**:

Method ini digunakan untuk menghapus semua item didalam List.

```Python
# Menghapus seluruh item pada List menggunakan method `remove()`
angka = [1, 2, 3, 4, 5]
angka.clear()   # statement ini akan menghapus semua item pada List

print(angka)   # Hasil: []. Semua item pada list tidak akan muncul karena dihapus seleruhnya.
```

### Merapikan dan Memutar Posisi Item pada List

**Menggunakan `sort()`**:

Method `sort()` digunakna untuk mengurutkan item pada List berdasarkan bilangan (terbesar ke terkecil) atau sesuai abjat alpabetikal.

```Python
# Menggunakan method `sort()` untuk mengurutkan item pada List
angka = [1, 99, 21, 87, 35, 76, 66, 55, 44]
angka.sort()   # statement ini akan mengurutkan item pada list sesuai urutan bilangan

print(angka)   # Hasil: [1, 21, 35, 44, 55, 66, 76, 87, 99]

# Sesuai abjat alpabetikal
huruf = ['e', 'a', 'f', 'd', 'c', 'b',]
huruf.sort()

print(huruf)
```

**Menggunakan `sorted()`**:

Method `sorted()` sedikit berbeda dengan `sort()`. `sorted()` akan mengurutkan item pada List dengan memasukannya kedalam variabel baru. Dengan tetap membiarkan variabel lama tidak terurut (tetap acak).

```Python
# Menggunakan `sorted()` untuk mengurutkan item List
acak = [19, 2, 35, 1, 67]
rapi = sorted(acak)

print(acak) # Tetap berantakan: [19, 2, 35, 1, 67]
print(rapi) # Rak baru yang rapi: [1, 2, 19, 35, 67]
```

**Menggunakan `reverse()`**:

Method ini digunakan untuk membalikan item dari urutan sebelumnya.

```Python
# Menggunakan method `reverse()` pada item List
item = [5, 4, 3, 2, 1]
item.reverse()   # statement ini akan membalikan urutan pada list (reverse)

print(item)   # Hasil: [1, 2, 3, 4, 5]
```

### Mencari Index Item

**Menggunakan `index()`**:

Method tersebut digunakan untuk mencari tahu, suatu item terdapat pada index berapa pada sebuah item.

```Python
# Menggunakan method `index()` untuk mencari index item pada List
bahasa = ['Python', 'Java', 'C++', 'Rust']
print(bahasa.index('Java'))   # Hasil: 1, statement ini akan mencari dimana letak index dari 'Java', yaitu index ke-1
```

Catatan: Perlu diketahui dalam penggunaan method `index()`, jika kita mencari index dari value (item) yang tidak terdapat pada List, maka Python akan memberikan eror `ValueError`. Termasuk juga kesalahan spesifik pada item yang dituju. Dalam contoh diatas, dicari index dari value `'Java'` dan mengembalikan hasil 1 (berhasil). Tetapi jika yang kita masukan adalah `'java'` maka akan eror, karena berbeda antara `'Java'` dan `'java'`, atau biasa disebut `case-sensitive`.

Method-method diatas merupakan fungsi yang dapat digunakan untuk bekerja dengan List di Python.

## Apa itu Tuples?

Mirip seperti *List*, *Tuple* juga merupakan tipe data di Python yang berfungsi untuk menyimpan nilai secara terurut. Dapat diisi dengan string, integer, boolean dan tipe data lainnya.

```Python
# Tipe Data Tuple
karyawan = ('Alice', 24, 'Rust Developer')
```

**Perbedaan Utama**:

Jika List merupakan tipe data yang dapat diubah (*mutable*), sementara Tuple merupakan tipe data yang tidak dapat diubah (*imutable*). Begitu tipe data tersebut dideklarasikan, maka isinya tidak dapat diubah.

Jika dengan sengaja kita mencoba merubah isi dari Tuple, maka Python akan mengirimkan eror `TypeError`.

```Python
bahasa = ('Python', 'Java', 'C++', 'Rust')
bahasa[0] = 'JavaScript'   # Statement yang mencoba merubah nilai pada index 0

print(bahasa)   # Hasil: TypeEror. Python akan mengirimkan error.
```

### Cara Mengakses Nilai pada Tuple

Meskipun nilai pada Tuple tidak dapat diubah, namun kita tetap bisa mengakses nilai yang berada didalamnya. Dengan cara yang sama dengan bagaimana kita mengakses item pada List.

```Python
# Mengakses Nilai didalam Tuple
karyawan = ('Alice', 24, 'Rust Developer')
print(karyawan[1])   # Hasil: 24, mengakses index ke 1 pada Tuple: 24.
```

**Mengakses Nilai dengan Negative Indexing**:

Cara mengakses nilai negatif index juga dapat diterapkan di Tuple.

```Python
# Mengakses dengan Metode Negative Indexing
angka = (1, 2, 3, 4, 5)
print(angka[-1])   # Hasil: 5. Mengakses index paling belakang dari Tuple.
```

Catatan: Aturan dalam indexing juga berlaku dalam Tuple, dimana jika kita sengaja mengakses index yang tidak tersedia di Tuple, maka eror akan diberikan Python `IndexError`.

### Membuat Tuple dari Data Lain

**Menggunakan Fungsi `tuple()`**:

Jika di List, kita mengenal fungsi `list()` yang dapat digunakan untuk menjadikan sebuah nilai dalam variabel menjadi bentuk List. Tuple juga memiliki fungsi serupa yaitu, `tuple()` yang akan mengkonversi nilai menjadi bentuk Tuple. Namun perlu diketahui, fungsi tersebut hanya berlaku untuk String, yang akan memecah sub-string kedalam index terurut. Tidak berlaku untuk tipe data lain diluar string.

```Python
# Menggunakan fungsi tuple()
nama = 'Jessica'
print(tuple(nama))   # Hasil: ['J', 'e', 's', 's', 'i', 'c', 'a']
```

**Mengecek Ketersediaan Nilai didalam Tuple dengan Opertor `in`**:

Dengan operator `in`, kita bisa mengecek apakah sebuah nilai ada dialam Tuple. Hasil akan dikembalikan dalam bentuk boolean, dimana jika nilai yang dimaksud tersedia didalam Tuple maka akan dikembalikan True, dan jika tidak tersedia akan dikembalikan False.

```Python
# Menggunakan operator `in`, untuk mengecek nila pada Tuple
bahasa = ('Python', 'Java', 'C++', 'Rust', 'JavaScript')
print('Rust' in bahasa)   # Hasil: True. Karena nilai 'Rust' tersedia didalam Tuple.
print('javaScript' in bahasa)   # Hasil: False. Karena nilai 'JavaScript' tidak tersedia didalam Tuple.
```

Catatan: Perlu diperhatikan dengan cermat ketika mengecek suatu nilai menggunakan operator `in` di dalam Tuple. Kondisi `case-sensitive` berlaku, jika bentuk atau format yang dicari berbeda secara eksplisit, maka akan dikembalikan False (tidak tersedia). Berbeda antara `'JavaScript'` dan `'javaScript'`.

### Melakukan Unpacking dan Slicing pada Tuple

**Melakukan Unpacking pada Tuple**:
Di Tuple kita juga dapat melakukan Unpacking dan Slicing seperti di List. Metode yang digunakan juga sama persis dengan yang dilakukan di List.

```Python
# Unpacking Nilai pada Tuple
karyawan = ('Alice', 34, 'Rust Developer')
nama, umur, pekerjaan = karyawan   # statement ini akan memecah nilai pada Tuple kedalam variabel baru yang disediakan (nama, umur dan pekerjaan)
print(nama)   # Hasil: 'Alice'
print(umur)   # Hasil: 34
print(pekerjaan)   # Hasil: 'Rust Developer'
```

Kita juga dapat melakukan unpacking pada sebagian atau satu nilai pada Tuple, dengan menggunakan operator `*`.

```Python
# Melakuka unpacking pada satu nilai dan mengirim sisanya kesatu variabel.
karyawan = ('Alice', 34, 'Rust Developer')
nama, *sisanya = karyawan   # statement ini akan melakukan unpack pada nilai 'Alice' kedalam variabel nama, dan memasukan nilai lain kedalam variabel *sisanya.
print(nama)   # Hasil: 'Alice'.
print(*sisanya)   # Hasil: (34, 'Rust Developer')
```

**Melakukan Slicing pada Tuple**:

Tuple juga dapat dilakukan slicing seperti di List. Dengan menggunakan operator `:` semicolon.

```Python
# Melakukan Slicing pada Tuple
kue = ('Pie', 'Bolu', 'Brownis', 'Pukis', 'Pancong')
print(kue[1:3])   # Hasil: (Bolu, Brownis)
```

### Kenapa Nilai didalam Tuple Tidak Dapat Dihapus?

Karena sifatnya yang immutable (permanen), kita juga tidak dapat membuang nilai yang ada didalam Tuple. Seperti menggunakan kata kunci `del` yang dapat dilakukan dengan List. Tetapi di Tuple tidak bisa dilakukan.

### Kapan Harus Menggunakan Tuple dan List?

- Dalam situasi dimana kita memerlukan data yang dinamis, dimana setiap nilai yang dimasukan dapat diubah dan diganti kapan saja seiring berjalannya program, maka kita memerlukan List `[]`.
- Sementara untuk situasi yang bersifat statis atau permanen, dimana nilai tidak akan diubah kita dapat menggunakan Tuple `() `.

## Method di Tuple

Python juga memberikan alat bantu untuk kita bekerja dengan Tuple.

### Menghitung Suatu Nilai yang terdapat dialam Tuple

Dengan method `count()` kita dapat mengetahui berapa banyak suatu nilai berada didalam sebuah Tuple.

```Python
# Menggunakan Method count()
bahasa = ('Python', 'Java', 'Rust', 'C++', 'JavaScript', 'Rust')

print(bahasa.count('Rust'))   # Hasil: 2. Dalam statement tersebut diketahui bahwa Rust memiliki 2 nilai didalam tuple bahasa
```

Jika nilai yang dicari tidak berada didalam Tuple tersebut, maka Python tidak akan mengembalikan eror, tetapi nilai 0.

```Python
# Jika Nilai yang dicari tidak ada didalam Tuple
bahasa = ('Python', 'Java', 'Rust', 'C++', 'JavaScript', 'Rust')

print(bahasa.count('C#'))   # Hasil: 0.
```

Catatan: Ketika menggunakan method `count()`, kita wajib mengisi argumen pada method. Jika method dibiarkan kosong maka Python akan mengembalikan eror `TypeError`.

### Mencari Index Suatu Nilai pada Tuple

Dengan method `index()` kita dapat mengetahui posisi index suatu nilai didalam sebuah Tuple.

```Python
# Menggunakan method index() untuk mencari index suatu nilai didalam Tuple
bahasa = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(bahasa.index('Java')) # Hasilnya: 1 (Laci kedua)
```

Catatan: Jika nilai yang dicari tidak terdapat didalam Tuple, maka Python akan mengembalikan eror `ValueError`.

Terdapat teknik lebih lanjut untuk mencari index dari suatu nilai didalam Tuple. Denga menentukan argumen index yang dicari.

```Python
bahasa = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
# Cari kata 'Python', tapi mulai pencarian dari laci nomor 3
print(bahasa.index('Python', 3)) # Hasilnya: 5
# Python mengabaikan 'Python' di laci nomor 2, dan langsung menemukan 'Python' berikutnya di laci nomor 5
```

Bisa dilakukan juga dengan menentukan nilai Mulai dan Berhenti pencarian index.

```Python
bahasa = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript')
# Cari 'Python', mulai dari laci 2, tapi berhenti mencari sebelum laci 5
print(bahasa.index('Python', 2, 5)) # Hasilnya: 2
```

### Merapikan isi Tuple

Dengan method `sorted()`. Diketahui bahwa kita tidak dapat mengubah nilai pada Tuple, berbeda dengan List yang dapat diubah. Dengan demikian kita tidak bisa menggunakan method `sort()` di Tuple.

Namun kita tetap bisa merpikan Tuple dengan menggunakan method `sorted()`, dimana nilai Tuple akan dipindahkan dari variabel lama ke variabel baru. Tanpa mengubah nilai Tuple dari variabel lama. Dengan demikian method `sorted()` dapat digunakan di Tuple.

```Python
# Menggunakan Method sorted()
angka = (13, 2, 78, 3, 45, 67, 18, 7)
angka_rapi = sorted(angka)

print(angka_rapi) # Hasilnya berupa LIST BARU: [2, 3, 7, 13, 18, 45, 67, 78]
```

**Trik Khusus dalam Merapikan Tuple dengan `sorted()`**:

Kita dapat merapikan (menyortir) nilai berdasarkan panjang elemen yang dimilikinya. Untuk melakukannya kita dapat menggunakan method `key=len`.

Jika kita memiliki nilai dan ingin mengurutkannya dari kata yang paling pendek ke yang paling panjang, gunakan `key=len` (length/panjang).

```Python
# Menggunakan key=len untu menyortir nilai di Tuple
bahasa = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(bahasa, key=len)) 
# Hasilnya: ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']
```

Selain itu, kita juga dapat melakukan sorti secara terbalik dengan `reverse=True`. Secara bawaan sortir dilakukan dari A-Z atau Besar-Kecil. Jika Kita ingin membalikan, bisa menambahkan argument `reverse=True`.

```Python
# Melakukan Sortir Terbalik dengan reverse=True
bahasa = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(bahasa, reverse=True))
# Hasilnya: ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']
```

Berikut merupakan cara menggunakan method untuk membantu pengolahan data Tuple di Python.

## Loop di Python

Pasti akan sangat melelahkan jika harus mengulang suatu hal yang sama secara berulah. Dalam dunia pemrograman ada suatu aksi yang dilakukan secara berulang oleh komputer, hal tersebut dikenal dengan *Loop* atau perulangan.

### Perulangan `for`

`for` merupakan kata kunci yang digunakan untuk membuat perulangan. Seperti kita ingin menelusuri semua data pada suatu List, kita ingin mengeluarkan semua data yang ada didalam List tersebut.

**Menelusuri List**:

Kita bisa meminta Python mencetak setiap data yang ada pada List berikut.

```Python
# Melakukan perulangan pada List, untuk menelusuri seluruh data
bahasa_pemrograman = ['Rust', 'Java', 'Python', 'C++']

for bahasa in bahasa_pemrograman:   # statement perulangan
  print(bahasa)   
```

Hasil dari perulangan tersebut:

```shell
Rust
Java
Python
C++
```

Catatan: Perlu diperhatikan bahwa `for` memiliki blok kode untuk menghasilkan eksekusi. Perlu diingat bahwa blok kode di Python ditandai dengan indentasi pada baris setelah statement utama.

**Menelusuri Teks String**:

Kita juga bisa memecah sebuah string, menjadi bagian-bagian sub-string dengan menggunakan `for`.

```Python
# Melakukan perulangna pada string
for huruf in 'kode':
  print(huruf)
```

### Perulangan Bersarang (Nested Loops)

Kita juga bisa membuat perulangan didalam perulangan.

```Python
# Melakukan Nested Loop
kategori = ['Buah', 'Sayur']
makanan = ['Apel', 'Wortel', 'Pisang']

for kat in kategori:   # Perulangan Luar
  for mak in makanan:   # Perulangan Dalam 
    print(kat, mak)
```

Cara kerjanya adalah Python akan mengambil 'Buah' dan memasangkan dengan semua makanan. Setelah selesai, akan mengambil 'Sayur' dan memasangkan dengan semua makanan kembali.

Hasilnya:

```shell
Buah Apel
Buah Wortel
Buah Pisang
Sayur Apel
Sayur Wortel
Sayur Pisang
```

### Perulangan While

Berbeda dengan `for`, dimana jumlah perulangan yang dilakukan sudah diketahui. `while` digunakan ketika tidak diketahui pasti kapan perulangan harus berhenti. Tetapi ada sebuah syarat yang harus dipenuhi.

Seperti sebuah game tebak angka, "Selama angka yang dimaksud tertebak, maka diperbolehkan untuk terus bertanya dan menebaknya.

```Python
# Perulangan dengan while
angka_rahasia = 3
tebakan = 0

# Selama 'tebakan' tidak sama dengan 'angka_rahasia', perulangan akan tersu dilakukan.
while tebakan != angka_rahasia:
  # Meminta input pengguna dan mengubahnya menjadi integer
  tebakan = int(input('Tebak angka (1 - 5): '))

  if tebakan != angka_rahasia:
    print('Salah! Coba lagi.')

# Jika tebakan benar, maka cetak print berikut
print('Kamu berhasil menebaknya')
```

### Mengendalikan Perulangan dengan `break` dan `continue`

Python memiliki kata kunci yang dapat digunakan untuk mengintervensi perulangan yang dilakukan.

**Kata kunci `break`**:

Kata kunci `break` akan secara otomatis memberhentikan perulangan yang terjadi meskipun tugas belum selesai dilakukan.

```Python
# Menggunakan `break` pada perulangan
nama_karyawan = ['Jess', 'Naomi', 'Tom']

for nama in nama_karyawan:
    if nama == 'Naomi':
        break  # Ketemu Naomi? Langsung BERHENTI!
    print(nama)
```

Hasilnya hanya mencetak Jess. Begitu melihat 'Naomi', program langsung keluar dari perulangan, sehingga 'Tom' tidak pernah tersentuh.

**Kata Kunci `continue`**:

Digunakan untuk mengabaikan perulangan yang sedang berjalan, dan melanjutkan perulangan selanjutnya.

```Python
# Menggunakan `continue` pada perulangan
nama_karyawan = ['Jess', 'Naomi', 'Tom']

for nama in nama_karyawan:
    if nama == 'Naomi':
        continue  # Ketemu Naomi? Lompati dia, lanjut ke orang berikutnya!
    print(nama)
```

Hasilnya mencetak Jess dan Tom. 'Naomi' dilompati begitu saja.

### Memasangkan else dengan for dan while

Dalam bahasa pemrograman, `else` biasanya akan dipasangkan dengan `if` saja. Namun di Python, kata kunci `else` dapat dipasangkan dengan `for` dan `while` dibagian akhir.

Aturannya adalah blok `else` hanya akan dijalankan jika perulangan dilakukan dengan sesuai sampai akhir (Tidak dihentikan dengan `break`).

```Python
# Menggunakna katak kunci else pada perulangan
kata_kata = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for kata in kata_kata:
    for huruf in kata:
        # Jika menemukan huruf vokal
        if huruf.lower() in 'aeiou':
            print(f"'{kata}' memiliki huruf vokal '{huruf}'")
            break # Huruf vokal ketemu, hentikan pencarian di kata ini!
    
    else:
        # Bagian ini HANYA jalan jika 'break' di atas TIDAK PERNAH tersentuh 
        # (Artinya sudah dicari sampai ujung, tapi tidak ada vokal sama sekali)
        print(f"'{kata}' tidak punya huruf vokal")
```

## Menggunakan Range di Loop

Jika sebelumnya kita sudah mengetahui cara mengekstraksi data dari sebuah List atau Tuple dengan menggunakan perulangan `for`.

Tapi bagaimana kita ingin melakukan perulanga angka tanpa data pada List atau Tuple sebanyak 10 kali.

### Apa itu `range()`

Fungsi `range` adalah menghasilkan deretan angka bulat secara otomatis. Memiliki tigas bagain argumen yaitu, `range(mulai, berhenti, langkah)`.

**Menetukan titik berhenti**:

Jika kita hanya memberikan satu nilai pada argumen `range`, maka Python menganggap nilai tersebut sebagai nilai akhir atau batas akhir.

```Python
# Menggunakan range, menentukan batas akhir
for angka in range(3):   # nilai argumen 3 pada range dianggap sebagai batas akhir perulangan
  print(angka)
```

Hasilnya:

```Shell
0
1
2
```

Catatan: Seperti urutan pada umumnya dalam pemorograman, hitungan dimualai dari bilangan 0. Dan 3 merupakan nilai yang bersifat inklusif, jadi tidak ikut dicetak karena bersifat sebagai pembatas.

**Menentukan titik awal**:

Jika kita tidak mau memulainya dari 0, maka kita bisa menentukan titik awal dengan menambahkan argumen pada `range`.

```Python
# Menggunakan range, menentukan titik awal dan akhir
for angka in range(1, 5):   # nilai 1 merupakan awal dimana hitungan dimulai dari angka 1, nilai 5 merupakan jumlah perulangan yang dilakukan
  print(angka)   # Hasil: 1 2 3 4
```

**Menentukan Ukuran Lompatan**:

Bagaimana jika kita hanya akan mencetak nilai genap saja. Untuk membuat perulangan tersebut, kita bisa menentukan langkah pada `range`.

```Python
# Menggunakan range, menetuka langkah untuk mencetak nilai genap
for angka in range(2, 11, 2):   # Nilai 2 merupakan bilangan awal, nilai 11 adalah batas akhir, dan nilai 2 yang terakhir adalah langkah yang dilakukan, maksudnya perulangan dilakukan 2 langkah, dari 2 ke 4 dan seterusnya sampai batas akhir di 11.
  print(angka)   # Hasil: 2 4 6 8
```

### Melakukan Hitungan Mundur (Lompatan Negatif)

Fungsi `range()` juga bisa berjalan mundur! Syaratnya adalah titik mulai harus lebih rendah dari titik berhenti, dan angka lompatan harus negatif.

```Python
# Mulai dari 40, berhenti sebelum 0, mundur 10 langkah setiap putaran
for angka in range(40, 0, -10):
    print(angka)
```

### Aturan Dalam Range

- Tidak Boleh Kosong. Kita wajib memberikan nilai argumen pada `range()` minimal satu. 
- Tidak Bisa Menggunakan Nilai Float. `range()` hanya berfungsi pada bilangan integer. Jika sengaja memasukan nilai float maka Python akan mengembalikan eror `TypeError`.

### Membuat Trik dengan Range

Selain dipasangkan denga `for`, `range()` juga bisa dipasangkan dengan `list()` untuk membuat List berisi angka dalam sekejap.

```Python
# Menggunakan Range untuk membuat List
angka_genap = list(range(2, 11, 2))

print(angka_genap) # Hasilnya instan: [2, 4, 6, 8, 10]
```

Fungsi range() adalah salah satu alat yang akan sangat, sangat sering kamu gunakan saat membuat program dengan Python.

## Menggunakan Enumerate dan Zip

Setelah mengetahui cara melakukan perulangan dengan `for`. Selain mengambil nilai dari sebuah List, terkadan juga kita ingin mengetahui nilai tersebut merupakan nilai keberapa, atau membaca dua List sekaligus.

Python memiliki dua fungsi yang dapat membatu melakukan hal tersebut yaitu `enumerate()` dan `zip()`.

### `enumerate()`

Ketika kita memiliki List bahasa, dimana kita ingin mencetaknya dengan nomor urut, biasanya kita juga akan membuat variabel untuk membuat nomor urut secara manual.

```Python
# Melakukan perulangan denga nomor urut dengan variabel manual
bahasa_pemrograman = ['Python', 'Java', 'C++', 'Rust']

nomor = 0   # Nomor untuk urutan manual

for bahasa in bahasa_pemrograman:
  print(f'{nomor} adalah bahasa {bahasa}')
  nomor += 1
```

Python memberikan solusi untuk melakukan hal tersebut jauh lebih simpel, menggunakan fungsi `enumerate()`. Berfungsi memberikan urutan nomor indeks pada perulangan yang dibuat secara otomatis.

```Python
# Menggunakan enumerate() dalam perulangan
bahasa_pemrograman = ['Python', 'Java', 'C++', 'Rust']

for nomor, bahasa in enumerate(bahasa_pemrograman):
  print(f'{nomor} adalah bahasa {bahasa}')
```

Fungsi `enumarate()` melakukan urutan dari bilangan 0, berlaku umum di Python. Jika kita ingin melakukan urutan dari bilangan 1, maka kita bisa menambahkan argumen kedua pada fungsi, sesuai bilangan awal atau urutan awal.

```Python
# Menggunakan enumerate() dalam perulangan dan memberikan argumen titi awal
bahasa_pemrograman = ['Python', 'Java', 'C++', 'Rust']

for nomor, bahasa in enumerate(bahasa_pemrograman, 1):
  print(f'{nomor} adalah bahasa {bahasa}')
```

### `zip()`

Bagiamana jika disuatu kondisi, kita memiliki dua List yang memiliki data yang berketerkaitan. List pertama berisi nama karyawan, dan List kedua berisi ID karyawan. Kemudian, kita ingin mencetak kedua List tersebut secara bersamaan.

Dalam kondisi tersebut, kita dapat menggunakan fungsi `zip()`. Ibarat sebuah resleting yang mengunci sebelah kiri dan kanan secara bersamaan, lalu menjadikan satu pasangan Tuple.

Contoh:

```Python
# Menggunakan zip()
karyawan = ['Alrizq', 'Damara', 'Rocky', 'Wayan']
id_karyawan = [1, 2, 3, 4]

data_karyawan = zip(karyawan, id_karyawan)   # statement ini menampung operasi dari zip yang menggabungkan dua List menjadi satu
print(data_karyawan)
```

Kemampuan terbaik zip akan sangat berguna ketika dipasangkan dengan `for`. Dimana kita bisa membaca dua List secara paralel (bersamaan):

```Python
# Menggunakan zip dengan for
karyawan = ['Alrizq', 'Damara', 'Rocky', 'Wayan']
id_karyawan = [1, 2, 3, 4]

# Melakuakan pembongkaran pasangan nama dan id secara bersamaan
for nama, id in zip(karyawan, id_karyawan):
  print(f'Nama: {nama}')
  print(f'ID: {id}')
  print('---')
```

### Kesimpulan

- Kita dapat menggunakan `enumerate()` jika kita membutuhkan data beserta nomor urutnya.
- Kita dapat menggunakan `zip()`, jika kita butuh untuk membaca dua atau lebih List secara bersamaan.

## List Comprehension

Biasanya, ketika kita hendak membuat List berisikan angka genap 0 - 20, kita harus menyiapkan List kosong, membuat Loop, lalu melakukan if, dan memasukannya satu per satu dengan append().

```Python
# cara lama membuat List yang berisikan angka genap
angka_genap = []

for angka in range(21):
  if angka % 2 == 0:   # melakukan pengecekan jika bilangan habis dibagi dua, berarti bilangan genap
    angka_genap.append(angka)

print(angka_genap)   # Hasil: berisikan bilangan genap
```

**Menggunakan cara List Comprehension**:

Jika kita perlu membuat beberapa kode baris seperti diatan, Python memungkinkan kita untuk membuat hal yang sama hanya dengan baris kode yang lebih sedikit, dengan memberikan statement langsung didalam kurung siku `[]`.

```Python
# Menggunakan cara List Comprehension
angka_genap = [angka for angka in range(21) if angka % 2 == 0]

print(angka_genap)   # Hasil: berisikan bilangan genap
```

Cara membaca kode diatas yang lebih simple:

"Masukkan `angka` (hasil akhir) -- dari setiap `angka` di dalam `range(21)` -- tapi HANYA JIKA `angka % 2 == 0`."

**Bagaimana jika ada `if` dan `else`**:

Jika kita ingin menggunakan `if` dan `else` sekaligus, maka aturannya sedikir berubah. Kedua statement tersebut harus diletakan didepan sebelum statement `for`.

```Python
# Menggunakan if dan else dalam List Comprehension
angka = [1, 2, 3, 4, 5]

# Memasang bilangan genap dengan 'Genap' dan bilangan ganjil dengan 'Ganjil'
hasil = [(a, 'Genap') if a % 2 == 0 else (a, 'Ganjil') for a in angka]

print(angka)   # Hasil: bilangan genap akan diberi label 'Genap', bilangan ganjil akan diberi label 'Ganjil'
```

### Menggunakan `filter()` (Bouncer)

Jika kita memiliki List besar, dan hanya ingin mengambil value dengan syarat tertentu saja, gunakan `filter()`. Fungsi ini butuh dua hal: aturan dan data aslinya.

contoh:

```Python
# Menggunakan filter
kata_kata = ['pohon', 'langit', 'gunung', 'sungai', 'awan', 'matahari']

# 1. membuat aturan untuk fungsi yang dijalankan
def apakah_kata_panjang(kata):
  return len(kata) > 4   # hanya boleh masuk jika huruf lebih dari 4

# 2. menggunakan filter() dan ubah kembali hasilnya menjadi List
kata_panjang = list(filter(apakah_kata_panjang, kata_kata))

print(kata_panjang)
# Hasilnya: ['pohon', 'langit', 'gunung', 'sungai', 'matahari'] 
# ('awan' tidak ikut karena hurufnya cuma 4) 
```

### Fungsi `map()`

Berbeda dengan filter yang membuang data, `map()` bertugas mengubah/memodifikasi semua isi list secara masal menggunakan suatu rumus.

Misalnya, kita punya suhu dalam ukuran celsius dan ingin mengubahnya dalam bentuk fahrenheit

```Python
# Menggunakan map
celcius = [0, 10, 20, 30, 40]

# 1. Buat rumus pengubah
def ke_fahrenheit(suhu):
  return (suhu * 9/5) + 32

# 2. Gunakan map untuk menerapkan rumus ke semua suhu didalam list
fahrenheit = list(map(ke_fahrenheit, celcius))

print(fahrenheit)
# Hasil: [32.0, 50.0, 68.0, 86.0 104.0]
```

### Fungsi `sum()`

Fungsi sum merupakan fungsi paling sederhana dan berguna. Jika kita memiliki List bersikan angka dan ingin menjumlah totalnya, cukup panggil `sum()`

```Python
# Menggunakan sum
angka = [5, 10, 15, 20]
total = sum(angka)

print(total)   # Hasil: 50
```

**Trik Tambahan**:

Bagaimana jika kamu sudah memiliki saldo awal sebesar 10, lalau ingin menambahkan semua angka di List ke Saldo tersebut, kita bisa menambahkan `start`.

```Python
# Menambahkan start pada sum
angka = [5, 10, 15, 20]

# Menambahkan total angka (50) dengan saldo awal (10)
total_akhir = sum(angka, start=10) 

print(total_akhir) # Hasilnya: 60
```

Konsep List Comprehension beserta fungsi map() dan filter() mungkin terasa agak mengintimidasi dan sulit dibaca pada awalnya. Itu sangat wajar! Semakin sering kamu menulis kode Python, matamu akan semakin terbiasa dan kamu akan sangat menyukai seberapa ringkas kodenya nanti.

## Python Lambda Function

### Apa itu Fungsi Lambda

Sejauh ini, jika kita ingin membuat fungsi untuk memangkatkan angka (kuadrat), kita menuliskannya secara resmi dan memberinya nama sepert berikut.

```Python
# Menggunakna Fungsi biasa
def kuadrat(angka):
  return angka ** 2

print(kuadrat(4))   # Hasil: 16
```

Dalam kasus tersebut kita dapat menyingkatnya hanya dengan satu baris kode saja, dengan Lambda Function. Kita tidak perlu memberinya nama (itulah kenapa disebut sebagai Anonymous Function atau Fungsi Anonim).

```Python
# Menggunakan Fungsi Lambda
lambda angka: angka ** 2
```

Cara membacanya: `"Sebuah fungsi tanpa nama, yang menerima input 'angka', lalu langsung mengembalikan hasil dari 'angka dipangkatkan 2'."` (Perhatikan bahwa kita bahkan tidak perlu menulis kata return!).

### Kapan waktu yang tepat menggunakan Lambda

Fungsi sangat berguna ketika dioperasikan dengan fungsi lain seperti `filter()` dan `map()`.

Seperti ketika kita mencoba menyaring bilangan genap dari sebuah List. Dibanding kita membuat fungsi khusus untuk menyaring bilangan genap, kita bisa langsung menyisipkan `lambda` didalam filter.

```Python
# Menggunakna Lambda untuk menyaring nilai genap
angka = [1, 2, 3, 4, 5]

# Menyaring angka genap langsung dalam satu baris
angka_genap = list(filter(lambda x: x % 2 == 0, angka))

print(angka_genap)   # Hasil: [2, 4]
```

Di sini, lambda x: x % 2 == 0 bertindak sebagai fungsi "sekali pakai" yang mengecek apakah angka tersebut habis dibagi dua.

### Best Practice Lambda Function

Beberapa kesalahan yang sering dilakukan oleh Pemula.

- Jangan memberi nama pada fungsi tanpa nama (Lambda).

Sering kali pemula menyimpan fungsi Lambda ke dalam sebuah variabel (seolah-olah memberinya nama).

```Python
# Kesalahan dalam penggunaan Lambda oleh Pemula
angka = [1, 2, 3, 4, 5]

# JANGAN LAKUKAN INI! Ini menghilangkan esensi "Anonim" dari Lambda
kuadrat = lambda x: x ** 2 
hasil = list(map(kuadrat, angka))
```

Cara yang benar:

Jika fungsimu butuh nama karena akan dipanggil berkali-kali, gunakanlah def biasa!

```Python
angka = [1, 2, 3, 4, 5]

def kuadrat(x):
    return x ** 2

hasil = list(map(kuadrat, angka))
```

- Jangan Lambda yang terlalu rumit

Filosofi Python adalah kode harus mudah dibaca. Jika logikamu butuh if-else yang panjang dan rumus matematika yang rumit, jangan paksa dijejalkan ke dalam satu baris Lambda.

Cara yang salah:

```Python
hasil = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)
print(hasil) # Hasilnya 14, tapi matamu lelah membacanya
```

Cara yang benar:

Buatlah fungsi biasa yang rapi dan terstruktur. Komputer mungkin tidak peduli, tapi teman setimmu (atau dirimu di masa depan) akan sangat berterima kasih!

```Python
def hitung_rumus(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4

print(hitung_rumus(3)) # Hasilnya 14, dan sangat mudah dipahami!
```

## Kesimpulan

Gunakan Lambda jika kamu butuh fungsi sederhana, singkat, dan hanya dipakai sekali lewat (seperti di dalam map atau filter). Gunakan def jika logikanya mulai rumit atau akan digunakan berkali-kali di tempat lain!