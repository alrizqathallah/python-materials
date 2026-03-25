# Python Numbers and Mathematical Operations

## Bagaimana Bekerja Dengan Bilangan Integer dan Float?

Integer dan Float adalah tipe data bilangan utama di Python, dengan keduanya, pengguna dapat menyimpan data bilangan dan mengoperasikannya dengan operator matematika.

**Integer**

Integer adalah bilangan bulat tanpa desimal (koma), baik itu positif atau negatif.

```Python
# Integer Number
my_int_1 = 56
my_int_2 = -4

print(type(my_int_1))   # <class 'int'>
print(type(my_int_2))   # <class 'int'>
```

Berikut merupakan cara untuk melakukan penjumlahan menggunakan bilangan integer.

```Python
# Addition
my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints)   # Integer Addition: 68
```

Berikut untuk mengoperasikan pengurangan dengan integer.

```Python
# Subtraction
my_int_1 = 56
my_int_2 = 12

diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints)   # Integer Subtraction: 44
```

Berikut untuk melakukan perkalian.

```Python
# Multiplication
my_int_1 = 12
my_int_2 = 4

product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints)   # Integer Multiplication: 48
```

Berikut untuk melakukan pembagian dengan integer.

```Python
# Division
my_int_1 = 56
my_int_2 = 12

div_ints = my_int_1 / my_int_2
print('Integer Division:', div_ints) # Integer Division: 4.666666666666667
```

**Floats**

Float adalah bilangan desimal, baik itu positif atau negatif.

```Python
# Float
my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>
```

Operasi penjumlahan dengan float.

```Python
# Addition
my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition) # Float Addition: 17.4
```

Operasi pengurangan dengan float.

```Python
# Subtraction
my_float_1 = 5.4
my_float_2 = 12.0

float_subtraction = my_float_2 - my_float_1
print('Float Subtraction:', float_subtraction) # Float Subtraction: 6.6
```

Operasi perkalian dengan float.

```Python
# Multiplication
my_float_1 = 5.4
my_float_2 = 12.0

float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication) # Float Multiplication: 64.80000000000001
```

Operasi pembagian dengan float.

```Python
# Division
my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1
print('Float Division:', float_division) # Float Division: 2.222222222222222
```

Jika penjumlahan dilakukan antara bilangan Integer dan Float, maka hasil penjumlahan akan otomatis dikonversi dalam bentuk float.

```Python
# Addition: Integer + Float
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>
```

Hal tersebut berlaku juga untuk operasi matematika dasar lainnya, seperti pengurangan, perkalian dan pembagian. Jika bilangan integer di operasikan dengan bilangan float maka hasil yang akan dikembalikan adalah float.

Operasi matematika yang lebih lanjut juga dapat dilakukan seperti pembagian dua bilangan dan modulo, pembagian dasar, dan perpangkatan untuk bilangan bulat dan pecahan.

Berikut operasi bilangan dengan menggunakan operator modulo.

```Python
# Modulo
y_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo:', mod_ints) # Integer Modulo: 8
print('Float Modulo:', mod_floats) # Float Modulo: 1.1999999999999993
```

