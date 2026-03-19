# Variables and Data Types

## Variabel

Variabel merupakan bagian penting dari rangkaian pemrograman.

Variabel membuat sebuah logic lebih mudah untuk diimplementasikan dan dioperasikan, dibanding tidak menggunakan variabel.

Variabel bersifat seperti kotak berlabel yang digunakan untuk menyimpan nilai (data) dengan tipe tertentu.

Python tidak memerlukan kata kunci khusus untuk mendeklarasikan variabel.

Pengguna cukup menentukan nama variabel dan menugaskan nilai pada variabel tersebut.

```Python
name = 'Alrizq'
age = 25
tinggi = 1.75
lajang = True
```

### Aturan Penamaan Variabel

Python memiliki kaidah penamaan variabel yang berlaku untuk memvalidasi independensi nilai yang disampaikan.

Penaman variabel di Python tidak boleh dimulai dengan angka atau bilangan (0-9).

```Python
2x = 10   # Tidak Boleh
```

Boleh dimulai denggan *underscore* (`_`), dan diutamakan karakter huruf.

```Python
x = 10    # Boleh
_x = 10   # Boleh
```

Penamaan variabel di Python hanya boleh mengandung karakter alfanumerikal dan `_`, (a-z), (A-Z), (0-9).

```Python
my_var = 'free'
my_var2 = 'free'
```

### Format Penamaan Variabel

Beberapa bahasa pemrograman memiliki format penamaan yang berlaku umum digunakan oleh para penggunanya.

Python memiliki format umum yang biasa digunakna oleh pengguna Python yaitu `snake-case`.

Contoh:

```Python
first_name = 'Alrizq'
last_name_user  = 'Athallah'
```

### Penting

Sangat disarankan untuk pengguna Python menentukan nama variabel yang deskriptif, efisien dan jelas.

Python juga menerapkan *case-sensitivity*, artinya beda bentuk dan format tidak serta merta menyamakan nilai dan dianggap sama.

`age`, `Age` dan `AGE` dianggap berbeda.

### Multiple Variabel

Python juga memungkinkan pengguna untuk membuat beberapa variabel secara bersamaan.

Untuk melakukannya, dapat menggunakan `,` sebagai pemisah antar nama dan nilai variabel

```Python
x, y, z = 10, 20, 30
print(x)
print(y)
print(z)
```

### Menyamakan Nilai Variabel

Python juga memungkinkan pengguna untuk menyamakan nilai beberapa variabel secara bersamaan.

```Python
x = y = z = "orange"
print(x)
print(y)
print(z)
```

### Local dan Global Variabel

Dalam python, *scope* variabel menetukan variabel tersebut dapat diakses atau tidak.

Terdapat dua *scope* umum pada variabel yaitu *Local* dan *Global*.

**Variabel Local:**

Sebuah variabel yang dideklarasikan dalam sebuah fungsi, dan hanya dapat diakses didalam atau oleh fungsi itu sendir.

Contoh:

```Python
def my_function():
  y = "Saya Lokal"   # variabel lokal
  print(y)

my_function()
```

**Variabel Global**

Variable Global adalah variabel yang didefinisikan diluar fungsi atau di body utama Python

Variabel global dapat diakses oleh fungsi didalamnya.

```Python
x = "Saya Global"

def my_function():
  y = "Saya Lokal
  print(y)
  print(x)

my_function()
```

**Kata Kunci Global**

Jika pengguna ingin menjadikan local variabel menjadi Global Variabel, maka dapat dilakukan dengan kata kunci `global`.

```Python
def my_function():
  global user_name = 'alrizqathallah'
  print(user_name)

my_function()

print(user_name)
```

## Tipe Data

Tipe Data adalah tipe yang merepresentasikan sebuah data pada seubah variabel.

Python memiliki beberapa tipe data yang mencakup tipe data teks, bilangan dan objek.

