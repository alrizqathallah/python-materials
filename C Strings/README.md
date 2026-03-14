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
