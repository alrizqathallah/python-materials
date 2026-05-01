# Python Materials

---

## Pondasi Pemrograman

---

### Berpikir seperti komputer

**Fokus Pembelajaran**: Memahami bagaimana memecahkan sebuah perintah menjadi instruksi langkah demi langkah yang logis (Algoritma).

Komputer pada dasarnya adalah mesin yang sangat patuh, tetapi sama sekali tidak memiliki inisiatif. Ia tidak bisa memahami perintah yang ambigu atau berasumsi layaknya manusia. Untuk membuat komputer bekerja, kita harus memberikan instruksi yang sangat spesifik, terurut dan logis. Rangkain instruksi inilah yang dalam dunia pemrograman disebut dengan **Algoritma**.

Mari kita gunakan analogi kehidupan nyata: **Memasak Mi Instan**.
Jika kita menyuruh taman, "Tolong buatkan mi," mereka langsung mengerti. Namun, jika kita menyuruh komputer (atau robot), kita harus merinci secara detail:
1. Siapkan panci
2. Isi panci dengan 400ml air.
3. Taruh panci diatas kompor.
4. Nyalakan kompor.
5. Tunggu hingga air mendidih.
6. Masukan mi kedalam air.

Jika kita melewati langkah ke-4("Nyalakan Kompor"), komputer akan tetap menaruh panci disana dan menunggu selamanya karena air tidak akan pernah mendidih. Komputer akan gagal menyelesaikan tugasnya (mengalami *error*) karena instruksi yang diberikan tidak lengkap.

**Latihan**:
Mari berlatih menyusun algoritma sebelum kita menyentuh kode Python. Bayangkan kita harus memberikan instruksi kepada sebuah robot pelayanan untuk **membuat secangkir kopi manis panas**.

Langkah-langkah membuat kopi:
1. Siapkan cangkir dan satu saset kopi.
2. Buka saset kopi dan tuangkan bubuk kopi kedalam cangkir.
3. Ambil panci dan masukan air sebanyak cangkir kopi.
4. Taruh panci berisi air diatas kompor dan nyalakan kompor.
5. Tunggu air sampai mendidih dan matang.
6. Setelah itu tuangkan air tersebut kedalam cangkir yang sudah terisi bubuk kopi.
7. Aduk kopi hingga merata.
8. Kopi siap disajikan

Mari kita lihat susunan instruksi dari "kacamata" sebuah komputer atau robot yang sangat kaku. Terdapat dua celah logika yang menarik disini:

1. **Lupa mematikan kompor**: Di langkah ke-6, kita mneyuruh robot menuangkan air mendidih, tetapi tidak ada instruksi untuk mematikan kompor setelahnya. Robot akan membiarkan kompor menyela terus-menerus! Dalam dunia pemrograman, lupa menghentikan suatu proses bisa menyebabkan program berjalan tanpa henti (*infinite loop*) atau menguras memori komputer.

2. **Asumsi "Kopi Manis"**: Tujuan awal kita adalah membuat secangkir kopi manis panas. Jika saset yang kita maksud adalah kopi campur gula (3-in-1), maka aman. Tapi jika itu kopi hitam pekat, robot tidak akan berinisiatif menambahkan gula kedalamnya karena kita tidak memberikan instruksi "tambahkan satu sendok gula". Komputer sama sekali tidak memiliki inisiatif.

Menemukan celah logika seperti ini dan memperbaikinya adalah kegiatan sehari-hari seorang *Software Engineer*, yang biasa kita sebut sebagai proses **Debugging** (mencari dan membasmi "kutu" atau kesalahan dalam kode).

**Kesimpulan Materi**:
Komputer membutuhkan algoritma (langkah-langkah) yang 100% detail, spesifik, dan tanpa asumsi. Jika program kita mengalami *error*, itu bukan karena komputernya bodoh, melainkan karena ada instruksi kita yang kurang tepat atau terlewat.

---

### Persiapan

**Fokus Pembelajaran**: Mengenal dan menyiapkan perangkat lunak yang dibutuhkan untuk menulis dan menjalankan kode Python.

Sebagai calo *Software Engineer*, kita tidak bisa menulis kode hanya dengan membayangkannya. Kita membutuhkan "bengkel" kerja. Untuk memprogram dalam bahasa Pyton, kita wajib memiliki dua alat utama:

1. **Python Interpreter (Penerjemah)**:
   Komputer pada dasarnya hanya mengeri bahasa mesin, yaitu deretan angka `0` dan `1`. Ia tidak mengerti bahasa inggris, bahasa Indonesia, apalagi bahasa Python. Oleh karena itu, kita perlu menginstal program khusus dari situs resmi Python. Program ini bertugas membaca kode Python yang kita tulis, lalu menerjemahkannya ke bahasa mesin agar komputer bisa memprosesnya.

2. **Code Editor**:
   Ini adalah tempat kita mengetik instruksi atau kode. Secara teknis, kita bisa mengetik kode di program bawaan seperti *Notepad*, tetapi itu sangat menyiksa karena teksnya hanya berwarna hitam putih dan tidak ada pengingat jika kita salah ketik. Di dunia industri, kita menggunakan perangka lunak yang disebut IDE (*Integrated Development Environment*). Salah satu yang paling populer dan gratis adalah **Visual Studio Code (VS Code)**. VS Code akan memberi warna berbeda pada setiap kata kunci dan membantu melengkapi kode kita secara otomatis.

