# Bahasa Pemrograman Python

## Apa itu Python?

- **Bahasa Pemrograman General-Purpose**: Python dirancang untuk berbagai kebutuhan, bukan hanya satu bidang spesifik.
- **Populer Karena Sederhana**: Dikenal sangat mudah untuk dipelajari dan digunakan, menjadikannya bahasa yang sangat populer saat ini.
- **Fleksibel**: Cocok untuk pemula maupun skala industri besar.

## Kegunaan Utama Diberbagai Bidang:

1. **Data Science dan AI**:
   - _Analisis Data_: menggunakan library seperti _Pandas_ dan _Numpy_ untuk mempermudah pengolahan data.
   - _Machine Learning_: menggunakan _Tensorflow_ dan _Scikit_ untuk menggunakan model AI dengan lebih fleksibel.
2. **Pengembangan Web (Backend)**:
   - Membangun sistem yang aman dan terukur dengan framework seperti _Django_, _FastAPI_ dan _Flask_.
   - Digunakan oleh platform besar seperti _Instagram_ dan _Pinterest_.
3. **Kemanan Siber (Cybersecurity)**:
   - Mendeteksi malware dan virus.
   - Membangun pemindaian otomatis serta menganalisis ancaman.
4. **IoT dan Embedded System**:
   - Berjalan baik pada mikrokomputer seperti _RaspberryPi_.
   - Digunakan untuk proyek perangkat pintar (_smarthome_) dan stasiun pemantauan cuaca.
5. **Otomasi dan Scripting**:
   - _Tugas Repetitif_: mengotomatiskan pengiriman email, pengolahan spreadsheet dan manajemen file.
   - _Web Scraping_: mengambil data publik dari situs web menggunakan _Selenium_ dan _BeautifulSoup_.
6. **DevOps dan Administrasi Sistem**:
   - Menuliskan skrip _CI/CD_ dan mengelola infrastruktur.
   - Pemantauan server, pengelolaan log, dan pembuatan API internal.
7. **Software Testing**:
   - Membuat rangkaian pengujian (_test suites_) yang handal menggunakan alat seperti _PyTest_.

<br>

<hr>

**Python adalah pilihan tepat bagi siapapun yang ingin memulai belajar pemrograman karena kemampuannya yang bisa diterapkan dihampir semua spesialisasi teknologi**.

<hr>

<br>

# Instalasi Python

## Persiapan Umum

- **Sumber Resmi**: Selalu unduh installer dari situs resmi [Python](https://python.org "Website resmi Python").
- **Terminal/Command Prompt**: Alat berbasis teks untuk berinteraksi dengan komputer.
  - **MacOS**: _Terminal_.
  - **Windows**: _Commmand Prompt_ atau _Powershell_.
  - **Linux**: _Gnome Terminal_ atau konsole.

## Langkah Instalasi Berdasarkan OS

1. **MacOS**:
   - Buka situs [Python](https://python.org "Website resmi Python"), arahkan kursor ke _Downloads_ dan klik versi terbaru.
   - Buka file `.pkg` yang terunduh.
   - Klik _Continue_ hingga bagian _Installation Type_, lalu klik _Install_.
   - Masukan password perangkat jika diminta dan tunggu hingag selesai.

2. **Windows**:
   - Unduh file _executeable_ (`.exe`) dari menu _Download For Windows_ di situs resmi.
   - Bukan installer tersebut.
   - _Penting_: Centang opsi _Add python.exe to PATH_ agar Python bisa diakses dari terminal manapun.
   - Klik _Install Now_

3. **Linux**:
   - Sebagian besar distro (_Ubuntu_, _Debian_, _Fedora_) sudah menyertakan Python secara bawaan.
   - Cek ketersediaan melalui terminal.
   - Jika belum ada, gunakan pengelola paket bawaan distro atau unduh paket instalasi dari situs resmi.

## Verifikasi dan Penggunaan

- **Cara cek instalasi**:
  - Buka terminal dan ketik perintah berikut untuk memastikan Python terpasang: `python --version` atatu `python3 --version`

- **Python 2 vs Python 3**:
  - _Penting_: Python 2 sudah usang (_end-of-life_).
  - Pada sistem lama (_macOS_ / _Linux_), perintah `python` merujuk ke Python 2.
  - Gunakan selalu `python3` untuk pengembangan baru.

## Menajalankan Python Interpreter

Anda bisa langsung mengetik kode Python secara interaktif dengan mengetik `python` atau `python3` di terminal untuk membuka _interpreter_.
