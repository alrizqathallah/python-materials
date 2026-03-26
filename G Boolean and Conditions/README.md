# Boolean and Condition

## Bagaimana Statement Pengkondisian dan Operator Logika Bekerja?

Conditional Statements, atau pengkondisian, memungkinkan untuk mengatur alur program yang didasarkan kondisi tertentu yaitu True (Benar) atau False (salah).

**Comparasion Operator**

Operator Komparasi digunakan untuk membandingkan dua nilai atau lebih dan mengembalikan nilai boolean.

- `==`, digunakan untuk mengecek apakah nilai setara.
- `!=`, digunakan untuk mengecek apakah nilai tidak setara.
- `>`, digunakan untuk mengecek apakah nilai lebih besar.
- `<`, digunakan untuk mengecek apakah nilai lebih kecil.
- `>=`, digunakan untuk mengecek apakah nilai lebih besar dan setara.
- `<=`, digunakan utnuk mengecek apakah nilai lebih kecil dan setara.

Berikut beberapa contoh ekspresi yang menghasilkan True atau False.

```Python
# Comparasion Operator
print(3 > 4)    # False
print(3 < 4)    # True
print(3 == 4)   # False
print(4 == 4)   # True
print(3 != 4)   # True
print(3 >= 4)   # False
print(3 <= 4)   # True
```

Di Python penggunaan pengkondisian (percabangnan) dasar umumnya menggunakan `if` statement.

```Python
if condition:
  pass # Kode dieksekusi jika kondisi bernilai True
```

- if statement menggunakan kata kunci `if`.
- Pengkondisian (percabangan) merupakan operasi yang menghasilkan True (benar) dan False (salah), diikuti semicolon `:`.
- Diikuti blok kode dibawah statement pengkondisian. Python menggunakan indentasi untuk mendefinisikan blok kode.

Pada contoh di atas, isi dari pernyataan if berisi pernyataan pass. Ketika pernyataan pass dieksekusi, tidak terjadi apa pun. Ini adalah kata kunci khusus yang dapat digunakan sebagai tempat penampung untuk kode di masa mendatang dan berguna ketika blok kode kosong tidak diizinkan.

Kode didalam body hanya akan dieksekusi jika operasi menghasilkan nilai True.

```Python
# if Statement
age = 18

if age >= 18:
  print('You\'re and adult')
```

Sangat perlu diperhatikan indentasi pada blok kode, pada contoh tersebut `print` memiliki indentasi yang mengindikasikan statement print masuk kedalam blok kode.

Jika pengguna lupa atau sengaja tidak menambahkan indentasi, maka akan terjadi `IndentationError`.

```Python
age = 18

if age >= 18:
print('You are an adult') # IndentationError: expected an indented block after 'if' statement on line 3
```

Selain statement `if`, ada juga statement `else` yang akan dieksekusi jika nilai `if` mngahasilkan False.

```Python
# Else Condition
age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet') # You are not an adult yet
```

Pada contoh diatas, statement `else` akan secara otomatis dieksekusi ketika `if` menghasilkan kondisi false.

Mungkin ada suatu kondisi, dimana terdapat pengkondisian alternatif selain If (True) dan Else (False). `elif` merupakan statement pengkondisian alternatif anatara `if` dan `else`.

```Python
# elif Statement
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child
```

dan Statment Elif dapat dibuat sebanyak yang diinginkan.

```Python
# Conditional
age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant
```

## Apa itu Nilai Truthy dan Falsy, Serta Bagaimana Operator Boolean dan Short-Circuiting Bekerja?

Terkadang akan ada kondisi dimana terjadi "nested" condition, seperti berikut.

```Python
# Example
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
```

Dalam contoh tersebut, pertama mengecek apakah `is_citizen` bernilai True. Jika benar, maka akan dilanjutkan pada statement `if` selanjutnya, dengan mengecek apakah `age` lebih dari 18. Jika benar, maka statement print "You ara eligible to vote" akan dieksekusi. Jika tidak untuk kedua statement tersebut, maka print `else` akan dieksekusi.

Dalam kondisi tertentu, selain menggunakan `if` statement, pengguna juga bisa menggunakan operator pengkondisian lain yang lebih kompleks seperti `and`, `or` dan `not`.

Di Python dan bahasa pemrograman lain biasanya terdapat nilai yang secara bawaan bersifat True atau False. Nilai yang memiliki sifat bawaan True disebut Truthy dan nilai yang memiliki sifat bawaan False disebut dengan Falsy.

Beberapa nilai Falsy.

- `None`
- `False`
- Intger `0`
- Float `0.0`
- Empty Sting `""` (string kosong)

Nilai-nilai tersebut merupakan nilai Falsy, sedangkan untuk setiap nilai diluar nilai-nilai tersebut akan bersifat Truthy. Sekalipun `" "` terlihat seperti empty string namun ada karakter spasi didalamnya, yang membuat bersifat Truthy.

Pengguna bisa menggunakan operator `bool()` untuk mengecek apakah sebuah nilai itu bersifat Truthy atau Falsy. Serta akan mengembalikan nilai dalam bentuk boolean, jika hasilnya True maka nilai tersebut Truthy, jika False maka Falsy.

```Python
# Truthy dan Falsy
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True
```

Mari mengetahui tentang boolean operator.

**`and` operator**. 

Operator `and` akan akan mengevaluasi dua nilai (operand) dan akan mengembalikan nilai pertama jika nilai tersebut falsy, sebalinya akan mengembalikan nilai kedua jika nilai pertama Truthy. Dalam operator logika `and` nilai yang dioperasikan harus sama-sama bersifat Truthy agar menghasilkan operasi yang benar.

```Python
# and Operator
is_citizen = True
age = 25

print(is_citizen and age) # 25
```

Pada contoh di atas, angka 25 dicetak ke terminal karena operator `and` akan mengevaluasi operan kedua jika operan pertama bernilai `True`. Operator `and` dikenal sebagai operator sirkuit pendek. Sirkuit pendek berarti Python memeriksa nilai dari kiri ke kanan dan berhenti segera setelah menentukan hasil akhir.

Pengguna juga dapat menggunakan `and` dan `if` secara bersamaan untuk mengecek multiple conditions.

```Python
# if dan `and`
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
```

Inti dari operator `and` adalah, tidak mengizinkan satupun operand (nilai) bersifat false, semua operand harus mengembalikan nilai true.

**`or` operator**

Operator `or` bersifat lebih ringan, dimana cukup salah satu nilai (operand) bernilai True, maka operasi akan bernilai True.

```Python
# or
age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')
```

**`not` operator**

Operator ini adalah "pembantah". Fungsinya hanya satu: membalikkan nilai. Jika sesuatu itu benar, `not` akan menjadikannya salah, dan sebaliknya.

```Python
# not
is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')
```