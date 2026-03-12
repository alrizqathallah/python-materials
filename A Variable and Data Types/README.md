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

### Komentar

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