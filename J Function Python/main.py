# Another function like print, `input`
name = input('What is your name?')
print('Hello', name)

# Create function and invoke
def hello():
  print('Hello World')
  
hello()

# Example Function for Adding number
def addition(a, b):
  print(a + b)
  
addition(1, 5)   # 6

# another
def total_checkout(price, discount, shipping):
  total_price = price * discount + shipping
  print(total_price)
  
total_checkout(100, 0.25, 50)

# another
price = 80.50
discount = 0.10

def total_check(p, d):
    # Menghitung harga setelah diskon
    final_price = p * (1 - d)
    print(f"Harga awal: {p}")
    print(f"Diskon: {d * 100}%")
    print(f"Total yang harus dibayar: {final_price}")

# Memanggil fungsi dengan memasukkan variabel sebagai argumen
total_check(price, discount)   # 72.45

# Another
price = 80.50
discount = 0.10

def calculate_total(p, d):
    # Menghitung harga setelah diskon
    final_price = p * (1 - d)
    
    # "Mengembalikan" nilai agar bisa disimpan di luar fungsi
    return final_price

# Memanggil fungsi dan MENYIMPAN hasilnya ke dalam variabel baru
hasil_belanja = calculate_total(price, discount)

# Sekarang kita bisa menggunakan variabel 'hasil_belanja' kapan saja
print(f"Tagihan yang harus dibayar adalah: Rp{hasil_belanja}")

# Contoh penggunaan ulang: jika bayar pakai uang 100
kembalian = 100 - hasil_belanja
print(f"Uang kembalian Anda: Rp{kembalian}")

# Parameter: gaji_pokok, bonus
def hitung_total_gaji(gaji_pokok, bonus):
    total = gaji_pokok + bonus
    return total # Mengirim hasil keluar

# Argumen: 5000000, 1500000
gaji_bulan_ini = hitung_total_gaji(5000000, 1500000)

# Karena ada RETURN, kita bisa mengolah hasilnya lagi
pajak = gaji_bulan_ini * 0.05
print(f"Gaji setelah pajak: {gaji_bulan_ini - pajak}")