**Alternatif**:
Di era modern ini, adal solusi jika kita tidak ingin atau belum bisa menginstal apa pun di komputer kita. Kita bisa menggunakan **Google Colab**. Ini ibarat *Google Docs* tetapi khusu untuk menjalankan kode Python. Semuanya berjalan secara *online* di dalam peramban (*browser*) kita, sehingga kita bisa langsung melai mengetik kode detik ini juga!

---

### Kode Pertama

**Fokus Pembelajaran**: Memerintahkan komputer untuk berbicara atau menampilkan informasi ke layar.

**Penjelasan Materi**:
Di dalam bahasa Python, instruksi paling dasar yang akan paling sering kita gunakan adalah `print()`.

Bayangkan `print()` sebagai sebuah megafon. Apa pun yang kita letakkan di dalam tanda kurun `()` akan "diteriakkan" (ditampilkan) oleh komputer ke layar kita.

Namun, ada satu aturan ketat dari komputer: Jika kita ingiin menampilkan (huruf, kata, atau kalimat), teks tersebut wajib diapit oleh tanda kutip ganda (`" "`) atau tanda kutip tunggal (`' '`).

Dalam dunia pemrograman, teks yang diapit oleh tnada kutip ini disebut sebagai **String**. Tanda kutip berfungsi sebagai pemisah untuk memberi tahu komputer: "*Hei, ini cuma teks biasa yang harus kamu tampilkan, ini bukan kode perintah rahasia.*" Jika kita lupa memakai tanda kutip, komputer akan bingung (*error*).

**Langkah Praktis di VS Code:**

1. Buka aplikasi VS Code kita.

2. Buat berkas (*file*) baru dan simpan dengan nama `latihan1.py`.
   (*Catatan: Akhiran `.py` wajib digunakan untuk memberi tagu komputer bahwa berkas tersebut berisi instruksi bahasa Python*).

**Latihan**:
Berdasarkan penjelasan diatas, jika instruksi untuk menampilkan kata Halo adalah `print("Halo")`, coba kita tuliskan disini (dan juga di VS Code kita) kode persis yang harus diketik untuk menyuruh komputer menampilakan kalimat berikut:

`Halo dunia, saya siap menjadi Software Engineer!`

Setelah kita mengetiknya di VS Code, coba jalankan kodenya (biasanya dengan menekan tombol 'Play' di pojok kanan atas layar VS Code). Coba tuliskan kode kita dan apa hasil yang muncul!

```python
print("Halo dunia, saya siap menjadi Software Engineer!")
```

```terminal
Halo dunia, saya siap menjadi Software Engineer!
```

**Kesimpulan Materi:** Perintah `print()` adalah cara kita menyuruh komputer berbicara, dan teks biasa harus selalu diapit oleh tanda kutip agar dikenali sebagai *String* (teks) oleh komputer.

---

### Variabel

Menyimpan informasi.

**Fokus Pembelajaran:** Memahami cara komputer menyimpan dan memanggil kembali sebuah data.

Di program sebelumnya, kita langsung menyuruh komputer menampilkan teks. Namun, bagaimana jika kita ingin komputer mengingat nama kita, lalu memanggilnya berkali-kali di bagian program yang lain? Disinilah kita menggunakan **Varibel**.

Bayangkan variabel sebagai sebuah kardus kosong. Kita bisa memasukan barang apa saja ke dalamnya, lalu kita menempelkan label nama di luar kardusnya agar tidak lupa isinya.

Contoh di Python:

```Python
nama = "Budi"
```

Di sini, kita membuat kardus (variabel) berlabel `nama`, dan kita memasukan teks `"Budi"` ke dalamnya. Tanda samas dengan (`=`) di sini bukan berarti "sama dengan" seperti matematika, melainkan perintah **Memasukkan nilai** (dari kanan ke kiri).

Jika ingin melihat isi kardus tersebut, kita cukup memanggil labelnya:

```Python
print(nama)
```

*Catatan penting:* Perhatikan bahwa saat kita memanggil variabel di dalam `print()`, kita **tidak** menggunakan tanda kutip. Jika kita menggunakan tanda kutip `print("nama")`, komputer akan mencetak kata "nama", bukan isinya ("Budi").

**Latihan Anda:**
Coba buat sebuah kode di VS Code dengan dua langkah ini:

1. Buat sebuah variabel bernama `cita_cita` dan masukkan teks `Software Engineer` ke dalamnya.

2. Gunakan perintah `print()` untuk menampilkan isi dari variabel `cita_cita` tersebut ke layar.

**Praktik:**

```Python
cita_cita = "Software Engineer"

print(cita_cita)
```

```Terminal
Software Engineer
```

Sifat utama dari variabel adalah nilainya bisa diubah. Jika dibaris paling bawah ditambahkan kode `cita_cita = "Tech Lead"` lalu mencetaknya lagi dengan `print(cita_cita)`, komputer akan menampilkan "Tech Lead". Komputer mengeksekusi kode dari atas ke bawah dan selalu mengingat isi yang paling baru.

**Praktik:**

```Python
cita_cita = "Software Engineer"

print(cita_cita)

cita_cita = "Tech Lead"

print(cita_cita)
```

```Terminal
Tech Lead
```

**Kesimpulan Materi:**
Variabel adalah wadah menyimpan data. Untuk melihat isinya, kita memanggil nama variabel tersebut di dalam `print()` tanpa menggunakan tanda kutip.

---

### Tipe Data

