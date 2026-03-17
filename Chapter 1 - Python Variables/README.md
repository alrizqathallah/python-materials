# Python Variables

## Apa itu Variabel

Variabel diibaratkan seperti kotak yang diberikan sebuah label untuk menyimpan nilai tertentu.

Label pada kotak, disebut sebagai nama variabel, dan nilai yang disimpan merupakan data.

Misal sebuah kota bernama `age` dengan isi `25`, sama dengan variabel `age` dengan value `25`.

## Membuat Variabel

Dalam Pytho, varibel otomatis dikenali (terdeklarasi) ketika nilai ditugaskan pada variabel tersebut.

```Python
age = 25
name = 'Alice'
height = 1.68
```

Disini:

- Variabel `age` menyimpan data integer `int` yaitu `25`.
- Variabel `name` menyimpan data string `str` yaitu `'Alice'`.
- Variabel `height` menyimpan data float `float` yaitu `1.68`.

Mendeklarasikan sebuah varibel di Python tidak memerlukan kata kunci khusus seperti `var`, `let` atau `const`.

Nilai pada variabel juga dapat diganti setelah dibuat.

## Aturan Penamaan Variabel

Ada beberapa aturan terkait penamaan variabel di Python:

- Penamaan variabel hanya dapat mengandung karakter alfanumerik, (a-z), (A-B), (0-9) dan (_).
- Nama variabel tidak boleh dimulai dari bilangan atau angka.
- *Case-Sensitive*, nama variabel `age`, `Age`, dan `AGE` dianggap berbeda.
- Pemberian nama variabel tidak boleh menggunakan katak kunci khusus yang telah ditetapkan Python seperti `if`, `for`, `while`, `def`, dsb.

Contoh penaman variabel yang tepat:
```Python
my_var = 10
var2 = 20
_long_name = 30
```

Contoh penamaan variabel yang tidak tepat:
```Python
2var = 10    # Memulai nama variabel dengan angka
my-var = 20  # Mengandung karakter yang tidak diizinkan `-`
if = 30      # Menggunakan kata kunci khusus yang ditetapkan Python.
```

**Format Penamaan Variabel**

- Disetiap bahasa pemrograman biasanya memiliki format penamaan variabel yang umum digunakan.
- Python menggunakan format *snake_case*, penamaan karakter menggunakan huruf kecil dan dipisah dengan garis bawah.
- Kecuali beberapa karakter tunggal seperti `i` dsb, yang umum digunakan dalam looping.

Contoh:
```Python
student_name = 'John'
total_score = 95
is_graduated = True
```

## Tipe Data Dasar

Variabel menyimpan data dengan tipe tertentu, berikut beberapa contoh tipe data bawaan yang umum di Python dan bahasa pemrograman lainnya.

| Tipe  |          Deskripsi        |      contoh     |
|-------|---------------------------|-----------------|
|  int  |       Bilangan bulat      |      x = 5      |
| float |      Bilangan desimal     |   pi = 3.14159  |
|  str  |             Teks          | name = 'Python' |
|  bool | Boolean (True atau False) | is_valid = True |

Pengguna dapat mengecek sebuah variabel denga tipe data tertentu dengan operator atau fungsi `type()`.

```Python
x = 10
print(type(x))        # <class 'int'>

y = 3.14
print(type(y))        # <class 'float'>

name = 'Alice'
print(type(name))     # <class 'str'>

flag = False
print(type(flag))     # <class 'bool'>
```

## Dynamic Typing

Python menerapkan *Dynamically Typing*, yang berarti varibel dapat diubah selama program dieksekusi dan tidak perlu dideklarasikan secara eksplisit.

contoh:

```Python
value = 10       # int
print(value)

value = 'ten'   # int
print(value)
```

Fleksibilitas tersebut terkadang dapat membawa eror jika pengguna tidak hati-hati. Disarankan untuk memperhatikan varibel serta isi variabel tersebut.

## Multiple Assignment

Python memungkinkan untuk membuat dan menugaskan variabel dalam satu baris yang sama.

```Python
a, b, c = 5, 10, 15
print(a)
print(b)
print(c)
```

Juga dapat menugaskan beberapa untuk nilai yang sama.

```Python
a = b = c = 10
print(a, b, c)
```

Multiple assigment sangat berguna untuk menukar nilai:

```Python
a, b = 10, 20
print(a, b)   # 10 20

a, b = b, a   # swap
print(a, b)   # 20 10
```

## Konversi Tipe (Casting)

Terkadang pengguna perlu mengkonversi suatu tipe data ke tipe data lainnya.

Python mengakomodasi keperluan tersebut dengan melakukan casting:

- `int()`, untuk mengkonversi nilai ke integer
- `float()`, untuk mengkonversi nilai ke float
- `str()`, untuk mengkonversi nilai ke string
- `bool()`, untuk mengkonversi nilai ke boolean

Contoh:

```Python
# String to integer
num_str = "123"
num_int = int(num_str)
print(num_int + 1)   # 124

# Integer to float
x = 5
x_float = float(x)
print(x_float)       # 5.0

# Float to integer (truncates decimal)
pi = 3.14159
approx = int(pi)
print(approx)        # 3

# Number to string
age = 30
message = "I am " + str(age) + " years old."
print(message)       # I am 30 years old.
```

Hati-hati: mengkonversi string yang bukan merupakan angka akan menyebabkan kesalahan.

```Python
int("hello")   # ValueError: invalid literal for int()
```

## Konstanta (Constants)

Konstanta merupakan variabel yang nilainya tidak boleh berubah.

Python tidak memiliki deklarasi bawaan untuk konstanta, tetapi secara tradisi pengguna Python menggunakan huruf kapital untuk menandakan sebuah variabel merupakan konstanta.

```Python
PI = 3.14159
MAX_SIZE = 100
DEFAULT_COLOR = "blue"
```

## Mendapatkan Input Pengguna

Anda dapat meminta input dari pengguna menggunakan fungsi `input()`. Fungsi ini selalu mengembalikan `string`.

```Python
name = input('What is your name? ')
print('Hello, ' + name + '!')
```

Jika Anda memerlukan angka, konversikan setelah memasukkannya:

```Python
age_str = input("How old are you? ")
age = int(age_str)   # convert to int
next_year = age + 1
print("Next year you will be", next_year)
```

## Mencetak Variabel dengan f-string

Python 3.6 memperkenalkan f-string, cara mudah untuk menyematkan variabel di dalam string. Cukup letakkan huruf 'f' sebelum tanda kutip pembuka dan gunakan {variabel} di dalamnya.

```Python
name = "Bob"
age = 22
print(f"{name} is {age} years old.")
```

Menggunakan F-string lebih rapi dari penggunaan concatenation `+`.

## Kesalahan Umum

- Menggunakan variabel yang belum diberi nilai: print(x) sebelum x = 5 → NameError.
- Tipe yang tidak cocok: "Age: " + 30 → TypeError (tidak dapat menggabungkan string dan integer). Gunakan f-string atau konversi.
- Lupa mengkonversi input: age = input("Age: ") dan kemudian age + 1 → error karena age adalah string.