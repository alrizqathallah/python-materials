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
