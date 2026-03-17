# Pengatar Python

Selamat datang di Python!

Repositori ini akan membahas materi dan pembelajarna Python. Mencakup dasar, penulisan dan penarapan kode.

## Apa itu Python?

Python adalah bahasa pemrograman **high-level**, **interpreted** yang terkenal dengan sintaks yang ringkas dan keterbacaan tinggi.

Dibuat oleh **Guido Van Rossum**, dan pertama kali diperkenalkan pada tahun 1991. Python didesain denga filosofi keterbacaan kode, menggunakan indentasi untuk mendefinisikan blok kode, membuat Python lebih mudah dibaca dan dipahami.

Python merupakan bahasa pemrograman **general-purpose**, yang dapat digunakan dalam berbagai bidang pemrograman. Mulai dari *pengembangan web*, *otomasi dan scripting*, *analisis data*, *pembelajaran mesin dan kecerdasan buatan*, hingga *IoT dan Game*.

## Mengapa Python?

Beberapa alasan mengapa Python sangat layak dipelajari, terlebih oleh para pemula:

1. **Mudah dipelajari**: Python memiliki sintaks yang ringkas, dan mudah dibaca, sehingga tidak sulit untuk dipahami.
2. **Versatile**: Python mampu digunakan diberbagai bidang, mulai dari scripting hingga skala enterprise.
3. **Komunitas dan Ekosistem besar**: Python memiliki komunitas yang besar dan ekosistem yang luas, sehingga bagi siapapun akan jauh lebih mudah untuk mengakses dan mempelajarinya.
4. **Permintaan Tinggi**: Programmer atau Python Developer banyak dicari di Industri, dan ketersediaan cukup besar di Job Market.
5. **Ramah Pemula**: Dari beberapa alasan sebelumnya sudah menjelaskan betapa Python sangat ramah untuk pemula, terlebih dengan latar belakang non-computer science.

## Sejarah Python

- Diakhir 1980'an mulai menggarap Python sebagai penerus bahasa pemrograman ABC.
- 1991, Python 0.9.0 pertama kali dirilis.
- 2000, Python 2.0 diperkenalkan ke publik dengan fitur yang lebih baik, seperti *garbage collection*.
- 2008, Python 3.0 dirilis, memperbaiki versi sebelumnya, namun tidak memiliki *backward-compatible* dengan versi sebelumnya (Python 2.0).
- 2020, Python 2 sudah usang, Python 3 menjadi satu-satunya versi aktif yang digunakan untuk pengembangan.

Semua pengembangan modern menggunakan versi Python 3.

## Fitur Kunci pada Python

- **Interpreted**: Python merupakan bahasa *interpreted*, dimana kode dieksekusi baris per baris tanpa harus dikompilasi.
- **Dynamic-Type**: Python menganut sistem *dynamic-typing*, dimana pengguna tidak perlu mendeklarasikan tipe variabel secara spesifik, secara otomatis dapat dikenali oleh interpreter.
- **Object-Oriented**: Python mendukung paradigma pemrograman modern seperti *OOP*, tetapi juga mengakakomodasi model paradigma lain seperti *procedural* dan *functional*.
- **Extensive Standard Library**: Python memiliki library standar yang kaya, sehingg sangat memudahkan dalam penulisan dan pengembangan aplikasi.
- **Cross-Platform**: Salah satu keunggulan utama Python adalah cross-platform, dimana Python dapat dijalankan hampir diseluruh sistem operasi.

## Instalasi Python

Sebelum dapat menjalankan program Python, pengguna perlu menginstall Python terlebih dahulu di komputer masing-masing.

**Pertama**:
Silahkan cek ketersediaan Python melalui Terminal atau CMD:

```shell
python --version
```

atau,

```shell
python3 --version
```

Jika pada terminal / cmd mengembalikan `python 3.x.x` maka komputer tersebut sudah terinstal Python. Jika belum maka harus menginstal terlebih dahulu.

**Download Python Installer**:

Silahkan kunjungi situs resmi [Python](https://www.python.org/) dan pilih halaman "Downloads".

Python menyediakan installer untuk beberapa sistem operasi: MacOS, Windows dan Linux.

Download berdasarkan sistem operasi yang digunakan, dan pastikan pengguna mendownload versi Python terbaru (3.x.x) keatas, atau pilih versi stabil yang tersedia.

**MacOS**:

Silahkan jalankan file installer `.pkg` dan ikuti instruksi instalasi, jika diperlukan permission, silahkan penuhi dan ikuti step yang diperlukan hingga Python benar terinstal.

Jika instalasi selesai, silahkan cek kembali pada terminal dan ketikan: `python --version` atau `python3 --version`.

Secara umum untuk MacOS dan Linux, lebih disarankan menggunakan `python3 --version` ketika memverifikasi instalasi.

**Windows**:

Silahkan jalankan file installer `.exe.` dan ikuti step instalasi seperti biasa.

Sangat disarankan untuk pengguna Windows untuk mencentang kolom 'Add to PATH' ketika diawal instalasi, agar secar otomatis installer python akan menambahkan Python pada environment variable. Sehingga Python dapat diakses dari terminal manapun.

Atau juga dapat menambahkan secara manual folder `bin` Python ke "Environment Variable".

Jika instalasi berhasil dan selesai, silahkan verifikasi melalui terminal dengan mengetik `python --version`.

**Linux**:

Secara umum, distro modern Linux seperti *Ubuntu*, *Debian*, *Fedora* dan lainnya sudah menyediakan Python secara bawaan.

Silahkan verifikasi: `python --version` atau `python3 --version`.

Jika belum terinstal, silahkan gunakan distro package manager untuk menginstall Python secara manual.

## Kode Editor

Sebelum benar-benar menggunakan Python, pengguna perlu alat untuk menulis kode Python.

Beberapa kode editor yang dapat digunakan:

1. **VSCode**, paling populer, gratis, fitur terbatas.
2. **PyCharm**, berbayar, fitur lengkap.
3. **JupyterNotebook**, alat khusus data analisis.

Silahkan instal kode editor yang sesuai, disarankan untuk menggunakan *VSCode* atau *Antigravity*, karena fitur lumayan lengkap dan gratis.

Python juga memiliki editor bawaan yang bisa digunakan, **IDLE**. Dengan mengetik `python` atau `python3` di terminal, akan dimuat editor bawaan Python.

## Menulis Kode Pertama Python