Berbeda dengan bahasa pemrograman lain yang membagi tipe data menjadi dua golongan, yaitu *primitive* dan *reference*.

Python tidak memberlakukan demikian, Python menyamakan perlakuan terhadap semua tipe data yang disediakan, dengan objek.

Berikut beberapa tipe data di Pyton:

- *String* `str`.
- *Integer* `int`.
- *Float* `float`.
- *Boolean* `bool`.
- *List* `list`.
- *Tuple* `tuple`.
- *Dictionary* `dict`.
- *Set* `set`.
- *None* `None`.

```Python
# String
full_name = 'Alrizq Athallah'

# Integer
age = 28

# Float
gpa = 3.52

# Boolean
is_student = True

# List
formula_one = ["Mercedez", "Ferrari", "Renault", "Aston Martin", "Honda"]

# Tuple
fifa_world_cup = (2006, 2010, 2014, 2018, 2022)

# Dictionary
user_data = {"username": "thebenkz", "points": 2000, "is_active": True}

# Sets
moto_gp = {"Ducati", "Honda", "Yamaha"}

# None
x = None
```

### Fungsi `type()`

Fungsi `type()` merupakan operator yang digunakan untuk mengetahui sebubah variabel memiliki tipe data tertentu.

contoh:

```Python
x = 5
print(type(x))   # <class 'int'>
```

Dalam contoh tersebut x memiliki tipe data integer `<class 'int'>`.

### Casting

Dalam pemrograman, Casting adalah proses mengubah tipe data satu variabel ke tipe data lainnya. Python adalah bahasa yang menggunakan Object-Oriented, sehingga casting dilakukan menggunakan fungsi-fungsi konstruktor.

Casting sangat berguna ketika kamu menerima input dari pengguna (yang biasanya bertipe teks/String) namun perlu melakukan perhitungan matematika padanya.

**Fungsi Utama Casting di Python**
Ada tiga fungsi yang paling sering digunakan untuk melakukan casting:

1. `int()` - mengkonversi ke bilangan bulat.

Fungsi ini digunakan untuk mengubah string atau angka desimal menjadi bilangan bulat.

- Jika dari float: Angka di belakang koma akan dihapus (bukan dibulatkan).
- Jika dari string: String tersebut harus berisi karakter angka.

Contoh:
```Python
x = int(1)     # x akan menjadi 1
y = int(2.8)   # y akan menjadi 2 (desimal hilang)
z = int("3")   # z akan menjadi 3
```

2. `float()` - mengkonversi bilangan desimal.

Fungsi ini mengubah bilangan bulat atau string menjadi angka dengan titik desimal.

- Jika dari `int`: Akan ditambahkan `.0` di belakangnya.

Contoh:
```Python
x = float(1)     # x akan menjadi 1.0
y = float(2.8)   # y akan tetap 2.8
z = float("3")   # z akan menjadi 3.0
w = float("4.2") # w akan menjadi 4.2
```

3. `str()` - menkonversi ke string.

Fungsi ini mengubah hampir semua tipe data (angka, list, dll) menjadi bentuk teks agar bisa digabungkan dengan kalimat lain.

Contoh:
```Python
x = str("s1") # x akan tetap "s1"
y = str(2)    # y akan menjadi "2"
z = str(3.0)  # z akan menjadi "3.0"
```

**Kapan Kita Membutuhkan Casting?**

Kasus yang paling umum adalah saat mengambil input dari user. Perhatikan contoh berikut:

```Python
# Input dari user selalu dianggap String
usia = input("Masukkan usia Anda: ") 

# Jika kita ingin menjumlahkan, kita harus casting ke int
usia_tahun_depan = int(usia) + 1

print("Tahun depan usia Anda adalah " + str(usia_tahun_depan))
```

**Catatah Penting:**
Kamu tidak bisa melakukan casting string huruf ke angka. Misalnya, `int("Halo")` akan menyebabkan `ValueError` karena "Halo" tidak memiliki nilai angka.