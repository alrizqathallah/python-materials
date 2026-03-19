# Python

Python merupakan salah satu dari bahasa pemrograman paling populer didunia saat ini.

Pertama kali dibuath oleh *Guido Van Rossum* dan pertama kali diperkenalkan pada tahun 1991.

## Kegunaan Python

Python bukan sekedar bahasa pemrograman biasa, kepopuleran Python hari ini tidak lepas dari kinerja dan kegunaan yang diberikan secara luas.

Python mampu digunakan dalam berbagai bidang spesifik, *General-Purpose* mulai dari pengembangan web, analisis data hingga membuat kecerdasan buatan.

**Kemampuan Python untuk berbagai bidan spesifik:**

- Python dapat dimaksimalkan untuk membangun sisi server (server-side) dalam pengembangan web, dengan beberapa rangka kerja yang ditawarkan (*Django*, *FastAPI*, *Flask*).

- Python dapat dimaksimalkan untuk pengintegrasian perangkat lunak untuk menciptakan sebuah alur kerja perangkat lunak.

- Python bisa dikoneksikan dengan sistem basis data, mampu mengelola dan memanipulasi data dan file.

- Python mampu mengelola data dalam jumlah raksasa dan perhitungan matematika yang rumit.

- Digunakan dalam pengembangan dini untuk menciptakan produk prototipe yang handal, sebelum penggarapan versi massal yang lebih kompleks.

## Kenapa Python?

Banyak alasan yang mendasari mengapa Python banyak dipilih oleh pemula dan profesional sebagai bahasa pemrograman yang digunakan.

- Python menawarkan simplisitas dan keterbacaan tinggi, sehingga tidak sulit untuk dimengerti oleh pemula dan alur yang mudah dipahami oleh profesional.

- Python mampu dioperasikan hampir disetiap sistem operasi umum, *windows*, *mac*, *linux* hingga *Raspberry Pi*.

- Python dijalakan menggunakan sistem interpreter (*Interpreted-language*), kode yang ditulis dapat langsung dieksekusi tanpa perlu mengkompilasi terlebih dahulu.

- Mengakomodasi berbagai paradigma pemrograman, *procedural*, *object-oriented*, dan *functional*.

- Dibanding dengan bahasa pemrograman lain, Python hanya memerlukan sedikit baris kode untuk membuat sebuah statement print, dibanding bahasa pemrograman lain.

## Perlu Diketahui

Perlu diketahui, Python memiliki beberapa versi, namun versi yang paling stabil saat ini adalah Python 3.

Python 2 sudah tidak lagi direkomendasikan, atau sudan usang.

Untuk setiap pengembangan modern, wajib menggunakan Python versi 3 (Python 3.x.x).

Diperlukan alat khusus seperti *IDE* (*Integrated Development Environment*) untuk menulis kode Python, baik dalam skala kecil atau proyek besar.

Beberapa IDE bisa digunakan untuk menulis dan mengelola proyek Python:

- **Pycharm**, IDE berbayar namun memiliki fitur sangat lengkap.
- **VS Code**, IDE ringan yang dapat dimaksimalkan untuk pengembangna Python dengan bantuan ekstensi khusus dan tambahan.

## Instalasi Python

Python menyediakan paket installer yang dapat diunduh untuk sistem operasi umum seperti *windows*, *mac* dan *linux*.

