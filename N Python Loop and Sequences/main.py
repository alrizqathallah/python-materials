# Membuat List
kota = ['Jakarta', 'Bandung', 'Surabaya']

# Memanggil item pada List
print(kota)   # Hasil: ['Jakarta', 'Bandung', 'Surabaya']
print(kota[0])   # Hasil: 'Jakarta' (memanggil salah satu item pada list, berdasarkan indeks-nya)

# Negative Indexing
print(kota[-1])   # Hasil: 'Surabaya' (memanggil item list paling terakhir, indeks terkahir)

# Fungsi Len
angka = [1, 2, 3, 4, 5]
print(len(angka))   # Hasil: 5 (panjang list (index) 5)

# Fungsi List
nama = 'Budi'
print(list(nama))

# Mengganti item pada List
bahasa = ['Python', 'Jav', 'C++', 'Rust']
print(bahasa)
bahasa[0] = 'JavaScript'   # Mengganti index ke-0 dari 'Python' menjadi 'JavaScript'
print(bahasa)   # Hasil: ['JavaScript', 'Java', 'C++', 'Rust']

# Menghapus Item List dengan kata kunci `del`
karyawan = ['Budi', 23, 'Programmer']
print(karyawan)   # Hasil: ['Budi', 23, 'Programmer']
del karyawan[1]   # Statement ini akan menghapus index ke-1 (23)
print(karyawan)   # Hasil: ['Budi', 'Programmer']

# Mengecek isi List dengan operator `in`
bahasa = ['Python', 'Java']
print('Java' in bahasa)   # Hasil: True (Benar)
print('Ruby' in bahasa)   # Hasil: False (Salah)

# Mengecek Nested List
data = ['Alice', 25, ['Python', 'Rust', 'C++'], ['JavaScript', 'Java']]
print(data[2][1])   # Hasilnya: 'Rust'
print(data[3])   # Hasil: ['JavaScript', 'Java']
print(data[3][1])   # Hasil: 'Java'

# Melakukan Unpacking pada List
profil = ['Alice', 34, 'Developer']
nama, usia, pekerjaan = profil

print(nama)   # Hasil: 'Alice'
print(pekerjaan)   # Hasil: 'Developer'

# Unpacking dengan bersamaan `*`
siswa = ['Ali', 'Budi', 'Carlos']
siswa_pertama, *siswa_lainnya = siswa
#print(siswa_pertama)   # Hasil: 'Ali'
print(siswa_lainnya)   # Hasil: ['Budi', 'Carlos']

# Melakukan Slicing pada List
kue = ['Bolu', 'Kukis', 'Es Krim', 'Pie', 'Brownies']
print(kue[1:4])   # Hasil: ['Kukis', 'Es Krim', 'Pie']

# Melakukan Slicing - Step
bilangan = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bilangan[1::2])   # Hasil: [2, 4, 6, 8]. Mulai dari index ke-1, naik dua index setelahnya [2, 4, 6, 8]
print(bilangan[1::3])   # Hasil: [2, 5, 8]. Mulai dari index ke-1, naik dua index setelahnya [2, 5, 8]

# Menambah item menggunakan `append()`
angka = [1, 2, 3, 4, 5]
angka.append(6)

print(angka)   # Hasil: [1, 2, 3, 4, 5, 6]

# Menggunakan method append() - Nesting List
angka = [1, 3, 5]
angka_genap = [2, 4, 6]
angka.append(angka_genap)

print(angka)   # Hasil: [1, 3, 5, [2, 4, 6]]

# Menambahkan List dengan method `extend()`
angka = [1, 2, 3]
angka_ditambah = [4, 5, 6]
angka.extend(angka_ditambah)

print(angka)   # Hasil: [1, 2, 3, 4, 5, 6]

# Menambahkan item menggunakan method `insert()`
angka = [1, 2, 4, 5]
angka.insert(2, 3)   # 2 adalah index yang hendak disisipkan, dan 3 merupakan item yang dimasukan

print(angka)   # [1, 2, 3, 4, 5]

# Menghapus item menggunakan `remove()`
nilai = [10, 20, 30, 40, 50, 60 , 50]
nilai.remove(50)   # statment ini akan menghapus nilai (value) 50 yang ada pada List

print(nilai)   # Hasil: [10, 20, 30, 40, 60, 50]

# Menghapus item pada List dengan `pop()`
angka = [1, 2, 3, 4, 5, 6]
angka.pop(1)   # statement ini akan menghapus nilai 2 pada List

print(angka)   # Hasil: [1, 3, 4, 5, 6]

angka.pop()   # statement ini akan menghapus nilai terakhir pada List, dengan tidak menambahkan argumen apapun pada method `pop()`

print(angka)   # Hasil: [1, 3, 4, 5]

# Menghapus seluruh item pada List menggunakan method `remove()`
angka = [1, 2, 3, 4, 5]
angka.clear()   # statement ini akan menghapus semua item pada List

print(angka)   # Hasil: []. Semua item pada list tidak akan muncul karena dihapus seleruhnya.

