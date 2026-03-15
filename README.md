# Bahasa Pemrograman Python

## Apa itu Python?

- **Bahasa Pemrograman General-Purpose**: Python dirancang untuk berbagai kebutuhan, bukan hanya satu bidang spesifik.
- **Populer Karena Sederhana**: Dikenal sangat mudah untuk dipelajari dan digunakan, menjadikannya bahasa yang sangat populer saat ini.
- **Fleksibel**: Cocok untuk pemula maupun skala industri besar.

## Kegunaan Utama Diberbagai Bidang:

1. **Data Science dan AI**:
   - *Analisis Data*: menggunakan library seperti *Pandas* dan *Numpy* untuk mempermudah pengolahan data.
   - *Machine Learning*: menggunakan *Tensorflow* dan *Scikit* untuk menggunakan model AI dengan lebih fleksibel.
2. **Pengembangan Web (Backend)**:
   - Membangun sistem yang aman dan terukur dengan framework seperti *Django*, *FastAPI* dan *Flask*.
   - Digunakan oleh platform besar seperti *Instagram* dan *Pinterest*.
3. **Kemanan Siber (Cybersecurity)**:
   - Mendeteksi malware dan virus.
   - Membangun pemindaian otomatis serta menganalisis ancaman.
4. **IoT dan Embedded System**:
   - Berjalan baik pada mikrokomputer seperti *RaspberryPi*.
   - Digunakan untuk proyek perangkat pintar (*smarthome*) dan stasiun pemantauan cuaca.
5. **Otomasi dan Scripting**:
   - *Tugas Repetitif*: mengotomatiskan pengiriman email, pengolahan spreadsheet dan manajemen file.
   - *Web Scraping*: mengambil data publik dari situs web menggunakan *Selenium* dan *BeautifulSoup*.
6. **DevOps dan Administrasi Sistem**:
   - Menuliskan skrip *CI/CD* dan mengelola infrastruktur.
   - Pemantauan server, pengelolaan log, dan pembuatan API internal.
7. **Software Testing**:
   - Membuat rangkaian pengujian (*test suites*) yang handal menggunakan alat seperti *PyTest*.

<br>

<hr>

**Python adalah pilihan tepat bagi siapapun yang ingin memulai belajar pemrograman karena kemampuannya yang bisa diterapkan dihampir semua spesialisasi teknologi**.

<hr>

<br>

# Instalasi Python

## Persiapan Umum

- **Sumber Resmi**: Selalu unduh installer dari situs resmi [Python](https://python.org "Website resmi Python").
- **Terminal/Command Prompt**: Alat berbasis teks untuk berinteraksi dengan komputer.
  - **MacOS**: *Terminal*.
  - **Windows**: *Commmand Prompt* atau *Powershell*.
  - **Linux**: *Gnome Terminal* atau konsole.

## Langkah Instalasi Berdasarkan OS

1. **MacOS**:
   - Buka situs [Python](https://python.org "Website resmi Python"), arahkan kursor ke *Downloads* dan klik versi terbaru.
   - Buka file `.pkg` yang terunduh.
   - Klik *Continue* hingga bagian *Installation Type*, lalu klik *Install*.
   - Masukan password perangkat jika diminta dan tunggu hingag selesai.

2. **Windows**:
   - Unduh file *executeable* (`.exe`) dari menu *Download For Windows* di situs resmi.
   - Bukan installer tersebut.
   - *Penting*: Centang opsi *Add python.exe to PATH* agar Python bisa diakses dari terminal manapun.
   - Klik *Install Now*

3. **Linux**:
   - Sebagian besar distro (*Ubuntu*, *Debian*, *Fedora*) sudah menyertakan Python secara bawaan.
   - Cek ketersediaan melalui terminal.
   - Jika belum ada, gunakan pengelola paket bawaan distro atau unduh paket instalasi dari situs resmi.

## Verifikasi dan Penggunaan

- **Cara cek instalasi**:
  - Buka terminal dan ketik perintah berikut untuk memastikan Python terpasang: `python --version` atatu `python3 --version`

- **Python 2 vs Python 3**:
  - *Penting*: Python 2 sudah usang (*end-of-life*).
  - Pada sistem lama (*macOS* / *Linux*), perintah `python` merujuk ke Python 2.
  - Gunakan selalu `python3` untuk pengembangan baru.

## Menajalankan Python Interpreter

Anda bisa langsung mengetik kode Python secara interaktif dengan mengetik `python` atau `python2` di terminal untuk membuka *interpreter*.

