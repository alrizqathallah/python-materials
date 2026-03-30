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