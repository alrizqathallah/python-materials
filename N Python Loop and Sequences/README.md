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