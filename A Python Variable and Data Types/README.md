# Python Variable

## Bagaimana Cara Mendeklarasikan Variabel dan Menamakan Variabel?

Di Python, Variabel seperti kotak berlabel yang digunakan untuk menyimpan dan mereferensikan berbagai jenis data.

Untuk mendeklarasikan variabel di Python, perlu menugaskan nilai menggunakan operator `=`. Tidak memerlukan kata kunci khusus seperti `var`, `let` atau `const`.

Di Python, cukup menuliskan nama variabel disebelah kiri, kemudian diikuti operator `=` dan nilai disebelah kanan. Seperti contoh berikut:

```Python
name = 'John Doe'
age = 25
```

Dalam contoh tersebut, variabel `name` menyimpan nilai `'John Doe'`, Nilai tersebut merupakan sebuah `string`, merupakan sekumpulan karakter yang merepresentasikan sebuah teks. String ditulis menggunakn `'` single quote atau `"` double qoute, `'Hello'` atau `"Hello"`.

Beberapa aturan penting dalam penamaan variabel di Python:

- Penamaan variabel di Python hanya bisa dimulai dengan huruf atau `_`, tidak boleh dimulai dengan angka atau bilangan.
- Nama variabel hanya dapat dimuat dengan karakter alfanumerik (a-z), (A-Z), (0-9) dan _.
- Nama variabel bersifat `case-sensitive`, `age`, `Age` dan `AGE` dianggap unik dan berbeda.
- Nama variabel tidak boleh menggunakan kata kunci atau kata khusus yang sudah ditetapkan oleh Python, seperti `if`, `class` atau `def`.
- Jika sengaja memberi nama variabel diluar aturan tersebut maka program akan mengembalikan `SyntaxError`.

Format penamaan variabel di Python, umumnya menggunakan format `snake_case`. Kata pertama harus menggunakan huruf kecil, dan dipisah dengan _.

```Python
my_variable_name = 'freeCodeCamp'
```

Dalam penamaan variabel harus menggunakan nama yang deskriptif. Seperti contoh umur pengguna, `user_age` lebih baik dari `age` atau disingkat `ua`.

```Python
user_age = 30
```

Selanjutnya, juga disarankan tidak menggunakan huruf tunggal dalam penamaan variabel.

```Python
x = 56
```

Dengan pengecualian ketika menggunakan loop dan operasi serupa, huruf tunggal sudah jamak digunakan.

Komentar `comments`, simbol `#` yang diikuti kalimat disebut dengan komentar. Di Python membuat komenatar menggunakn simbol `#` diawal dan diikuti kata / kalimat catatan yang diberikan.

```Python
# This is Comments

# This
# is
# Comments
```

## Bagaimana Fungsi Print Bekerja?

Setiap bahasa pemrograman memiliki cara tersendiri untuk menampilkan data ke terminal denga method bawaan, fungsi, properti, atau kata kunci.

Python menggunakan fungsi `print()` untuk mencetak data ke terminal.

```Python
print('Hello World!')
```

Fungsi print juga dapat mencetak argumen lebih dari satu,

```Python
print('My favorite colors are', 'blue', 'green', 'red')

# Output: My favorite colors are blue green red
```

## Apa Tipe Data yang Umumnya Digunakan di Python dan Bagaimana Cara Mengetahui Variabel dengan Tipe Data Tertentu?

Sangat penting untuk mengetahui apa itu tipe data, karena tipe data mendeskripsikan nilai yang dipegang oleh sebuah variabel.

Python adalah bahasa pemrograman dinamis, `dynamic-typed` language. Python mengerti tipe data sebuah variabel berdasarkan nilai yang ditugaskan pada variabel tersebut.

```Python
name = 'John Doe'   # Python mengetahui bahwa ini adalah string.
age = 25            # Python mengetahui bahwa ini adalah sebuah integer.
```

Dengan dynamic-typed, membuat penulisan kode lebih cepat dan fleksibel, namun dapat mendatangkan eror yang tidak terduga sebelum kode dijalankan, bukan ketika dikompilasi.

Python akan mengeksekusi kode baris per baris, dan jika terdapat eror pada baris yang ditemui, maka eksekusi akan berhenti dan mengembalikan eror.

Berbeda dengan bahasa pemrograman lain yang ketika terjadi error sudah dapat diketahui sejak kode dikompilasi, sehingga kesalahan dapat diketahui sebelum program dijalankan.

Beberapa tipe data di Python:

- `Integer`, bilangan bulat tanpa desimal, dapat berbentuk positif atau negatif.
```Python
my_integer_var = 10

Print('Integer: ', my_integer_var) # Integer: 10
```

- `Float`, bilangan dengan desimal seperti `4.4` atau `-0.4`.
```Python
my_float_var = 4.50
print('Float: ', my_float_var)   # Float: 4.5
```

- `String`, sebuah rangakaian karakter yang dibungkus dengan single quote atau double quote.
```Python
my_string_var = 'hello'
print('String: ', my_string_var)   # String: hello
```

- `Boolean`, sebuah tipe data yang mengembalikan kebenaran, `True` atau `False`.
```Python
my_boolean_var = True
print('Boolean: ', my_boolean_var)   # Boolean: True
```

- `Set`, sebuah koleksi tek berurut dari elemen berbeda, `{0.5, 4, 'apple'}`.
```Python
my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var) # Set: {7, 'hello', 8.5}
```

- `Dictionary`, Kumpulan pasangan kunci-nilai yang diapit dalam tanda kurung kurawal.
```Python
my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}
```

- `Tuple`, Koleksi terurut yang tidak berubah, diapit dalam tanda kurung, seperti `('apel', 4.5, 7)`.
```Python
my_tuple_var = (7, 'hello', 8.5)
print('Tuple:', my_tuple_var) # Tuple: (7, 'hello', 8.5)
```

- `Range`, Urutan angka, sering digunakan dalam perulangan, misalnya, `range(5)`.
```Python
my_range_var = range(5)
print('Range:', my_range_var) # Range: range(0, 5)
```

- `List`, Kumpulan elemen yang terurut yang mendukung berbagai tipe data.
```Python
my_list = [22, 'Hello world', 3.14, True]
print(my_list) # [22, 'Hello world', 3.14, True]
```

- `None`, Nilai khusus yang mewakili ketiadaan suatu nilai.
```Python
my_none_var = None
print('None:', my_none_var) # None: None
```

Untuk mendapatkan tipe data dari sebuah variabel dapat menggunakan operator `type()`.

```Python
my_var_1 = 'Hello world'
my_var_2 = 21

print(type(my_var_1)) # <class 'str'>
print(type (my_var_2)) # <class 'int'>
```

Dan berikut adalah semua tipe data yang dibahas dalam pelajaran ini, beserta tipe datanya di terminal.

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

Fungsi bawaan `isinstance()` memungkinkan Anda memeriksa apakah suatu variabel cocok dengan tipe data tertentu. Fungsi ini menerima sebuah objek dan tipe data yang ingin Anda periksa, kemudian mengembalikan nilai boolean. Berikut beberapa contohnya:

```Python
isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False
```