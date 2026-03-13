# Variabel dan Tipe Data

## Variabel

Variabel merupakan konsep yang akan ditemui disetiap bahasa pemrograman.

Fungsi dari variabel adalah wadah atau tempat untuk suatu nilai disimpan dengan tipe data tertentu.

Mendeklarasikan variabel di Python cukup mudah, karena tidak menggunakan kata kunci tertentu untuk mendeklatasikannya.

Cukup dengan menuliskan nama variabel dan diikuti dengan operator penugasan.

```Python
name = 'John Doe'
age = 25
```

Dalam contoh tersebut variabel `name` menyimpan nilai 'John Doe', dimana nilai tersebut adalah `string`.

Tipe data teks atau `string` di Python, ditulis menggunakan tanda kutip, baik itu kutip satu `'` atau kutip dua `"`, keduanya dapat digunakan. Namun disarankan untuk konsisten dalam penggunaannya.

Contoh seperti `'Hello'` dan `"World"`.

### Aturan Penamaan Variabel

- Penamaan variabel di Python harus dimulai dengan huruf atau *underscore* `_`.

- Penamaan variabel di Python hanya dapat menampung karakter alpanumerik seperti `a-z`, `A-Z`, `0-9` dan `_`.

- Python memiliki aturan penamaan variabel yang `case-sensitive`, artinya sebuah kata tidak boleh sama secara susunan atau bentuk, meski memiliki makna yang sama. Seperti `name` dengan `Name` adalah bentuk yang berbeda, meski memiliki makna yang sama.

- Penamaan variabel tidak boleh menggunakan kata yang telah dikunci oleh Python, atau kata yang dipergunakan untuk sintaks, seperti `if`, `class` atau `def` dan lainnya.

Jika kita salah dalam menuliskan nama variabel, maka akan muncul eror dalam bentuk pengembalian.

```Python
5variable_name = 5

# SyntaxError: invalid syntax
```

### Format Penamaan Variabel di Python

Secara umum, setiap bahasa pemrograman memiliki format penamaan variabel yang berbeda, meski hal tersebut bukanlah hal yang mutlak. Namun setiap pengguna bahasa pemrograman tertentu memiliki kebiasaan dan budaya tertentu dalam format penulisannya.

Di Python, format penulisan variabel yang paling umum digunakan adalah format `snake_case`.

Nama variabel menggunakan huruf kecil, jika nama lebih dari satu kata, digunakan `_` sebagi ruang atau pemisah kata tersebut.

Penaamaan variabel di bahasa pemrograman apapun tidak boleh mengandung *spasi*, jika tanpa sengaja terdapat spasi maka sintaks dianggap error.

```Python
my_variable_name = 'freeCodeCamp'
```

Kemudian, nama sebuah variabel haruslah deskriptif dengan nilai yang ditampung.

Nama harus menggambarkan isi dari data yang terdapat pada variabel

```Python
user_age = 25
```

Penggunaan `user_age` lebih baik dari penggunaan `age`, karena lebih informatif dan deskriptif.

Hal tersebut sangat berguna jika seubah proyek sudah ditangani oleh tim dengan komposisi yang besar, karena lebih informatif dan tersampaikan dengan baik.

Jangan pernah membuat variabel dengan satu huruf saja, kecuali pada proses pembelajaran. Karena dapat membingungkan pengguna dan orang lain yang melihat kode yang ditulis.

```Python
x = 56 # Apa yang dimaksud dengan x?
```

Berbeda kasus ketika dalam penggunaan fungsi perulangan, penggunaan nama dengan satu huruf dapat diterima karena ada kondisi tertentu pada bentuk kode yang ditulis, agar lebih ringkas.

## Komentar

Dalam bahasa pemrograman terdapat fitur *comments*, yang digunakan oleh pengguna untuk memnuliskan catatan.

Komentar tidak akan dibaca oleh interpreter atau kompilator, sehingga tidak akan ikut ditampilkan ketika kode dieksekusi.

Hanya untuk keperluan pengguna saja.

Di Python untuk membuat komentar dapat menggunakan simbol `#` atau `'''` yang ditutup dengan `'''`.

```Python
# Ini Komentar

username = 'freeCodeCamp' # Ini komentar satu baris

'''
Ini
Komentar
Multi-baris
'''
```

## Fungsi Print

Setiap bahasa pemrograman memiliki fungsi, metode, atau kata kunci bawaan yang digunakan untuk menampilkan data.

Python menggunakan fungsi `print()` untuk menampilkan data.

```Python
print('Hello World!')
# Output: Hello World!
```

