# Fungsi
# Membuat fungsi (profil toko)
def tampilkan_toko():
  print("Bengs Shop")
  print("Lebak Bulus, Jakarta")
  print("Sesuai pesanan Anda!")

tampilkan_toko()
tampilkan_toko()

# Parameter & Argumen
# 'nama' di dala kurung adalah Parameter (lubang penampung)
def sapa_pelanggan(nama):
  print("Halo, selamat datang,", nama)

# "Budi" dan "Siti" adalah Argumen (data yang dimasukkan)
sapa_pelanggan("Budi")
sapa_pelanggan("Siti")

# Membuat fungsi (proses_pesanan)
def proses_pesanan(nama_pelanggan, barang_dibeli):
  print("Pesanan,", barang_dibeli, "untuk Bapak/Ibu", nama_pelanggan, "sedang disiapkan!")

proses_pesanan("Alrizq", "Kemeja")
proses_pesanan("Rica", "Sepatu")

# Return (Mengembalikan Nilai)
def tambah_print(a, b):
  hasil = a + b
  print(hasil)

tambah_print(5, 10) # Langsung muncul 5 di layar. Selesai.

def tambah_return(a, b):
  hasil = a + b
  return hasil

# Karena fungsi ini 'menyerahkan' hasil, kita bisa menagkapnya dengan variabel
angka_baru = tambah_return(5, 10)

# Sekarang kita bisa memprosesnya lagi!
total_akhir = angka_baru * 2
print("Total akhir setelah dikali dua:", total_akhir)

# Membuat fungsi (Perhitungan pajak barang)
def hitung_pajak(harga_barang):
  pajak = harga_barang * 0.11
  return pajak

pajak_sepatu = hitung_pajak(200000)

print(pajak_sepatu)

# Membuat List
keranjang = ["Kemeja", "Sepatu", "Topi"]

# Menampilkan semua isi List
print(keranjang)

print(keranjang[1])

keranjang.append("Jaket")

# Membuat List
daftar_belanja = ["Kaos", "Celana", "Sepatu"]

daftar_belanja.append("Topi")

print(daftar_belanja)

print(daftar_belanja[1])

# Perulangan (for) dengan List
keranjang = ["Kemeja", "Sepatu", "Topi"]

for barang in keranjang:
  print("Saya membeli:", barang)
  
karyawan = ["Alrizq", "Athallah", "Sulung"]

for nama in karyawan:
  print("Selemat pagi", nama, "!", "Selemat bekerja.")
  print(f"Selamat pagi {nama}! Selamat bekerja.")
  
# DICTIONARY
# Membuat Dictionary
kontak_guru = {
  "Pak Budi": "0812345678",
  "Bu Siti": "0898765432"
}

# Memanggil data spesifik (menggunakan Kuncinya, bukan indeks angka)
print(kontak_guru["Pak Budi"])

# Menambahkan Data Baru ke Dictionary
kontak_guru["Pak Andi"] = "0855511122"

print(kontak_guru)

# Latihan
data_diri = {
  "nama": "Alrizq Athallah",
  "pekerjaan": "Software Engineer",
  "domisili": "Jakarta",
}

print(data_diri["domisili"])

data_diri["hobi"] = "Belajar"

print(data_diri)

# Try & Except (mengantisipasi kesalahan)
try:
  hasil = 10 / 0
  print(hasil)
except:
  print("Sistem medeteksi kesalahan: Anda tidak bisa membagi dengan angka nol!")
  
# Latihan
buku_telepon = {
  "Andi": "08111",
}

try:
  print(buku_telepon["Budi"])
except:
  print("Maaf, nama tersebut tidak ada di buku telepon.")