# Menggunakan method `sort()` untuk mengurutkan item pada List
angka = [1, 99, 21, 87, 35, 76, 66, 55, 44]
angka.sort()   # statement ini akan mengurutkan item pada list sesuai urutan bilangan

print(angka)   # Hasil: [1, 21, 35, 44, 55, 66, 76, 87, 99]

# Sesuai abjat alpabetikal
huruf = ['e', 'a', 'f', 'd', 'c', 'b',]
huruf.sort()

print(huruf)

# Menggunakan `sorted()` untuk mengurutkan item List
acak = [19, 2, 35, 1, 67]
rapi = sorted(acak)

print(acak) # Tetap berantakan: [19, 2, 35, 1, 67]
print(rapi) # Rak baru yang rapi: [1, 2, 19, 35, 67]

# Menggunakan method `reverse()` pada item List
item = [5, 4, 3, 2, 1]
item.reverse()   # statement ini akan membalikan urutan pada list (reverse)

print(item)   # Hasil: [1, 2, 3, 4, 5]

# Menggunakan method `index()` untuk mencari index item pada List
bahasa = ['Python', 'Java', 'C++', 'Rust']
print(bahasa.index('Java'))   # Hasil: 1, statement ini akan mencari dimana letak index dari 'Java', yaitu index ke-1

# Tipe Data Tuple
karyawan = ('Alice', 24, 'Rust Developer')

# Mengakses Nilai didalam Tuple
print(karyawan[1])   # Hasil: 24.

# Mengakses dengan Metode Negative Indexing
angka = (1, 2, 3, 4, 5)
print(angka[-1])   # Hasil: 5. Mengakses index paling belakang dari Tuple.

# Menggunakan fungsi tuple()
nama = 'Jessica'
print(tuple(nama))   # Hasil: ['J', 'e', 's', 's', 'i', 'c', 'a']

# Menggunakan operator `in`, untuk mengecek nila pada Tuple
bahasa = ('Python', 'Java', 'C++', 'Rust', 'JavaScript')
print('Rust' in bahasa)   # Hasil: True. Karena nilai 'Rust' tersedia didalam Tuple.
print('javaScript' in bahasa)   # Hasil: False. Karena nilai 'JavaScript' tidak tersedia didalam Tuple. Case-sensitive

# Unpacking Nilai pada Tuple
karyawan = ('Alice', 34, 'Rust Developer')
nama, umur, pekerjaan = karyawan   # statement ini akan memecah nilai pada Tuple kedalam variabel baru yang disediakan (nama, umur dan pekerjaan)
print(nama)   # Hasil: 'Alice'
print(umur)   # Hasil: 34
print(pekerjaan)   # Hasil: 'Rust Developer'

# Melakuka unpacking pada satu nilai dan mengirim sisanya kesatu variabel.
karyawan = ('Alice', 34, 'Rust Developer')
nama, *sisanya = karyawan   # statement ini akan melakukan unpack pada nilai 'Alice' kedalam variabel nama, dan memasukan nilai lain kedalam variabel *sisanya.
print(nama)   # Hasil: 'Alice'.
print(*sisanya)   # Hasil: (34 Rust Developer)

# Melakukan Slicing pada Tuple
kue = ('Pie', 'Bolu', 'Brownis', 'Pukis', 'Pancong')
print(kue[1:3])   # Hasil: (Bolu, Brownis)

# Menggunakan Method count()
bahasa = ('Python', 'Java', 'Rust', 'C++', 'JavaScript', 'Rust')

print(bahasa.count('Rust'))   # Hasil: 2. Dalam statement tersebut diketahui bahwa Rust memiliki 2 nilai didalam tuple bahasa

# Jika Nilai yang dicari tidak ada didalam Tuple
bahasa = ('Python', 'Java', 'Rust', 'C++', 'JavaScript', 'Rust')

print(bahasa.count('C#'))   # Hasil: 0.

# Menggunakan method index() untuk mencari index suatu nilai didalam Tuple
bahasa = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(bahasa.index('Java')) # Hasilnya: 1 (Laci kedua)

bahasa = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
# Cari kata 'Python', tapi mulai pencarian dari laci nomor 3
print(bahasa.index('Python', 3)) # Hasilnya: 5
# Python mengabaikan 'Python' di laci nomor 2, dan langsung menemukan 'Python' berikutnya di laci nomor 5

bahasa = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript')
# Cari 'Python', mulai dari laci 2, tapi berhenti mencari sebelum laci 5
print(bahasa.index('Python', 2, 5)) # Hasilnya: 2

# Menggunakan Method sorted()
angka = (13, 2, 78, 3, 45, 67, 18, 7)
angka_rapi = sorted(angka)

print(angka_rapi) # Hasilnya berupa LIST BARU: [2, 3, 7, 13, 18, 45, 67, 78]

# Menggunakan key=len untu menyortir nilai di Tuple
bahasa = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(bahasa, key=len)) 
# Hasilnya: ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

# Melakukan Sortir Terbalik dengan reverse=True
bahasa = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(bahasa, reverse=True))
# Hasilnya: ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']

