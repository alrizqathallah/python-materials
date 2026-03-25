# Python Strings

## Apa itu String dan String Immutability?

String adalah rangkaian karakter yang dibungkus dengan simbol kutip tunggal atau ganda. Dalam beberapa bahasa pemrograman rangkaian teks terbungkus kutip tunggal dan ganda memiliki perbedaan, namun hal tersebut bersifat sama di Python. Jadi dapat menggunakan kutip tunggal atau ganda untuk membuat string di Python.

```Python
# String
my_str1 = 'Hello'
my_str2 = "Hello"
```

Jika membutuhkan mulitine string dapat menggunakan triple kutip tunggal atau ganda.

```Python
# Multiline String
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''
```

Beberapa cara jika didalam rangkaian string memuat kutip tunggal atau ganda.

- Cara pertama dengan menggunakan tanda kutip yang berlawanan dengan pembungkus string.

```Python
# Opposite Symbol
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
```

- Cara kedua menggunakan escape sequence.

```Python
# Escape Sequence
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
```

Operator `in` digunakan untuk mengecek apakah satu atau lebih karakter terdapat dalam sebuah rangkaian string. Hasil dari operasi tersebut akan mengembalika nilai boolean, `True` jika karakter ada dalam rangkaian string, dan `False` jika karakter tidak ada dalam rangkaian string.

```Python
# Operator `in`
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
```

Fungsi `.len()` digunakan untuk mengecek panjang sebuah string, biasa disebut dengan pengindeksan (Indexing). Serta bekerja dengan karakter individual string tersebut.

```Python
# `len()` function
my_str = 'Hello world'
print(len(my_str))  # 11
```

Setiap karakter dalam sebuah string menempati posisi yang disebut dengan indeks. Sebuah indeks dimulai dari 0, karakter pertama pada sebuah string menempati indeks 0, dan karakter keduan menempati indeks 1, dan seterusnya.

Untuk mengakses karakter pada sebuah string dapat menggunakn _square-bracket_ `[]`, dengan nilai indeks yang ditentukan.

```Python
# String Index
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
```

Pengindeksan negatif juga diperbolehkan, sehingga Anda bisa mendapatkan karakter terakhir dari string apa pun dengan -1, karakter kedua dari belakang dengan -2, dan seterusnya:

```Python
# Negative Indexing
my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l
```

Pada umumnya bahasa pemrograman membedakan tipe data menjadi dua kelompok, _primitive_ dan _reference_. Tipe primitive adalah tipe data sederhana yang nilainya tidak dapat diubah (_Immutable_), yang tidak dapat dibuah setelah dideklarasikan. Sementara tipe reference, menyimpan banyak nilai dan nilai - nilai tersebut dapat dibuah (_mutable_).

Namun Python tidak membedakan secara tegas untuk keduanya, namun diperlakukan sama baik tipe primitive atau reference, secara umum semua tipe data diperlakukan sebagai objek. Terdapat beberapa tipe data yang tidak dapat diubah (_Immuteable_) dan sebagian bersifat (_mutable_).

Tipe data immuteable tidak dapat dibuah setelah dideklarasikan. Namun variabel terkait dapat diarahkan ke suatu yang baru, atau penugasan ulang (_Reassignment_), denga tidak dapat mengubah nilai aslinya.

String merupakan tipe data immutable.

```Python
# String is Immutable
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello
```

Namun, modifikasi langsung pada sebuah string tidak diperbolehkan.

```Python
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
```

Contoh tipe data immutable lainnya di Python adalah integer, float, boolean, tuple, dan range.

## Apa itu String Concatenation dan Interpolation?

Menggabungkan teks merupakan operasi umum yang akan ditemui ketika bekerja dengan string.

Di Python dapat menggabungkan string menggunakan operator `+`, Proses tersebut disebut dengan _String-Concatenation_.

```Python
# String Concatenation
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World
```

String concatenation hanya berlaku untuk sesama tipe data string, jika dipaksakan dengan tipe data lain, maka eror akan terjadi.

```Python
# TypeError
name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str
```

Hal tersebut dikarenakan Python tidak secara otomatis mengkonversikan tipe data selain string (integer) menjadi string untuk menggabungkannya. Python mengharuskan semua elemen merupakan string untuk menggabungkannya. Untuk mengatasi masalah tersebut, dapat menggunakan fungsi `str()`, untuk mengkonversikan integer menjadi string.

```Python
# str() Function
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26
```

Operator penugasan seperti `+=` juga dapat digunakan untuk penggabungan.

```Python
# Assigment Operator
name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26
```

String interpolation, merupakan sebuah proses dimana memasukan variabel dan ekspresi secara bersamaan kedalam string. Python memiliki kategori seperti `f-string`, yang memungkinkan untuk melakukan skema interpolasi dengan lebih mudah dan keterbacaan lebih baik.

F-string dimulai dengan huruf `f` sebelum tanda kutip, dan memungkinkan Anda untuk menyematkan variabel atau ekspresi di dalam bidang pengganti yang ditunjukkan oleh kurung kurawal ({}).

```Python
# F-string
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15
```

