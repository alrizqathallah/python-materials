# Variable and Data Types

## Tentang Variabel

**Mendeklarasikan Variabel**.

- Variabel ibarat sebuah kotak berlabel untuk menyimpan dan mereferensi data.

- Deklarasi dilakukan dengan menuliskan nama variabel, diikuti operator `=` dan nilai yang akan diberikan.

- Tidak memerlukan kata kunci seperti `let`, `const` atau `char`.

```Python
name = 'John Doe'  # string
age = 25           # integer
```

**Aturan Penamaan Variabel** (*Jika dilanggar akan menyebabkan `SyntaxError`).

- Harus diawali oleh huruf atau garis bawah (`_`), tidak boleh angka.

- Hanya boleh berisi karakter alfanumerik (a-z, A-Z, 0-9) dan garis bawah (_).

- Bersifat *case-sensitive*: `age`, `Age`, dan `AGE` dianggap berbeda.

- Tidak boleh menggunakan kata kunci (*reserved words*) Python, seperti `if`, `class`, `def`, dsb.

**Konvensi Penamaan** (*Gaya Penulisan yang Disarankan*).

- *Snake-case*: seluruh huruf kecil, kata dipisah dengan garis bawah.
  Contoh: `my_variable_name = 'freeCodeCamp'`

- *Gunakan nama deskriptif* agar mudah dipahami, misal `user_age` lebih baik dari `age`atau `ua`.

- *Hindari nama satu huruf* (kecuali untuk loop, seperti `i`, `j`, `k` yang sudah umum).
  `x = 56` (tidak jelas maksudnya), `total_score = 56` (lebih jelas maksudnya).

**Komentar** (`#`).

- Komentar diawali dengan tanda `#`; semua teks setelah `#` diabaikan Python.

- Bisa untuk satu bari:
  ```Python
  # Ini komentar satu baris
  ```

- Bisa juga beberapa baris dengan menuliskan `#` disetiap baris.

- Gunakan komentar untuk menjelaskan *alasan atau logika kode*, bukan menjelaskan maksud variabel - variabel seharusnya sudah jelas dari namanya.

## Fungsi `Print()` di Python

**Fungsi Dasar**

`print()` digunakan untuk menampilkan data ke terminal.

```Python
print('Hello World')  # Output: Hello World!
```

**String sebagai argumen**

Teks yang dicetak dituliskan didalam tanda kurung, diapit tanda kutip tungal `'` atau ganda `"`.

Contoh:

```Python
print("Halo")
print('Halo')
```

**Mencetak beberapa nilai sekaligus**

Pisahkan setiap nilai dengan koma (`,`).

Python secara otomatis menambahkan spasi diantara nilai-nilai tersebut.

Contoh:

```Python
print('Warna favorit saya', 'biru', 'hijau', 'merah')
# Output: Warna favorit saya biru hijau merah
```

**Kegunaan**

Memudahkan penggabungan beberapa informasi dalam satu baris tanpa perlu menggabungkan string secara manual.

## Tipe Data Umum di Python dan Cara Mendapatkan Tipenya

**Pengertian Tipe Data**

Tipe data menjelaskan jenis nilai yang disimpan dalam variabel, misalnya angka, teks, atau kumpulan data.

**Dynamic Typing di Python**

- Python menentukan tipe data secara otomatis berdasarkan nilai yang diberikan saat program berjalan.
- Tidak perlu mendeklarasikan tipe secara eksplisit seperti dibahasa statis (C# atau Java).
- Kelebihan: Cepat dan Fleksibel.
- Kekurangan: Kesalahan baru terdeteksi saat *runtime* (ketika baris kode dieksekusi), bukan saat dikompilasi.

**Perbedaan dengan Bahasa Statis**

- Bahasa statis (C++, Java, C#) memeriksa tipe saat kompilasi, sehingga kesalahan tipe dapat diketahui sebelum program dijalankan.
- Python baru mengetahui kesalahan tipe ketika kode yang bermasalah dijalankan.

**Tipe Data Umum dalam Python**

*Integer* `int`: Bilangan bulat.
```Python
my_int = 10
```

*Float* `float`: Bilangan desimal.
```Python
my_float = 4.5
```

*String* `str`: Teks(dalam kutip).
```Python
my_str = 'hello'
```

*Boolean* `bool`: Nilai kebenaran `True` / `False`.
```Python
my_bool = True
```

*Set* `set`: Koleksi unik tak berurutan.
```Python
my_set = {7, 'hello', 8.5}
```

*Dictionary* `dict`: Pasangan kunci nilai.
```Python
my_dict = {'name': 'Alice', 'age': 25}
```

*Tuple* `tuple`: Koleksi terurut, immutable.
```Python
my_tuple = (7, 'hello', 8.5)
```

*Range* `range`: Urutan angka (sering untuk perlungan).
```Python
my_range = range(5)
```

*List* `list`: Koleksi terurut, bisa berisi campuran tipe.
```Python
my_list = [22, 'Hello', 3.14, True]
```

*NoneType* `None`: Menyatakan tidak ada nilai.
```Python
my_none = None
```

**Cara Mendapatkan Tipe Variabel**

Fungsi `type()`, mengembalikan tipe data dalam format `<class '...'>`.

```Python
print(type(my_int))  # <class 'int'>
print(type(my_str))  # <class 'str'>
```

Fungsi `isinstance()`, memeriksa apakah suatu variabel bertipe tertentu; hasilnya `True` dan `False`.

```Python
isinstance('Hello', str)  # True
isinstance(42, float)     # False
```

Dengan memahami tipe data dan cara memeriksanya, kita dapat menghindari kesalahan yang mungkin muncul akibat ketidakcocokan tipe saat program berjalan.
