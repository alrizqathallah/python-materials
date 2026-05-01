nama_barang = "mushaf"
harga_satuan = 15000
jumlah_beli = 2
uang_pelanggan = 50000

total_harga = harga_satuan * jumlah_beli

kembalian = uang_pelanggan - total_harga

if uang_pelanggan >= total_harga:
   kembalian = uang_pelanggan - total_harga
   
   print("Barang:", nama_barang)
   print("Jumlah dibeli:", jumlah_beli)
   print("Total Harga:", total_harga)
   print("Jumlah Dibayar:", uang_pelanggan)
   print("Jumlah Kembalian:", kembalian)
  
   for i in range(3):
    print("Terima kasih telah berbelanja!")
else:
  print("Maaf, uang Anda tidak cukup untuk membayar pesanan ini.")