Pembagian lantai membagi dua angka dan mengembalikan bilangan bulat terbesar yang kurang dari atau sama dengan hasilnya. Ini dilakukan dengan operator garis miring ganda (//):

```Python
# Floor
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0
```

Perpangkatan memangkatkan suatu bilangan dengan bilangan lain, dan dilakukan dengan menggunakan tanda bintang ganda (**):

```Python
# Exponent
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089
```

Terkadang hasil dari operasi yang melibatkan bilangan pecahan (desimal) menghasilkan bilangan dengan digit desimal yang sangat banyak. Misalnya, penjumlahan 0,1 + 0,2 sama dengan 0,30000000000000004, bukan 0,3.

Hal ini terjadi karena angka disimpan dalam format biner, dan beberapa pecahan tidak dapat direpresentasikan secara tepat dalam biner. Akibatnya, pecahan tersebut disimpan sebagai perkiraan terbatas, sama seperti pecahan 1/3 yang tidak dapat direpresentasikan dengan jumlah digit terbatas dalam desimal dan dipotong setelah sejumlah digit tak terbatasnya (0,33333...).

Hal ini menyebabkan kesalahan pembulatan kecil.

Python juga menyediakan fungsi bawaan untuk mengkonversi data numerik atau string menjadi bilangan bulat atau bilangan pecahan.

Fungsi `float()` mengembalikan bilangan floating-point yang dibentuk dari bilangan yang diberikan:

```Python
# float()
my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1)  # 56.0
print(type(my_float_1))  # <class 'float'>
```

Fungsi `int()` mengembalikan bilangan bulat yang dibentuk dari angka yang diberikan:

```Python
# int()
my_float = 12.92563
my_int = int(my_float)

print(my_int)  # 12
print(type(my_int))  # <class 'int'>
```

Selain itu, Anda dapat menggunakan fungsi bawaan yang sama untuk mengkonversi string menjadi float atau integer:

```Python
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>
```

Berikut beberapa method bawaan Python yang dapat digunakan untuk bekerja dengan bilangan Integer atau Float:

- Round: `round()`, digunakan untuk membulatkan bilangna desimal, secara default digunakan untuk membulatkan bilangan ke bilangan integer terdekat, mengembalikan bilangan tanpa desimal.

```Python
# round()
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3
```

- Abs: `abs()`, membalikan nilai kedalam bentuk absolut.

```Python
# abs()
num = -15

absolute_value = abs(num)
print(absolute_value)   # 15
```

- Pow: `pow()`, digunakan untuk memangkatkan suatu bilangan dengan bilangan lain atau melakukan eksponensiasi modular.

```Python
# pow()
result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3
```

## Bagaimana Augmented Assigment Bekerja?

Augmented Assignment adalah proses penugasan yang mengkombinasikan operasi biner, menggunakan variabel dan mengoperasikannya dengan suatu nilai lain yang hasilnya akan disimpan kembali pada variabel tersebut.

Sintaks dasar Augmented Assignment:

```Python
variable <operator>= value
```

Sintaks tersebut lebih efisien dari bentuk penulisan berikut.

```Python
variable = variable <operator> value
```

Berikut contoh augmentd assignment untuk menambahkan nilai 5 ke variable yang sudah ada.

```Python
# Augmented Assignment: Addition
my_var = 10
my_var += 5

print(my_var)   # 15
```

Contoh diatas sama hal dengan .

```Python
my_var = 10
my_var = my_var + 5

print(my_var)   # 15
```

Nilai lebih dari augmented assignment adalah membuat kode lebih ringkas dan mudah dibaca, untuk memperbarui sebuah variabel. Hal tersebut mengurangi resiko redudansi dan kesalahan ketik yang serupa.

Operator lain yang dapat digunakan untuk augmented assignment:

- Subtraction: `-`.

```Python
# subtraction
count = 15
count -= 3

print(count)   # 12
```

- Multiplication: `*`.

```Python
# multiplication
product = 65
product *= 7

print(product)   # 455
```

- Division: `/`.

```Python
# division
price = 100
price /= 4

print(price)   # 25.0
```

- Floor: `//`.

```Python
# floor
total_pages = 23
total_pages //= 5

print(total_pages)   # 4
```

- Modulo: `%`.

```Python
# modulo
bits = 35
bits %= 2

print(bits)   # 1
```

- Exponent: `**`.

```Python
# exponent
power = 2
power **= 3

print(power)   # 8
```

Augmented assignment juga dapat dilakukan pada string. Seperti contoh berikut untuk menambahkan nilai pada sebuah variabel string.

```Python
# Augmented Assignment: String
greet = 'Hello'
greet += 'World'

print(greet)   # Hello World
```

Dan perkalian pada string dapat melakukan perulangan pada string

```Python
# Multiplication String
greet = 'Hello'
greet *= 3

print(greet)   # HelloHelloHello
```

Operator augmented assignment lain akan mengemalikan `TypeError` jika dilakukan pada string.

```Python
greet = 'Hello'
greet -= ' World'

print(greet) # TypeError: unsupported operand type(s) for -=: 'str' and 'str'


greet = 'Hello'
greet /= 'World'

print(greet) # TypeError: unsupported operand type(s) for /=: 'str' and 'str' 
```

Python tidak bisa menggunakan pintasan tambahan seperti operator increment `++`, atau decrement `--`. Hal tersebut menjaga agar bahasa tetap jelas dan eksplisit.

```Python
my_var = 5

print(+my_var)   # 5
print(++my_var)  # 5
print(+++my_var) # 5

my_var += 1

print(my_var) # 6
```

