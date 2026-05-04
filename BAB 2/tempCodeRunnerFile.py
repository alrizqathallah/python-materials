# Fitur Tambah Kontak
kumpulan_kontak = {}

def tambah_kontak(nama, nomor):
  kumpulan_kontak[nama] = nomor

# Fitur Cari Kontak + Pengaman
def cari_kontak(nama_dicari):
  try:
    print(f"Nomor telepon {nama_dicari} adalah {kumpulan_kontak[nama_dicari]}")
  except:
    print(f"Maaf, kontak {nama_dicari} tidak ditemukan.")
    
# Uji Coba Sistem
tambah_kontak("Bengs", "081287855393")

cari_kontak("Bengs")

cari_kontak("Alrizq")

# Fungsi Tambahan
def lihat_semua_kontak():
  for nama in kumpulan_kontak:
    print(nama)
    
lihat_semua_kontak()