Teks 'Hello World' adalah `string`, string merupakan tipe data teks, dimana perlu membungkusnya dengan simbol kutip, `'` atau `"`, agar dikenali sebagai sebuah data string.

Dengan simbol koma `,`, pengguna bisa membuat beberapa output teks dalam satu fungsi print.

```Python
print('My favorite colors are', 'red', 'green', 'blue')
# Output: My favorite colors are red green blue
```

Secara otomatis Python akan memberikan spasi disetiap akhir koma pada output.

## Tipe Data di Python

Setiap variabel akan menyimpan sebuah nilai dengan tipe data tertentu. 

Bahasa pemrograman memanfaatkan tipe data untuk memlakukan suatu proses kerja dan informasi tertentu.

Python memiliki tipe data yang dinamis, seperti JavaScript. Pengguna tidak perlu mempersiapkan secara eksplisit sebuah variabel untuk tipe data tertentu. Secara otomatis Pyton akan mengenali variabel dengan tipe data tertentu setelah nilai ditugaskan pada variabel.

```Python
name = 'John Doe' # Python mengenali sebagai tipe data string
age = 25 # Python mengenali sebagai tipe data integer
```

Berbeda dengan beberapa bahasa pemrograman lain seperti Java atu C# yang perlu memepersiapkan variabel dengan tipe data tertentu sebelum nilai ditugaskan pada variabel.

Kondisi tersebut membuat penulisan kode menjadi lebih cepat dan fleksibel. Namun kondisi tersebut juga akan menimbulkan beberapa *bug*, karena kesalahan akan diketahui setelah program dijalankan, bukan ketika dikompilasi.

Secara kerja menggunakan sistem interpreter, dimana Python akan menajalankan program dan membaca baris kode satu persatu, dari atas ke bawah. Ketika Python sampai dibaris dimana letak kesalahan terjadi, maka program akan berhenti dijalankan dan menampilkan pesan eror.

Sementara untuk beberapa bahasa pemrograman lain yang menggunakan sistem kompilasi. Kesalahan akan lebih dulu diketahui ketika kode program dikompilasi, jika terdapat eror, maka kompilasi akan terhenti dan kesalahan dapat diketahui sebelum program benar-benar dijalankan.

Sehinga kesalahan pada kode program Python tidak akan benar-benar diketahui, sampai interpreter membaca pada bagian yang terjadi kesalahan.

Berikut beberapa tipe data yang umum di Python:

- *Integer*: merupakan bentuk data dalam bilangan bulat.
- *Float*: merupakan bilangan dalam bentuk desimal.
- *String*: merupakan tipe data teks, atau sekumpulan karakter.
- *Boolean*: merupakan tipe data yang merepresentasikan benar *True* atau salah *False*.
- *Set*: merupakan kumpulan elemen berbeda yang tidak berurut.
- *Dictionary*: merupakan kumpulan pasangan kunci *key* dengan nilai *value* (*key-valur pair*).
- *Tuple*: merupakan kumpulan koleksi berurut yang tidak berubah, diapit dengan tanda kurung.
- *Range*: merupakan urutan bilangan, biasa digunakan untuk perulangan.
- *List*: merupakan kumpulan berurut denga bermacam tipe data.
- *None*: merupakan tipe data khusus yang mewakili ketiadaan suatu nilai.

```Python
my_integer_var = 10
print('Integer:', my_integer_var)

my_float_var = 4.50
print('Float:', my_float_var)

my_string_var = 'hello'
print('String:', my_string_var)

my_boolean_var = True
print('Boolean:', my_boolean_var)

my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var) # Set: {7, 'hello', 8.5}

my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var)

my_tuple_var = (7, 'hello', 8.5)
print('Tuple:', my_tuple_var)

my_range_var = range(5)
print('Range:', my_range_var)

my_list = [22, 'Hello world', 3.14, True]
print(my_list)

my_none_var = None
print('None:', my_none_var)
```

Pengguna bisa menggunakan fungsi `type()`, untuk mengetahui tipe data dari sebuah variabel.

```Python
my_var_1 = 'Hello world'
my_var_2 = 21

print(type(my_var_1)) # <class 'str'>
print(type (my_var_2)) # <class 'int'>
```

Berikut tipe data yang akan muncul diterminal ketikan dicek:

```Python
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>
```

Fungsi bawaan seperti `isinstance()` memungkinkan pengguna untuk mengecek variabel denga tipe data tertentu.

Fungsi akan menerima objek dan tipe data yang akan diperiksa, kemudian hasilnya akan dikembalikan dalam bentuk boolean.

```Python
isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False
```