Dapat dikunjungi situs resmi dari [Python](https://www.python.org/), kemudian menuju halaman "Downloads" untuk mengunduh installer.

Pastikan pengguna baru mengunduh installer Python versi terbaru atau versi stabil (3.x.x) yang disediakan.

### Windows

Setelah installer versi windows selesai diunduh,

- Menjalankan file installer tersebut yang berekstensi `.exe`,
- Dapat diikuti proses instalasi seperti proses instalasi aplikasi lain pada umumnya,
- Khusus pengguna windows, wajib mencentang kolom "Add to PATH" agar Python ditambahkan ke Environment Variable oleh installer,
- Setelah instalasi berhasil, silahkan memverifikasi dengan mengetikan `python --version` di terminal,
- dan akan mengembalikan versi Python yang terinstal.

### Linux

Pada umumnya distro modern di linux sudah menyediakan Python sebagai paket bawaan yang siap digunakan (sudah terinstal).

Pengguna hanya perlu memastikan denga mengetikan `python --version` atau `python3 --version` di terminal dan akan muncul versi Python yang digunakan (Python 3.x.x).

Jika Python belum tersinstal, maka pengguna bisa melakukan instalasi menggunakan paket manajer bawaan distro yang digunakan.

Secara otomatis paket Python akan diunduh dan diinstal kesistem operasi linux (distro) yang digunakan.

## Penggunaan Python

Sebelum menulis dan menjalankan program Python, pengguna wajib membuat file Python terlebih dahulu dengan memberi nama file yang berekstensikan `.py` yaitu ekstensi khusus program Python, dan membuka file tersebut dengan kode editor atu IDE yang digunakan.

Untuk menjalankan programn tersebut, pengguna dapat beralih dengan terminal dan menyesuaikan path program tersebut berada, dan mengetikan `python` yang diikuti nama program dengan sesuai.

Contoh:
```Shell
python main.py
```

Python akan menjalankan program tersebut dan menampilkannya pada terminal.

### Python CLI

Python CLI (*Command Line Interface*), merupakan editor bawaan Python yang dapat dijalankan langsung lewat terminal.

Dengan mengetikan `python` atau `python3` di terminal, secara otomatis akan dialihkan ke format CLI Python di terminal.

Pada workspace CLI, pengguna bisa langsung menuliskan kode Python dan mengeksekusinya secara langsung.

## Python Syntax

Syntax atau Sintaksis adalah aturan dalam penulisan suatu kode bahasa pemrograman tertentu.

Setiap bahasa pemrograman memiliki sintaks dan pendekatan penulisan yang berbeda-beda, meski secara umum memiliki kesamaan.

### Indentasi Python

Berbeda dengan bahasa pemrograman lain yang umumnya menggunakan *curly-braces* (kurung kurawal) `{}` sebagai penentu blok kode.

Python menggunakan indentasi (spasi diawal baris) sebagai penentu blok kode. Keberadaan indentasi sangat pentig di Python, kesalahan penempatan indentasi dapat menyebabkan eror pada sintaks.

Berikut contoh penggunaan indentasi di Python:

```Python
if 5 > 2:
  print('Five is greater than two')
```

Perlu diperhatikan agar penempatan indentasi sesuai dan tidak terjadi keslahan.

Berikut contoh kesalahan tidak menempatkan indentasi:

```Python
if 5 > 2:
print('five is greater than two')
```

### Statements

Statements merupakan baris kode yang berisikan instruksi untuk dieksekusi komputer.

Python adalah bahasa interpreted, dimana setiap baris bisa langsung dieksekusi tanpa perlu dikompilasi terlebih dahulu.

dan Python tidak memerlukan penutup statements seperti *semicolon* `;` untuk mengakhiri sebuah statements.

Contoh:

```Python
print('Hello World!')

print('Hello Python!')
```

**Terkecuali** pengguna hendak menuliskan beberapa statements dalam satu baris yang sama.

Dalam kondisi tersebut, `;` diperlukan untuk memisah antar statements dibaris yang sama.

Contoh:

```Python
print('Hello World!'); print('Hello Python!')
```

### Fungsi `print()`

Fungsi `print()` di Python berfungsi untuk menampilkan data ke terminal.

Mirip fungsi seperti `console.log()` di JavaScript atau `System.out.println()` di Java.

Fungsi tersebut dapat menampilkan berbagai jenis tipe data, `string`, `integer`, `float`, `boolean` dan lainnya.

Bisa juga berikan argumen yang bersifat operasi, seperti matematika dan perbandingan yang mengembalikan nilai boolean.

Contoh:

```Python
print('String')  # String
print(10)        # Integer
print(3.25)      # Float
print(True)      # Boolean
print(1 + 2)     # Math Operation
print(5 > 2)     # Comparasion Operation
```

### Comments

Comments atau komentar adalah baris atau beberapa baris statement yang tidak akan ikut dieksekusi, atau diabaikan oleh interpreter.

Komentar berfungsi sebagai catatan oleh pengguna, terkait *logic* atau *flow* dari sebuah kode.

Membuat komentar pada Python cukup menggunakan simbol `#`, dan statement apapun setelahnya akan dianggap sebagai komentar

```Python
# This is comments
# pring('Hello World!')
```

Penggunaan simbol `#` sebagai komentar di Python hanya mencakup satu baris saja, jika perlu menkomentar beberapa baris sekaligus dapat menggunakan simbol `'''` atau `"""` untuk membuat komentar multibaris.

```Python
''' This
is
Multiline 
comments
'''

""" This is
multiline comments """
```

