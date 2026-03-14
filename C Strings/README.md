# Strings

## Pengertian String

String adalah tipe data, merupakan serangkaian kumpulan karakter yang dibungkus tanda kutip, baik kutip satu atau kutip dua.

Terkadang dalam bahasa pemrograman lain, kumpulan karakter yang diapit dengan kutip satu berbeda dengan kumpulan karakter yang diapit kutip dua. Namun Python memberlakukan secara sama, jadi string di Python dapat diapit dengan kutip satu atau dua.

```Python
my_str_1 = 'Hello'
my_str_2 = "World"
```

Pengguna juga bisa menggunakan metode multiline string menggunakan kutip satu atau dua.

```Python
my_str_3 = '''Multiline
string'''
my_str_4 = """Another
Multiline
String"""
```

Jika dalam string terdapat tanda kutip satu atau dua, terdapat dua cara untuk melakukannya

- Pengguna dapat membuat string menggunakan pembungkus dengan kutip yang berlawanan.

```Python
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
```

- Menggunakan escape sequence untuk melakukannya:

```Python
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
```

Terkadang pengguna ingin mengecek, apakah sebuah karakter ada didalam sebuah string.

Untuk melakukannya, pengguna bisa menggunakan operator `in`.

Operator tersebut akan mengembalikan nilai boolean, jika karakter ada didalam string, maka akan mengembalikan nilai True, jika tidak ada maka akan mengembalikan nilai False.

```Python
my_str = 'Hello World'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
```

Dalam kasus lain, pengguna juga ingin mengecek panjang string.

String memiliki sifat seperti array, jadi penggunan bisa mengecek berapa panjang string tersebut menggunakan fungsi `len()`.

```Python
my_str = 'Hello world'
print(len(my_str))  # 11
```

Secara spesifik juga dapat mengecek isi dari index sebuah string.

Menggunakan `[]` untuk mengecek secara spesifik.

```Python
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
```

Pengindeksan negatif juga diperbolehkan, sehingga Anda bisa mendapatkan karakter terakhir dari string apa pun dengan -1, karakter kedua dari belakang dengan -2, dan seterusnya:

```Python
my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l
```

Dalam banyak praktik, sebuah bahasa pemrograman biasanya membedadkan antara tipe data primitif dan referensi.

Tipe data primitif adalah tipe data yang memiliki nilai sederhana dan tidak dapat diubah (immutable).

Sementar tipe data referensi adalah tipe data yang miliki nilai kompleks (beragam) dan dapat diubah (mutable), dan ada sebagian juga yang (immutable).

Python tidak mebedakan tipe data seperti komposisi tersebut, namun lebih diperlakukan seperti objek.

Tipe data immutable tidak dapat diubah setelah variabel dideklarasikan dan nilai ditugaskan, Namun dapat diarahkan untuk dilakukan penugasan ulang.

```Python
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello
```

String adalah tipe data immutable, nilai pada string tidak dapat diubah. Tetapi memodifikasi secara paksa juga tidak dapat dilakukan.

```Python
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
```

## String Concatenation dan String Interpolation

Dalam Python, pengguna bisa mengkombinasikan beberapa string menggunakan operator `+`.

Proses tersebut dikenal dengan string concatenation.

```Python
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str)
```

Penggunaan string concatenation hanya berlaku untuk sesama data string, tidak bisa digunakan untuk tipe data lainnya.

```Python
name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str
```

Jika pada suatu kondisi perlu untuk melakukan penggabungan tersebut, maka tipe data yang bukan string harus dikonversi menjadi tipe data string.

Hal tersebut dapat dilakukan dengan menggunakan operator casting `str()`.

```Python
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26
```

Pengguna juga bisa menggunakan operator augmentasi untuk melakukan concatenation.

Seperti `+=`.

```Python
name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26
```

Proses memasukan variabel dan ekpresi kedalam sebuah string disebut dengan interpolation.

Python memiliki fungsi `f-string` yang dapat melakukan tugas tersebut.

```Python
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15
```

## String Slicing

Sebelumnya telah diketahui bahwa karakter pada string dapat diidentifikasi berdasarkan indeks menggunakan *bracket notation*.

