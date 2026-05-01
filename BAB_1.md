# Pondasi Pemrograman

## Berpikir seperti komputer

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

