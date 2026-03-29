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