## Bagaimana itu String Slicing dan Cara Kerjanya?

Pada materi sebelumnya telah diketahui bahwa karakter pada rankaian string dapat diidentifikasi sesuai indeksnya, yang diakses melalui `[]`.

```Python
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1]) # d
```

String slicing memungkinkan untuk bekerja atau memilih bagian tertentu pada sebuah string, atau memilih sebagian string.

```
string[start:stop]
```

Jika hendak mengekstrak karakter string dari indeks tertentu ke lainnya, cukup dipisahkan dengan semicolon `:` bagian awal dan akhirnya.

```Python
# String Slicing
# string[start:stop]
my_str = 'Hello world'

print(my_str[1:4])   # ell
```

Perlu diketahui dalam contoh tersebut, index `stop` merupakan non-inklusif, artinya rangkaian hanya mengambil index 1 - 3 saja, tidak termasuk index 4.

Selain itu, indeks paling awal dan akhir rangkaian string dapat ditiadakan. Dimana indeks awal secara default akan ditetapkan dengan indeks 0, dan indeks akhir adalah indeks yang paling akhir pada rangkaian string sesuai panjang string tersebut.

```Python
my_str = 'Hello world'

print(my_str[:7])   # Hello w
print(my_str[8:])   # rld
```

Perlu ditekankan bahwa string slicing tidak dapat mengubah atau memodifikasi string itu sendiri.

Slicing juga dapat tidak menentukan index awal dan akhirnya untuk mencetak keseluruhan string.

```Python
my_str = 'Hello world'

print(my_str[:])   # Hello world
```

Selain parameter `start` dan `stop`, ada juga parameter `step`, yang digunakan untuk melakukan peningkatan pada setiap indeks.

```
string[start:stop:step]
```

Pada contoh berikut menunjukan ekstraksi dimulai dari indeks 0, dan diakhiri pada indeks sebelum 11, dan mengekstrak setiap setiap karakter kedua

```Python
my_str = 'Hello world'

print(my_str[0:11:2])   # Hlowrd
```

Juga sebuah trik untuk melakukan reverse terhadap string dengan memanfaatkan metode sebelumnya dengan menjadi parameter step menjadi `-1`.

```Python
my_str = 'Hello world'

print(my_str[::-1])   # dlrow olleH
```

## Method Umum Apa Saja yang Biasa digunakan di Python

Python menyediakan beberapa method string bawaan untuk mempermudah pekerjaan string.

- Uppercase: `upper()`, digunakan untuk mengkonversi string menjadi bentuk karakter kapital (huruf besar).

```Python
# upper()
my_str = 'hello world'

upper_my_str = my_str.upper()
print(upper_my_str)   # HELLO WORLD
```

- Lowercase: `lower()`, digunakan untuk mengkoversi karakter kedalam format lower (huruf kecil).

```Python
# lower()
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)   # hello world
```

- Strip: `strip()`, digunakan untuk menghilangkan whitespace yang terdapat diawal dan akhir pada sebuah string.

```Python
# strip()
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)   # "hello world"
```

- Replace: `replace(old, new)`, menggantikan elemen string lama dengan yang baru.

```Python
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replace_my_str)   # hi world
```

- Split: `split(seperator)`, digunakan untuk memisahkan sebuah string berdasarkan pemisah yang ditentukan, jika tidak ada pemisah, maka akan dipisah berdasarkan spasi.

```Python
# split()
my_str = 'hello world'

split_words = my_str.split()
print(split_words)   # ['hello', 'world']
```

- Join: `join(iterable)`, digunakan untuk menggabungkan string berdasarkan seperator atau pemisah.

```Python
# join()
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)   # hello world
```

- Startswith: `startswith(prefix)`, digunakan untuk mengidentifikasi string diawali oleh prefix tertentu, dan akan mengembalikan nilai boolean.

```Python
# startswith()
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(start_with_hello)   # True
```

- Endswith: `endswith(suffix)`, digunakan untuk mengidentifikasi string diakhiri oleh suffix tertentu, dan akan mengembalikan nilai boolean.

```Python
# endswith()
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)   # True
```

- Find: `find(subtring)`, mengembalikan indeks kemunculan pertama substring, atau -1 jika tidak ditemukan.

```Python
# find()
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)   # 6
```

- Count: `count(substring)`, digunakan untuk menampilkan berapa kali elemen karakter muncul pada rangkaian string.

```Python
# count()
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)   # 2
```

- Capitalize: `capitalize()`, digunakan untuk mengembalikan string baru dengan karakter pertama berupa huruf kapital dan karakter lainnya berupa huruf kecil.

```Python
# capitalize()
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
```

- Is Upper: `isupper()`, mengembalikan nilai True jika semua huruf dalam string adalah huruf besar dan False jika tidak.

```Python
# isupper()
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False
```

- Is Lower, `islower()`, mengembalikan nilai True jika semua huruf dalam string adalah huruf kecil dan False jika tidak.

```Python
# islower()
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True
```

- Title: `title()`, mengembalikan string baru dengan huruf pertama setiap kata dikapitalisasi.

```Python
# title()
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```