```Python
my_str = 'Hello World!'

print(my_str[0]) # H
print(my_str[2]) # l
print(my_str[-1]) # !
```

Dengan string slicing memungkinkan pengguna untuk mengidentifikasi sebagian dari sebuah string atau hanya bagian tertentu pada string.

```Python
string[start:stop]

my_str = 'Hello World!'
print(my_str(1:4)) # ell
```

Pengguna bisa mengekstrak karakter dari indeks tertentu ke indeks lain, cukup dipisahkan dengan titik dua `:`.

Perlu diperhatikan bahwa penentuan indeks tidak bersifat inklusif.

Jadi `[1:4]` hanya mengekstrak karakter dari indeks `1` hingga `3`, tidak termasuk indeks `4`.

Pengguna juga bisa menghilangkan indeks awal dan akhir, yang secara default akan menggunakan indeks paling pertama `0` atau indeks akhir.

```Python
my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str[:8]) # Hello wo
```

Selain indeks awal dan akhir, terdapat juga parameter langkah opsional, yang digunakan untuk menentukan peningkatan antara setiap indeks dalam irisan.

```Python
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd

my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH
```

## String Method

Python menyediakan sejumlah metode string bawaan yang dapat digunakan oleh pengguna.

- `upper()`: mengembalikan string baru dengan semua karakter diubah menjadi besar atau uppercase.
- `lower()`: mengembalikan string baru dengan semua karakter dibuah menjadi lowercase atau kecil.
- `strip()`: mengembalikan string baru dengan menghilangkan whitespace diawal dan akhir pada string.
- `replace(old, new)`: Mengembalikan string baru dengan semua kemunculan kata "old" digantikan oleh "new".
- `split(separator)`: Memisahkan string berdasarkan pemisah yang ditentukan menjadi daftar string. Jika tidak ada pemisah yang ditentukan, pemisahan dilakukan berdasarkan spasi.
- `join(iterable)`: Menggabungkan elemen-elemen dari sebuah iterable menjadi sebuah string dengan pemisah.
- `startswith(prefix)`: Mengembalikan nilai boolean yang menunjukkan apakah sebuah string diawali dengan awalan yang ditentukan.
- `endswith(suffix)`: Mengembalikan nilai boolean yang menunjukkan apakah sebuah string diakhiri dengan akhiran yang ditentukan.
- `find(substring)`: Mengembalikan indeks kemunculan pertama substring, atau -1 jika tidak ditemukan.
- `count(substring)`: Mengembalikan jumlah kemunculan suatu substring dalam sebuah string.
- `capitalize()`: Mengembalikan string baru dengan karakter pertama dikapitalisasi dan karakter lainnya dihuruf kecil.
- `isupper()`: Mengembalikan True jika semua huruf dalam string adalah huruf besar dan False jika tidak.
- `islower()`: Mengembalikan True jika semua huruf dalam string adalah huruf kecil dan False jika tidak.
- `title()`: Mengembalikan string baru dengan huruf pertama setiap kata dikapitalisasi.

```Python
my_str = 'Hello World'

# upper
uppercase_str = my_str.upper()
print(uppercase_str)  # HELLO WORLD

# lower
lowercase_str = my_str.lower()
print(lowercase_str)  # hello world

my_str_2 = '  Hello World  '

# strip
strip_str = my_str_2.strip()
print(my_str_2)  # '  Hello World  '
print(strip_str)  # 'Hello World'

my_str_3 = 'hello world'

# replace
replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world

my_list = ['hello', 'world']

#join
joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world

my_str = 'hello world'

# startswith
starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

my_str = 'hello world'

# endswith
ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True

my_str = 'hello world'

# find
world_index = my_str.find('world')
print(world_index)  # 6

my_str = 'hello world'

# count
o_count = my_str.count('o')
print(o_count)  # 2

my_str = 'hello world'

# capitalize
capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

my_str = 'hello world'

# isupper
is_all_upper = my_str.isupper()
print(is_all_upper)  # False

my_str = 'hello world'

# islower
is_all_lower = my_str.islower()
print(is_all_lower)  # True

my_str = 'hello world'

# title
title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```
