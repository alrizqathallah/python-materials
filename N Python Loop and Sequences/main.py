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